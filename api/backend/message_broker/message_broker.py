import pika
import json
from core.config import Settings
from functools import lru_cache

@lru_cache
def get_settings():
    return Settings()

class MessageBroker:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(get_settings().RABBITMQ_URL))
        self.channel = self.connection.channel()
        self._declare_queue()

    def publish_new_torrent(self, torrent):
        self.channel.basic_publish(exchange="", routing_key="add_torrent", body=json.dumps(torrent))

    def _declare_queue(self):
        self.send_queue = self.channel.queue_declare(queue="add_torrent")
