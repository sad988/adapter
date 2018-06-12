import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
chanel = connection.channel()
chanel.queue_declare('hello')