# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ocr_request_pb2 as ocr__request__pb2


class ocrApiServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.goURL = channel.unary_unary(
                '/ocr_request.ocrApiService/goURL',
                request_serializer=ocr__request__pb2.urlMsg.SerializeToString,
                response_deserializer=ocr__request__pb2.ApiResponse2.FromString,
                )


class ocrApiServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def goURL(self, request, context):
        """url -> text
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ocrApiServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'goURL': grpc.unary_unary_rpc_method_handler(
                    servicer.goURL,
                    request_deserializer=ocr__request__pb2.urlMsg.FromString,
                    response_serializer=ocr__request__pb2.ApiResponse2.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ocr_request.ocrApiService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ocrApiService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def goURL(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ocr_request.ocrApiService/goURL',
            ocr__request__pb2.urlMsg.SerializeToString,
            ocr__request__pb2.ApiResponse2.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
