import grpc
from concurrent import futures

import user_service_pb2
import user_service_pb2_grpc


class UserServiceServicer(user_service_pb2_grpc.UserServiceServicer):
    def GetUser(self, request, context):
        print(f'Получен запрос к методу GetUser для пользователя: {request.username}')
        return user_service_pb2.GetUserResponse(message=f"Привет, {request.username}")

    def PostUser(self, request: user_service_pb2.PostUserRequest, context):
        print(f'Получен запрос на создание юзера: {request} \n и с контекстом: {context.set_code(200)}')
        return user_service_pb2.GetUserResponse(message=f"Привет, {request.fullName}")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_service_pb2_grpc.add_UserServiceServicer_to_server(UserServiceServicer(), server)
    server.add_insecure_port('[::]:50051')

    server.start()
    print("grpc запущен")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
