from concurrent import futures

import grpc
import tictactoe_pb2
import tictactoe_pb2_grpc

class Gamer(tictactoe_pb2_grpc.GamerServicer):
    def SayTic(self, request, context):
        return tictactoe_pb2.HelloReply(message=f"Hello {request.name}! It's me Tic.")
    
    def SayTac(self, request, context):
        return tictactoe_pb2.HelloReply(message=f"Hi {request.name}! I'm Tac.")

    def SayToe(self, request, context):
        return tictactoe_pb2.HelloReply(message=f'Namaste, {request.name}! Toe here.')
    


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tictactoe_pb2_grpc.add_GamerServicer_to_server(Gamer(), server)
    print('Listening at [::]:50051')
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
