from concurrent import futures
import logging
import grpc
import chatbot_pb2
import chatbot_pb2_grpc

class Greeter(chatbot_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        while True:
            print(f'{request.name}')
            return chatbot_pb2.HelloReply(message=f'Hello, {request.name}')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chatbot_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()