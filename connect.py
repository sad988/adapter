import pika


class Adapter(object):
    host = None
    port = None
    credentials = None

    def connection(self):
        parameters = pika.ConnectionParameters(self.host, self.port, '/', self.credentials)
        return pika.BlockingConnection(parameters)

    def channel(self):
        connection = self.connection()
        chanel = connection.channel()
        chanel.queue_declare('hello')
