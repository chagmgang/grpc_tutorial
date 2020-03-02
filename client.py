import logging
import grpc
import chatbot_pb2
import chatbot_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    step = 0
    while True:
        step += 1
        stub = chatbot_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(chatbot_pb2.HelloRequest(name=step))
        print(f'Greeter client received: {response.message} {step}')
    

if __name__ == '__main__':
    logging.basicConfig()
    run()