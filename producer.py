''' 
Simple Producer which generates 500 test messages with random delay
'''
import pika
import json
import random
from faker import Faker
from time import sleep

fake = Faker()

credentials = pika.PlainCredentials('admin', 'admin')
connection = connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))

channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

#send 500 messages with random delay 
for i in range(1, 5000000000):
    message = {
        "name": fake.name(),      
        "email_id": fake.email(),      
        "address": fake.address()
        }
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=json.dumps(message),
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
        ))
    print(" [x] Sent %r" % json.dumps(message))

connection.close()
