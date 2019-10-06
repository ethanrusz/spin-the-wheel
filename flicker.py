from qhue import Bridge
import time
import random
import sys

bridge_ip = "<hue_ip_address>"
username = "<username>"
lights = [light_id_1, light_id_2]

def flicker(bridge, elapsed_time, lights_list = [], transition = 10):
    start_time= time.time()
    while (time.time() - start_time < elapsed_time):
        for light in lights_list:
            bridge.lights[light].state(bri=random.randint(50,130),on=True)
        time.sleep(random.uniform(0,0.5))
        for light in lights_list:
            bridge.lights[light].state(transitiontime=random.randint(0, transition), on=False)
        time.sleep(random.uniform(0,0.5))

b = Bridge(bridge_ip_address, username)
flicker(b, float(sys.argv[1]), lights, transition = 1)
for light in light_list:
    b.lights[light].state(bri=255,on=True)
