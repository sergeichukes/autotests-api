import asyncio
import websockets
from websockets import ServerConnection
import random


async def echo(websocket_connection: ServerConnection):
    async for message in websocket_connection:
        print(f'Получено сообщение: {message}')
        response = f'Сервер получил: {message} и добавил {random.randint(0, 12313)}'

        await websocket_connection.send(response)


async def main():
    server = await websockets.serve(echo, 'localhost', 8765)
    print('Сервер запущен на ws://localhost:8765')
    await server.wait_closed()


asyncio.run(main())
