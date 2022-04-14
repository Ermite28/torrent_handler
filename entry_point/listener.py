import os, sys
import json
import pika
from torrent_actions import TorrentActions
from time import sleep


class EntryPoint:
    def __init__(self, dispatcher="rabbitmq"):
        sleep(5)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
        self.channel = self.connection.channel()
        self.send_queue = self.channel.queue_declare(queue="add_torrent")
        # self.events_handler = TorrentActions()

    def run(self):
        self._listen()

    def _listen(self):
        self.channel.basic_consume(queue="add_torrent", auto_ack=True, on_message_callback=self.add_torrent)
        print(" [*] Waiting for messages. To exit press CTRL+C")
        self.channel.start_consuming()

    def add_torrent(self, ch, method, properties, body):
        data = json.loads(body)
        print(type(data))
        # print(f"[x] Received {data['name']}")
        # print(data['data'])
        # self.events_handler.add_torrent(**data)


if __name__ == "__main__":
    entry_point = EntryPoint()
    try:
        entry_point.run()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            entry_point.connection.close()
            sys.exit(0)
        except SystemExit:
            os._exit(0)
