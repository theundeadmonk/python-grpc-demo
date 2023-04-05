import grpc

from python_grpc_demo.grpc_types.greeting_pb2 import GreetingRequest
from python_grpc_demo.grpc_types.greeting_pb2_grpc import GreeterStub
from python_grpc_demo.client.interceptors.authentication_interceptor import add_authentication

def run():
    authentication = add_authentication('authorization', '42')
    name = input('What is your name?\n')

    with grpc.insecure_channel('localhost:50051') as channel:
        intercept_channel = grpc.intercept_channel(channel, authentication)        
        greeter_stub = GreeterStub(intercept_channel)
        request_data = GreetingRequest(name=name)
        response = greeter_stub.Greet(request_data)
        print(response.greeting)

def chat():
    with grpc.insecure_channel('localhost:50051') as channel:
        greeter_stub = GreeterStub(channel)

        request_iterator = iter(
            [
                GreetingRequest(name="Alice"), 
                GreetingRequest(name="Bob")
            ]
        )
        response_iterator = greeter_stub.Chat(request_iterator)
        for response in response_iterator:
            print(response.greeting)