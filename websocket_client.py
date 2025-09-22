import asyncio
import websockets


async def client():
    base_url = 'ws://localhost:8765'
    async with websockets.connect(base_url) as ws_connection:
        message = 'Привет, сервер'
        print(f'Отправляем на сервер от клиента: {message}')

        for _ in range(7):
            await ws_connection.send(message)
            response = await ws_connection.recv()
            print(f'Получили ответ от сервера: {response}')


asyncio.run(client())
