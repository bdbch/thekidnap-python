import socket

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'learndatasci'

# add your token from https://twitchapps.com/tmi/ here
token = 'oauth:PASS'

# your channel name
channel = '#CHANNEL'

def connect():
  sock = socket.socket()
  sock.connect((server, port))

  sock.send(f"PASS {token}\n".encode('utf-8'))
  sock.send(f"NICK {nickname}\n".encode('utf-8'))
  sock.send(f"JOIN {channel}\n".encode('utf-8'))

  return sock