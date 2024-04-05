import grpc
from dotenv import load_dotenv
import os
import sys
import time
from concurrent import futures
from os.path import isfile, join
from os import listdir
from threading import Thread
from pathlib import Path

proto_directory = Path(__file__).parent.parent / 'proto'

sys.path.append(str(proto_directory))
import dfs_pb2_grpc
import dfs_pb2

HEARTBEAT_INTERVAL = 10

def listFiles():
    files = [f for f in listdir("src/") if isfile(join("src/", f))]
    return files

class Files(dfs_pb2_grpc.dfsServicer):
    def PingFiles(self, request, context):
        response = dfs_pb2.PingFilesResponse(ack='1')
        return response
    def ListFiles(self, request, context):
        try:
            files = listFiles()
            print("ListFiles Request")
            response = dfs_pb2.ListFilesResponse(files=files,status=200)
        except:
            response = dfs_pb2.ListFilesResponse(status=500)
        return response
    def DownloadFile(self, request, context):
        chunk_size = 1024
        print("Download Request")
        filepath = "src/"+request.fileName
        if os.path.exists(filepath):
            print("Sending: "+filepath)
            with open(filepath, mode="rb") as f:
                while True:
                    chunk = f.read(chunk_size)
                    if chunk:
                        entry_response = dfs_pb2.DownloadFileResponse(chunk_data=chunk)
                        yield entry_response
                    else:
                        return
    
    def UploadFile(self, request_iterator, context):
        data = bytearray()
        filepath = 'src/'
        print("UPLOAD Request")

        for request in request_iterator:
            if request.fileName:
                filepath += request.fileName
                print("Uploading: "+request.fileName)
                continue
            data.extend(request.chunk_data)
        with open(filepath, 'wb') as f:
            f.write(data)
        
        namenode = os.getenv("namenode")
        datanode3 = os.getenv("datanode3")
        with grpc.insecure_channel(namenode) as chan:
            stub = dfs_pb2_grpc.dfsStub(chan)
            request = dfs_pb2.NameNodeRequest(conn=datanode3,files=listFiles())
            response = stub.NamenodeConn(request)
            if response.status == 200:
                print("Namenode success!")
        
        return dfs_pb2.EmptyMessage()

def send_heartbeat(namenode, datanode3):
    with grpc.insecure_channel(namenode) as chan:
        stub = dfs_pb2_grpc.dfsStub(chan)
        while True:
            try:
                request = dfs_pb2.NameNodeRequest(conn=datanode3, files=listFiles())
                stub.NamenodeConn(request)
                print("Heartbeat sent")
            except Exception as e:
                print(f"Failed to send heartbeat: {e}")
            time.sleep(HEARTBEAT_INTERVAL)

def createServer():
    namenode = os.getenv("namenode")
    print("namenode", namenode)
    datanode3 = os.getenv("datanode3")
    with grpc.insecure_channel(namenode) as chan:
        stub = dfs_pb2_grpc.dfsStub(chan)
        request = dfs_pb2.NameNodeRequest(conn=datanode3,files=listFiles())
        response = stub.NamenodeConn(request)
        if response.status == 200:
            print("Namenode success!")

    server = grpc.server(futures.ThreadPoolExecutor())

    dfs_pb2_grpc.add_dfsServicer_to_server(Files(),server)

    port = 50053
    server.add_insecure_port('[::]:'+str(port))
    server.start()
    print("server started, port: "+str(port))

    heartbeat_thread = Thread(target=send_heartbeat, args=(namenode, datanode3), daemon=True)
    heartbeat_thread.start()

    server.wait_for_termination()

def main():
    load_dotenv()
    createServer()    

if __name__ == "__main__":
    main()