import pika
import asyncio
import websockets

# Function to notify the WebSocket server
async def notify_websocket(data):
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send(data)

# Callback for RabbitMQ messages
def callback(ch, method, properties, body):
    message = body.decode()

    # Avoid forwarding already consumed messages
    if not message.startswith("Consumed: "):
        print(f" [x] Received {message}")
        processed_message = f"Consumed: {message}"
        asyncio.run(notify_websocket(processed_message))

def main():
    credentials = pika.PlainCredentials('admin', 'admin')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port='5672', credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
