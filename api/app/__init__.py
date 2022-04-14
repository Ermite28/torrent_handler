from flask import Flask
from time import sleep
from .message_broker import MessageBroker

app = Flask(__name__)
# sleep(5) # TODO fix that
# message_broker = MessageBroker()

from app import routes
