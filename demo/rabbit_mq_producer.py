#!/usr/bin/env python
import pika

# Use the below command to run RabbitMQ with Docker
# > docker run -d --hostname rabbitmq --name rabbit-server -e RABBITMQ_DEFAULT_USER=admin -e RABBITMQ_DEFAULT_PASS=admin -p 5672:5672 -p 15672:15672 rabbitmq:3-management

credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port='5672', credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')

# Publish a message
channel.basic_publish(exchange='', routing_key='hello', body='Hello from RabbitMQ Producer!')
print(" [x] Sent 'Hello from RabbitMQ Producer!'")
connection.close()
