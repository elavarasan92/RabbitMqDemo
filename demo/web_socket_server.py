import asyncio
import websockets
import pika

# RabbitMQ Producer - send messages to the RabbitMQ queue
def send_to_rabbitmq(message):
    credentials = pika.PlainCredentials('admin', 'admin')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port='5672', credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='', routing_key='hello', body=message)
    connection.close()

# WebSocket handler
async def echo(websocket):
    print("A client connected!")
    try:
        async for message in websocket:
            print(f"Received message from client: {message}")

            # Ignore messages that start with "Consumed: " (already processed)
            if not message.startswith("Consumed: "):
                # Send the message to RabbitMQ
                send_to_rabbitmq(message)
                print("Message sent to RabbitMQ")

                # Wait for 30 seconds before responding
                await asyncio.sleep(30)

                await websocket.send("Message sent to RabbitMQ. Waiting for consumer...")
    except websockets.exceptions.ConnectionClosed:
        print("A client disconnected!")

# Start the WebSocket server
async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("WebSocket server started on ws://localhost:8765")
    await server.wait_closed()

# Run the server
asyncio.run(main())
