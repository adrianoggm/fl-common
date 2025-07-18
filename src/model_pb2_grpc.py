# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
import model_pb2 as model__pb2

GRPC_GENERATED_VERSION = "1.73.1"
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower

    _version_not_supported = first_version_is_lower(
        GRPC_VERSION, GRPC_GENERATED_VERSION
    )
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f"The grpc package installed is at version {GRPC_VERSION},"
        + " but the generated code in model_pb2_grpc.py depends on"
        + f" grpcio>={GRPC_GENERATED_VERSION}."
        + f" Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}"
        + f" or downgrade your generated code using grpcio-tools<={GRPC_VERSION}."
    )


class FederatedServiceStub(object):
    """Servicio gRPC opcional para federated learning"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DistributeModel = channel.unary_unary(
            "/fl_common.proto.FederatedService/DistributeModel",
            request_serializer=model__pb2.ModelParameters.SerializeToString,
            response_deserializer=model__pb2.Empty.FromString,
            _registered_method=True,
        )
        self.SendClientUpdate = channel.unary_unary(
            "/fl_common.proto.FederatedService/SendClientUpdate",
            request_serializer=model__pb2.ClientUpdate.SerializeToString,
            response_deserializer=model__pb2.Ack.FromString,
            _registered_method=True,
        )
        self.SendAggregatedUpdate = channel.unary_unary(
            "/fl_common.proto.FederatedService/SendAggregatedUpdate",
            request_serializer=model__pb2.AggregatedUpdate.SerializeToString,
            response_deserializer=model__pb2.Empty.FromString,
            _registered_method=True,
        )


class FederatedServiceServicer(object):
    """Servicio gRPC opcional para federated learning"""

    def DistributeModel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SendClientUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SendAggregatedUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_FederatedServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "DistributeModel": grpc.unary_unary_rpc_method_handler(
            servicer.DistributeModel,
            request_deserializer=model__pb2.ModelParameters.FromString,
            response_serializer=model__pb2.Empty.SerializeToString,
        ),
        "SendClientUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.SendClientUpdate,
            request_deserializer=model__pb2.ClientUpdate.FromString,
            response_serializer=model__pb2.Ack.SerializeToString,
        ),
        "SendAggregatedUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.SendAggregatedUpdate,
            request_deserializer=model__pb2.AggregatedUpdate.FromString,
            response_serializer=model__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "fl_common.proto.FederatedService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers(
        "fl_common.proto.FederatedService", rpc_method_handlers
    )


# This class is part of an EXPERIMENTAL API.
class FederatedService(object):
    """Servicio gRPC opcional para federated learning"""

    @staticmethod
    def DistributeModel(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/fl_common.proto.FederatedService/DistributeModel",
            model__pb2.ModelParameters.SerializeToString,
            model__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def SendClientUpdate(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/fl_common.proto.FederatedService/SendClientUpdate",
            model__pb2.ClientUpdate.SerializeToString,
            model__pb2.Ack.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def SendAggregatedUpdate(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/fl_common.proto.FederatedService/SendAggregatedUpdate",
            model__pb2.AggregatedUpdate.SerializeToString,
            model__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )
