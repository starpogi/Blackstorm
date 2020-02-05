import requests
import logging
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
fire_profile = ColorAnimation(rate_s=0.2,
                              frames=[
                                  ColorFrame(color=CIE(x=0.70, y=0.25), 
                                             light=lights[0]),
                                  ColorFrame(color=CIE(x=0.65, y=0.35), 
                                             light=lights[1]),
                                  ColorFrame(color=CIE(x=0.55, y=0.40), 
                                             light=lights[2]),
                                  ColorFrame(color=CIE(x=0.50, y=0.45), 
                                             light=lights[3]),
                                  ColorFrame(color=CIE(x=0.70, y=0.25), 
                                             light=lights[1]),
                                  ColorFrame(color=CIE(x=0.65, y=0.35), 
                                             light=lights[2]),
                                  ColorFrame(color=CIE(x=0.55, y=0.40), 
                                             light=lights[3]),
                                  ColorFrame(color=CIE(x=0.50, y=0.45), 
                                             light=lights[0]),
                                  ColorFrame(color=CIE(x=0.70, y=0.25), 
                                             light=lights[2]),
                                  ColorFrame(color=CIE(x=0.65, y=0.35), 
                                             light=lights[3]),
                                  ColorFrame(color=CIE(x=0.55, y=0.40), 
                                             light=lights[0]),
                                  ColorFrame(color=CIE(x=0.50, y=0.45), 
                                             light=lights[1]),
                                  ColorFrame(color=CIE(x=0.70, y=0.25), 
                                             light=lights[3]),
                                  ColorFrame(color=CIE(x=0.65, y=0.35), 
                                             light=lights[0]),
                                  ColorFrame(color=CIE(x=0.55, y=0.40), 
                                             light=lights[1]),
                                  ColorFrame(color=CIE(x=0.50, y=0.45), 
                                             light=lights[2])
                              ])

def change_light(id: int,
                 x: float, 
                 y: float,
                 is_on: bool = True, 
                 ip: str = IP, 
                 key: str = KEY):
    payload = {
        "on": is_on,
        "xy": [x, y]
    }
    request = requests.put(f"http://{ip}/api/{key}/lights/{id}/state", 
                           json=payload)
    log.info(request.content)

def cycle_colors(profile):
    counter = 0
    
    while True:
        change_light(profile.frames[counter].light.id,
                     x=profile.frames[counter].color.x,
                     y=profile.frames[counter].color.y,
                     ip=IP,
                     key=KEY)
        counter += 1

        if counter == len(profile.frames):
            counter = 0

        time.sleep(profile.rate_s)

if __name__ == '__main__':
    cycle_colors(fire_profile)
    