#!./bin/python
# coding: utf-8
import pychromecast
import random
import time
from pychromecast.controllers.youtube import YouTubeController

# Scan for all chromecasts in the network
def scan_for_ccs():
    ccs = pychromecast.get_chromecasts()
    return ccs

# Get my tv
mycc = None

# If my tv hasn't been discovered, keep trying
while mycc is None:
    ccs = scan_for_ccs()
    for cc in ccs:
        if cc.device.friendly_name == 'iTato':
            mycc = cc
            mycc.wait()
            
print(mycc.status)

yt = YouTubeController()
mycc.register_handler(yt)

videos_to_play = [
    {'name': 'Power', 'artist': 'Kanye West', 'id': 'L53gjP-TtGE'},
    {'name': 'Wally Wilder', 'artist': 'Delicate Steve', 'id': 'MJ7chrLEZm4'}
]

video = random.choice(videos_to_play)
mycc.set_volume(0.4)

yt.play_video(video['id'])
time.sleep(1 * 60) # Wait one minute
mycc.quit_app()

