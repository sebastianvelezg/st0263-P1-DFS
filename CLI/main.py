import grpc
import os
from concurrent import futures
import requests
import re
from dotenv import load_dotenv

import sys
from pathlib import Path

project_root = Path(__file__).parent.parent / 'proto'

sys.path.append(str(project_root))
import dfs_pb2_grpc
import dfs_pb2


class CLIInterface:
    def __init__(self, name_node_url):
        self.name_node_url = name_node_url

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def continue_text(self):
        input("Press Enter to continue...")
        self.clear_screen()

    def interactuar_cli(self):
        while True:
            self.clear_screen()
            print("----------------------------------")
            print("Sistema de archivos distribuidos DFS")
            print("----------------------------------")
            print("Seleccione una opción:")
            print("----------------------")
            print("1. Download a file")
            print("2. Upload a file")
            print("3. Search a file")
            print("4. List files")
            print("5. Exit program")
            print("----------------------------------")
            eleccion_usuario = input("Ingrese el número de su elección: ")
            print("----------------------------------")

            if eleccion_usuario == "1":
                self.get_file()
            elif eleccion_usuario == "2":
                self.put_file(input("Ruta del archivo: "))
            elif eleccion_usuario == "3":
                self.find_file(input("Ingrese el nombre exacto del archivo: "))
            elif eleccion_usuario == "4":
                self.list_files()
            elif eleccion_usuario == "5":
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Intente de nuevo.")

            self.continue_text()

    def register(client):
        username = input("Enter username: ")
        password = input("Enter password: ")
        response = client.register(username, password)
        if response['success']:
            print("Cliente Añadido exitosamente a la base dato")
            input("Press Enter to continue...")

        else:
            print("Error al añadir cliente a la base de datos, Verifique que el cliente no exista")
            input("Press Enter to continue...")

    def login(client):
        username = input("Enter username: ")
        password = input("Enter password: ")
        response = client.login(username, password)
        if response['success']:
            print("Inicio de Sesión exitoso")
            return True  
        else:
            print("Error en el inicio de sesión. Verifique su usuario y contraseña.")
            input("Press Enter to continue...")
            return False  

    def get_file(self):
        try:
          
            with grpc.insecure_channel(self.name_node_url) as chan:
                stub = dfs_pb2_grpc.dfsStub(chan)
                list_response = stub.ListFiles(dfs_pb2.EmptyMessage())
                if list_response.status == 200:
                    print("Archivos disponibles:")
                    for idx, file_name in enumerate(list_response.files, 1):
                        print(f"{idx}. {file_name}")
                else:
                    print("No se pudieron obtener los archivos disponibles.")
                    return

            file_idx = int(input("Seleccione un archivo: ")) - 1
            if file_idx < 0 or file_idx >= len(list_response.files):
                print("Selección inválida.")
                return
            file_name = list_response.files[file_idx]

            
            with grpc.insecure_channel(self.name_node_url) as chan:
                stub = dfs_pb2_grpc.dfsStub(chan)
                download_response = stub.NamenodeDownloadFile(dfs_pb2.DownloadFileRequest(fileName=file_name))
                if download_response.status == 200 and download_response.conns:
                    selected_data_node = download_response.conns[0]
                    print(f"Descargando desde DataNode: {selected_data_node}")

           
                    with grpc.insecure_channel(selected_data_node) as dataNodeChan:
                        dataNodeStub = dfs_pb2_grpc.dfsStub(dataNodeChan)
                        filepath = "src/" + file_name
                        with open(filepath, mode="wb") as f:
                            for entry_response in dataNodeStub.DownloadFile(dfs_pb2.DownloadFileRequest(fileName=file_name)):
                                f.write(entry_response.chunk_data)
                            print(f"Archivo '{file_name}' descargado satisfactoriamente de DataNode {selected_data_node}.")
                else:
                    print("El archivo no se encontró en ningún DataNode.")
        except Exception as e:
            print(f"Error durante la descarga: {str(e)}")


    def read_iterfile(self,filepath, chunk_size=1024):
        _, filename = os.path.split(filepath)
        yield dfs_pb2.UploadFileRequest(fileName=filename)
        with open(filepath, mode="rb") as f:
            while True:
                chunk = f.read(chunk_size)
                if chunk:
                    entry_request = dfs_pb2.UploadFileRequest(chunk_data=chunk)
                    yield entry_request
                else:
                    return      

    def find_file(self, file_name):
        with grpc.insecure_channel(self.name_node_url) as chan:
            stub = dfs_pb2_grpc.dfsStub(chan)
            response = stub.FindFile(dfs_pb2.FindFileRequest(fileName=file_name))
            if response.status == 200:
                print(f"El archivo '{file_name}' se encontró en los siguientes DataNodes:")
                for address in response.nodeAddresses:
                    print(address)
            else:
                print(f"El archivo '{file_name}' no se encontró en el sistema.")


    def put_file(self, file_path):
        try:
            with grpc.insecure_channel(self.name_node_url) as chan:
                stub = dfs_pb2_grpc.dfsStub(chan)
                response = stub.NamenodeUploadFile(dfs_pb2.EmptyMessage())
                if response.status == 200 and len(response.conns) > 0:
                    for dataNode in response.conns:
                        with grpc.insecure_channel(dataNode) as dataNodeChan:
                            dataNodeStub = dfs_pb2_grpc.dfsStub(dataNodeChan)
                            dataNodeStub.UploadFile(self.read_iterfile(file_path))
                    print(f"File successfully uploaded to {len(response.conns)} data nodes.")
                else:
                    print("Error: Unable to upload the file. Please ensure at least 2 data nodes are available.")
                    return
        except Exception as e:
            print(f"Error: An exception occurred while uploading the file - {str(e)}")



    def search_files(self, regex):
        with grpc.insecure_channel(self.name_node_url) as chan:
            stub = dfs_pb2_grpc.dfsStub(chan)
            response = stub.SearchFiles(dfs_pb2.SearchFilesRequest(regex=regex))
            if response.status == 200:
                print(response.files)
            else:
                print("Error: No se pudo realizar la búsqueda")


    def list_files(self):
        with grpc.insecure_channel(self.name_node_url) as chan:
            stub = dfs_pb2_grpc.dfsStub(chan)
            request = dfs_pb2.EmptyMessage()
            response = stub.ListFiles(request)

        if response.status == 200:
            print(response.files)
        else:
            print("Error: No se pudo listar los archivos")
            print("Status code: ", response.status)


if __name__ == "__main__":
    load_dotenv()
    namenode = str(os.getenv("namenode")).encode('utf-8')
    print(namenode)
    cli = CLIInterface(namenode)
    cli.interactuar_cli()