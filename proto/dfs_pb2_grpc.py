# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import dfs_pb2 as dfs__pb2


class dfsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PingFiles = channel.unary_unary(
                '/files.dfs/PingFiles',
                request_serializer=dfs__pb2.EmptyMessage.SerializeToString,
                response_deserializer=dfs__pb2.PingFilesResponse.FromString,
                )
        self.ListFiles = channel.unary_unary(
                '/files.dfs/ListFiles',
                request_serializer=dfs__pb2.EmptyMessage.SerializeToString,
                response_deserializer=dfs__pb2.ListFilesResponse.FromString,
                )
        self.DownloadFile = channel.unary_stream(
                '/files.dfs/DownloadFile',
                request_serializer=dfs__pb2.DownloadFileRequest.SerializeToString,
                response_deserializer=dfs__pb2.DownloadFileResponse.FromString,
                )
        self.UploadFile = channel.stream_unary(
                '/files.dfs/UploadFile',
                request_serializer=dfs__pb2.UploadFileRequest.SerializeToString,
                response_deserializer=dfs__pb2.EmptyMessage.FromString,
                )
        self.NamenodeConn = channel.unary_unary(
                '/files.dfs/NamenodeConn',
                request_serializer=dfs__pb2.NameNodeRequest.SerializeToString,
                response_deserializer=dfs__pb2.StatusMessage.FromString,
                )
        self.NamenodeDownloadFile = channel.unary_unary(
                '/files.dfs/NamenodeDownloadFile',
                request_serializer=dfs__pb2.DownloadFileRequest.SerializeToString,
                response_deserializer=dfs__pb2.DataNodeResponse.FromString,
                )
        self.NamenodeUploadFile = channel.unary_unary(
                '/files.dfs/NamenodeUploadFile',
                request_serializer=dfs__pb2.EmptyMessage.SerializeToString,
                response_deserializer=dfs__pb2.DataNodeResponse.FromString,
                )
        self.FindFile = channel.unary_unary(
                '/files.dfs/FindFile',
                request_serializer=dfs__pb2.FindFileRequest.SerializeToString,
                response_deserializer=dfs__pb2.FindFileResponse.FromString,
                )


class dfsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PingFiles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListFiles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownloadFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadFile(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NamenodeConn(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NamenodeDownloadFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NamenodeUploadFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FindFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_dfsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PingFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.PingFiles,
                    request_deserializer=dfs__pb2.EmptyMessage.FromString,
                    response_serializer=dfs__pb2.PingFilesResponse.SerializeToString,
            ),
            'ListFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.ListFiles,
                    request_deserializer=dfs__pb2.EmptyMessage.FromString,
                    response_serializer=dfs__pb2.ListFilesResponse.SerializeToString,
            ),
            'DownloadFile': grpc.unary_stream_rpc_method_handler(
                    servicer.DownloadFile,
                    request_deserializer=dfs__pb2.DownloadFileRequest.FromString,
                    response_serializer=dfs__pb2.DownloadFileResponse.SerializeToString,
            ),
            'UploadFile': grpc.stream_unary_rpc_method_handler(
                    servicer.UploadFile,
                    request_deserializer=dfs__pb2.UploadFileRequest.FromString,
                    response_serializer=dfs__pb2.EmptyMessage.SerializeToString,
            ),
            'NamenodeConn': grpc.unary_unary_rpc_method_handler(
                    servicer.NamenodeConn,
                    request_deserializer=dfs__pb2.NameNodeRequest.FromString,
                    response_serializer=dfs__pb2.StatusMessage.SerializeToString,
            ),
            'NamenodeDownloadFile': grpc.unary_unary_rpc_method_handler(
                    servicer.NamenodeDownloadFile,
                    request_deserializer=dfs__pb2.DownloadFileRequest.FromString,
                    response_serializer=dfs__pb2.DataNodeResponse.SerializeToString,
            ),
            'NamenodeUploadFile': grpc.unary_unary_rpc_method_handler(
                    servicer.NamenodeUploadFile,
                    request_deserializer=dfs__pb2.EmptyMessage.FromString,
                    response_serializer=dfs__pb2.DataNodeResponse.SerializeToString,
            ),
            'FindFile': grpc.unary_unary_rpc_method_handler(
                    servicer.FindFile,
                    request_deserializer=dfs__pb2.FindFileRequest.FromString,
                    response_serializer=dfs__pb2.FindFileResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'files.dfs', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class dfs(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PingFiles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/files.dfs/PingFiles',
            dfs__pb2.EmptyMessage.SerializeToString,
            dfs__pb2.PingFilesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListFiles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/files.dfs/ListFiles',
            dfs__pb2.EmptyMessage.SerializeToString,
            dfs__pb2.ListFilesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DownloadFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/files.dfs/DownloadFile',
            dfs__pb2.DownloadFileRequest.SerializeToString,
            dfs__pb2.DownloadFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UploadFile(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/files.dfs/UploadFile',
            dfs__pb2.UploadFileRequest.SerializeToString,
            dfs__pb2.EmptyMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NamenodeConn(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/files.dfs/NamenodeConn',
            dfs__pb2.NameNodeRequest.SerializeToString,
            dfs__pb2.StatusMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NamenodeDownloadFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/files.dfs/NamenodeDownloadFile',
            dfs__pb2.DownloadFileRequest.SerializeToString,
            dfs__pb2.DataNodeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NamenodeUploadFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/files.dfs/NamenodeUploadFile',
            dfs__pb2.EmptyMessage.SerializeToString,
            dfs__pb2.DataNodeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FindFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/files.dfs/FindFile',
            dfs__pb2.FindFileRequest.SerializeToString,
            dfs__pb2.FindFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
