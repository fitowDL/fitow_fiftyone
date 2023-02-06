# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import FFRPC_pb2 as FFRPC__pb2


class FFRPCStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetIDs = channel.unary_unary(
                '/fitow.FFRPC/GetIDs',
                request_serializer=FFRPC__pb2.m_say.SerializeToString,
                response_deserializer=FFRPC__pb2.m_ids.FromString,
                )
        self.GetLength = channel.unary_unary(
                '/fitow.FFRPC/GetLength',
                request_serializer=FFRPC__pb2.m_say.SerializeToString,
                response_deserializer=FFRPC__pb2.m_length.FromString,
                )
        self.GetDatasetInfos = channel.unary_unary(
                '/fitow.FFRPC/GetDatasetInfos',
                request_serializer=FFRPC__pb2.m_say.SerializeToString,
                response_deserializer=FFRPC__pb2.m_say.FromString,
                )
        self.HeartBeat = channel.stream_stream(
                '/fitow.FFRPC/HeartBeat',
                request_serializer=FFRPC__pb2.m_say.SerializeToString,
                response_deserializer=FFRPC__pb2.m_say.FromString,
                )
        self.GetLabels = channel.stream_stream(
                '/fitow.FFRPC/GetLabels',
                request_serializer=FFRPC__pb2.m_say.SerializeToString,
                response_deserializer=FFRPC__pb2.m_label_stream.FromString,
                )


class FFRPCServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetIDs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLength(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDatasetInfos(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HeartBeat(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLabels(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FFRPCServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetIDs': grpc.unary_unary_rpc_method_handler(
                    servicer.GetIDs,
                    request_deserializer=FFRPC__pb2.m_say.FromString,
                    response_serializer=FFRPC__pb2.m_ids.SerializeToString,
            ),
            'GetLength': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLength,
                    request_deserializer=FFRPC__pb2.m_say.FromString,
                    response_serializer=FFRPC__pb2.m_length.SerializeToString,
            ),
            'GetDatasetInfos': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDatasetInfos,
                    request_deserializer=FFRPC__pb2.m_say.FromString,
                    response_serializer=FFRPC__pb2.m_say.SerializeToString,
            ),
            'HeartBeat': grpc.stream_stream_rpc_method_handler(
                    servicer.HeartBeat,
                    request_deserializer=FFRPC__pb2.m_say.FromString,
                    response_serializer=FFRPC__pb2.m_say.SerializeToString,
            ),
            'GetLabels': grpc.stream_stream_rpc_method_handler(
                    servicer.GetLabels,
                    request_deserializer=FFRPC__pb2.m_say.FromString,
                    response_serializer=FFRPC__pb2.m_label_stream.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'fitow.FFRPC', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FFRPC(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetIDs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fitow.FFRPC/GetIDs',
            FFRPC__pb2.m_say.SerializeToString,
            FFRPC__pb2.m_ids.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLength(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fitow.FFRPC/GetLength',
            FFRPC__pb2.m_say.SerializeToString,
            FFRPC__pb2.m_length.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDatasetInfos(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fitow.FFRPC/GetDatasetInfos',
            FFRPC__pb2.m_say.SerializeToString,
            FFRPC__pb2.m_say.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HeartBeat(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/fitow.FFRPC/HeartBeat',
            FFRPC__pb2.m_say.SerializeToString,
            FFRPC__pb2.m_say.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLabels(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/fitow.FFRPC/GetLabels',
            FFRPC__pb2.m_say.SerializeToString,
            FFRPC__pb2.m_label_stream.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)