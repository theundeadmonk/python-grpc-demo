import grpc
from concurrent import futures
import logging

from python_grpc_demo.grpc_types.greeting_pb2_grpc import add_GreeterServicer_to_server
from python_grpc_demo.server.servicers.greeter import Greeter
from python_grpc_demo.server.interceptors.authentication_interceptor import AuthenticationInterceptor

def serve() -> None:
    logging.basicConfig()
    authenticator = AuthenticationInterceptor(
        'authorization',
        '42',
        grpc.StatusCode.UNAUTHENTICATED,
        'Access denied!'
    )
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10),
        interceptors=(authenticator,)
        )
    add_GreeterServicer_to_server(Greeter(), server)
    port = 50051
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    print("Server started")
    server.wait_for_termination()