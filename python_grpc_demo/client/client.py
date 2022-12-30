import grpc

from python_grpc_demo.grpc_types.greeting_pb2 import GreetingRequest
from python_grpc_demo.grpc_types.greeting_pb2_grpc import GreeterStub

def run():
    name = input('What is your name?\n')

    with grpc.insecure_channel('localhost:50051') as channel:
        greeter_stub = GreeterStub(channel)
        request_data = GreetingRequest(name=name)
        response = greeter_stub.Greet(request_data)
        print(response.greeting)