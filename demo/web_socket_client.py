import asyncio
import websockets
import time

async def test():
    async with websockets.connect("ws://localhost:8765") as websocket:
        # Record the start time before sending the message
        start_time = time.time()

        await websocket.send("Hello from WebSocket Client!")
        print("Message sent to WebSocket server.")

        # Wait for the response from the server
        response = await websocket.recv()
        print(f"Response from server: {response}")

        # Record the end time after receiving the response
        end_time = time.time()

        # Calculate the response time
        response_time = end_time - start_time
        print(f"Response time: {response_time:.2f} seconds")

# Run the client
asyncio.run(test())
