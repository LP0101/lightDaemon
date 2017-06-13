import daemon
import time
import math
from phue import Bridge

b = Bridge('192.168.1.217')
#Sensor pollers
def sPoll():
    return b.get_sensor()
def sKitchen(s):
    return s['13']['state']['presence']
def sHall(s):
    return s['21']['state']['presence']

#Light pollers
def lPoll():
    return b.get_light()
def lKitchen(l):
    return l['6']['state']
def lHall(l):
    return l['4']['state']
def lRoom(l):
    return l['1']['state']

#Light groups
kitchen = [6, 7]
hall = [4, 5]

#Light Setters
def light_trigger(room, bri, xy):
    b.set_light(room, {'on': True, 'bri': bri, 'xy': xy, 'transitiontime': 15})
def light_dim(room, bri):
    newBri = math.floor(bri/2)
    b.set_light(room, {'bri': newBri, 'transitiontime': 15})
def light_off(room):
    b.set_light(room, {'on': False, 'transitiontime': 15})


def monitor():
    hTimer = 0
    kTimer = 0
    reachable = True
    while(reachable):
        s = sPoll()
        sKitchen = sKitchen(s)
        sHall = sHall(s)
        time.sleep(1)

def run():
    with daemon.DaemonContext():
        monitor()

if __name__ == "__main__":
    run()
