import pika

credentials = pika.PlainCredentials('duka', 'Fuckyou31')
parameters = pika.ConnectionParameters(host='138.68.189.32',port=5672, credentials=credentials,heartbeat=0)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='duka-purchases-queue', durable=True)

def send_log_to_queue(message: str):
        channel.basic_publish(
        exchange='',
        routing_key='duka-purchases-queue',
        body=message
    )