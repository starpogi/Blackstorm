import dataclasses
import logging
import random
import requests
import time
import os

from colors import CIE
from colors.animations import ColorAnimation
from colors.frames import ColorFrame
from lights import Light

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

KEY = os.environ.get('KEY')
IP = os.environ.get('IP')

lights = [
    Light(id=9),
    Light(id=10),
    Light(id=11),
    Light(id=21)
]
fire_profile = ColorAnimation(rate_s=0.8,
                              frames=[
                                  ColorFrame(color=CIE(x=0.70, y=0.29), 
                                             light=lights[0]),
                                  ColorFrame(color=CIE(x=0.65, y=0.35), 
                                             light=lights[1]),
                                  ColorFrame(color=CIE(x=0.62, y=0.30), 
                                             light=lights[2]),
                                  ColorFrame(color=CIE(x=0.60, y=0.35), 
                                             light=lights[3]),
                                  ColorFrame(color=CIE(x=0.70, y=0.29), 
                                             light=lights[1]),
                                  ColorFrame(color=CIE(x=0.65, y=0.35), 
                                             light=lights[2]),
                                  ColorFrame(color=CIE(x=0.62, y=0.30), 
                                             light=lights[3]),
                                  ColorFrame(color=CIE(x=0.60, y=0.35), 
                                             light=lights[0]),
                                  ColorFrame(color=CIE(x=0.70, y=0.29), 
                                             light=lights[2]),
                                  ColorFrame(color=CIE(x=0.65, y=0.35), 
                                             light=lights[3]),
                                  ColorFrame(color=CIE(x=0.62, y=0.30), 
                                             light=lights[0]),
                                  ColorFrame(color=CIE(x=0.60, y=0.35), 
                                             light=lights[1]),
                                  ColorFrame(color=CIE(x=0.70, y=0.29), 
                                             light=lights[3]),
                                  ColorFrame(color=CIE(x=0.65, y=0.35), 
                                             light=lights[0]),
                                  ColorFrame(color=CIE(x=0.62, y=0.30), 
                                             light=lights[1]),
                                  ColorFrame(color=CIE(x=0.60, y=0.35), 
                                             light=lights[2])
                              ])

def change_light(id: int,
                 x: float = None, 
                 y: float = None,
                 hue: int = None,
                 saturation: int = None,
                 temperature: int = None,
                 colormode: str = None,
                 brightness: int = 254,
                 is_on: bool = True, 
                 ip: str = IP, 
                 key: str = KEY):
    payload = {
        "on": is_on,
        "bri": brightness
    }

    if x is not None and y is not None:
        payload.setdefault("xy", [x, y])
    elif hue is not None and saturation is not None:
        payload.setdefault("hue", hue)
        payload.setdefault("sat", saturation)
    elif temperature is not None:
        payload.setdefault("ct", temperature)
        
    request = requests.put(f"http://{ip}/api/{key}/lights/{id}/state", 
                           json=payload)
    log.info(request.content)

def cycle_colors(profile):
    counter = 0
    
    while True:
        frame = profile.frames[counter]
        change_light(frame.light.id,
                     **dataclasses.asdict(frame.color),
                     ip=IP,
                     key=KEY)
        counter += 1

        if counter == len(profile.frames):
            random.shuffle(profile.frames)
            counter = 0

        time.sleep(profile.rate_s)

if __name__ == '__main__':
    cycle_colors(fire_profile)
    