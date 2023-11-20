import os
import socket

from dotenv import load_dotenv

load_dotenv()

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'learndatasci'

token = os.environ.get("TWITCH_TOKEN")

# your channel name
channel = os.environ.get("TWITCH_CHANNEL")

def connect():
  sock = socket.socket()
  sock.connect((server, port))

  sock.send(f"PASS {token}\n".encode('utf-8'))
  sock.send(f"NICK {nickname}\n".encode('utf-8'))
  sock.send(f"JOIN #{channel}\n".encode('utf-8'))

  return sock