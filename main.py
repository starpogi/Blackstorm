import requests
import logging
import time

from colors import CIE
from colors.animations import ColorAnimation

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

KEY = "ETKkOpw4AvR5nfIzLfNHCo0w1xFhjaL0NfxhFnQV"
IP = "192.168.1.66"


fire_profile = ColorAnimation(rate_s=0.2,
                              frames=[
                                  CIE(x=0.70, y=0.25),
                                  CIE(x=0.65, y=0.35),
                                  CIE(x=0.55, y=0.40),
                                  CIE(x=0.50, y=0.45)
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
        change_light(9,
                     x=profile.frames[counter].x,
                     y=profile.frames[counter].y,
                     ip=IP,
                     key=KEY)
        counter += 1

        if counter == len(profile.frames):
            counter = 0

        time.sleep(profile.rate_s)

if __name__ == '__main__':
    cycle_colors(fire_profile)
    