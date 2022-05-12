import grpc
import tictactoe_pb2
import tictactoe_pb2_grpc

def run():
    
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = tictactoe_pb2_grpc.GamerStub(channel)
        
        response = stub.SayTic(tictactoe_pb2.HelloRequest(name='John'))
        print("Gamer client received: " + response.message)
        
        response = stub.SayTac(tictactoe_pb2.HelloRequest(name='Aryan'))
        print("Gamer client received: " + response.message)
        
        response = stub.SayToe(tictactoe_pb2.HelloRequest(name='Nikhil'))
        print("Gamer client received: " + response.message)
        


if __name__ == '__main__':
    run()
