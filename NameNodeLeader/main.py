import grpc
import sys
import random
from concurrent import futures
import re
import time
from threading import Thread
from pathlib import Path

proto_directory = Path(__file__).parent.parent / 'proto'

sys.path.append(str(proto_directory))
import dfs_pb2_grpc
import dfs_pb2



nodes = []
files = {}
HEARTBEAT_INTERVAL = 10
DISCONNECT_THRESHOLD = 30

class Files(dfs_pb2_grpc.dfsServicer):
    def __init__(self):
        self.files = {}
        
    def NamenodeConn(self, request, context):
        print("DataNode request")
        if request.conn:
            nodes.append(request.conn)
            files[request.conn] = request.files
            print("-- Conection: "+request.conn)

        return dfs_pb2.StatusMessage(status=200)

    def ListFiles(self, request, context):
        print("LIST Request")
        listFiles = set()
    
        for i in files:
            for file in files[i]:
                listFiles.add(file)

        uniqueListFiles = list(listFiles)
    
        print(uniqueListFiles)
    
        return dfs_pb2.ListFilesResponse(files=uniqueListFiles, status=200)
    
    def NamenodeDownloadFile(self, request, context):
        fileName = request.fileName
        
        nodeAddresses = [node for node, fileList in files.items() if fileName in fileList]
        
        
        if nodeAddresses:
            selected_node = random.choice(nodeAddresses)
            return dfs_pb2.DataNodeResponse(conns=[selected_node], status=200)
        else:
        
            return dfs_pb2.DataNodeResponse(status=404)

    def FindFile(self, request, context):
        fileName = request.fileName
        nodeAddresses = []
        for node, fileList in files.items():
            if fileName in fileList:
                nodeAddresses.append(node)
        if nodeAddresses:
            return dfs_pb2.FindFileResponse(nodeAddresses=nodeAddresses, status=200)
        else:
            return dfs_pb2.FindFileResponse(status=404)
        
    
    def NamenodeUploadFile(self, request, context):
        if len(nodes) < 2:
            return dfs_pb2.DataNodeResponse(status=400)

        selected_nodes = random.sample(nodes, 2)

        response = dfs_pb2.DataNodeResponse(status=200)
        for node in selected_nodes:
            response.conns.append(node)

        return response
    
def check_heartbeat():
    while True:
        disconnected_nodes = []
        for node, last_heartbeat in list(nodes.items()):
            if time.time() - last_heartbeat > DISCONNECT_THRESHOLD:
                print(f"-- Connection lost: {node}")
                disconnected_nodes.append(node)
                del files[node]
        for node in disconnected_nodes:
            del nodes[node]
        time.sleep(HEARTBEAT_INTERVAL)
    
def createServer():
    server = grpc.server(futures.ThreadPoolExecutor())

    dfs_pb2_grpc.add_dfsServicer_to_server(Files(),server)

    port = 50050
    server.add_insecure_port('[::]:'+str(port))
    server.start()
    print("server started, port: "+str(port))
    server.wait_for_termination()

def main():
    createServer()
    

if __name__ == "__main__":
    main()