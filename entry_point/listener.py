import os, sys
import json
import pika
from torrent_actions import TorrentActions
from time import sleep


class EntryPoint:
    def __init__(self, dispatcher="rabbitmq"):
        sleep(10)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
        self.channel = self.connection.channel()
        self.send_queue = self.channel.queue_declare(queue="add_torrent")
        self.events_handler = TorrentActions()

    def run(self):
        self._listen()

    def _listen(self):
        self.channel.basic_consume(queue="add_torrent", auto_ack=True, on_message_callback=self.add_torrent)
        print(" [*] Waiting for messages. To exit press CTRL+C")
        self.channel.start_consuming()

    def add_torrent(self, ch, method, properties, body):
        data = json.loads(body)
        print(data)
        print(type(data))
        #print(f"[x] Received {data['name']}")
        #print(data['data'])
        data = {"magnet":"magnet:?xt=urn:btih:A2AD2A669250A014BED19919E6C386DD4F82A883&dn=Eternals.2021.1080p.WEBRip.DDP5.1.x264-NOGRP&tr=http%3A%2F%2Ftracker.trackerfix.com%3A80%2Fannounce&tr=udp%3A%2F%2F9.rarbg.me%3A2950%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2870%2Fannounce&tr=udp%3A%2F%2Ftracker.tallpenguin.org%3A15720%2Fannounce&tr=udp%3A%2F%2Ftracker.thinelephant.org%3A12780%2Fannounce&tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce"}
        self.events_handler.add_torrent(**data)


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
