import grpc

from python_grpc_demo.grpc_types.greeting_pb2_grpc import GreeterServicer
from python_grpc_demo.grpc_types.greeting_pb2 import GreetingRequest, GreetingResponse

class Greeter(GreeterServicer):
    def Greet(self, request: GreetingRequest, context: grpc.ServicerContext) -> GreetingResponse:
        return GreetingResponse(greeting='Hello %s!' % request.name)

    def Chat(self, request_iterator , context: grpc.ServicerContext):
        for request in request_iterator:
            yield GreetingResponse(greeting=f"Welcome, {request.name}!")
