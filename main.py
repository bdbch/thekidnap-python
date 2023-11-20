# import local "kidnap-controls.py"
import kidnap_controls as kc
import twitch
import re

from dotenv import load_dotenv

controls = kc.Kidnap_Controls()

# list of events
events = [
  "w",
  "s",
  "a",
  "d",
  "shift",
  "click",
  "f",
  "c",
  "ll",
  "ll+",
  "ll++",
  "lr",
  "lr+",
  "lr++",
  "lu",
  "lu+",
  "lu++",
  "ld",
  "ld+",
  "ld++"
]

def main():
  sock = twitch.connect()

  while True:
    resp = sock.recv(2048).decode('utf-8')

    # split from #channelName : and take last element
    message = resp.split(f'{twitch.channel} :')[-1]

    # remove whitespaces and newlines and spaces
    # only allow alphanumeric characters and +
    message = re.sub(r'[^a-zA-Z0-9+]', '', message)
    
    # lowercase
    message = message.lower()

    print(message)
    print(len(message))

    # if message is inside events, send event
    if message in events:
      controls.send_event(message)

main()