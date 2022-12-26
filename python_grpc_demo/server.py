import grpc
from concurrent import futures

from python_grpc_demo.grpc_types.greeting_pb2_grpc import add_GreeterServicer_to_server
from python_grpc_demo.servicers.greeter import Greeter


def serve() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_GreeterServicer_to_server(Greeter(), server)
    port = 50051
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    print("Server started")
    server.wait_for_termination()