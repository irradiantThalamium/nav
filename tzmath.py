# math stuff

import math

pi = 3.14 # for fun editing later :3333

def hypoCalc(sda,sdb): # a^2 + b^2 = c^2, so invert this
    sdc = math.sqrt((sda**2)+(sdb**2)) # i am a motherfucking idiot lmaoooo
    return sdc

def magCalc(sda,sdb,sdc): # i fucking hate this
    sdd = math.sqrt((sda**2)+(sdb**2)+(sdc**2))
    return sdd

def degToRad(inp):
    otp = (inp/180)*pi
    return otp

def radToDeg(inp):
    otp = round((inp/pi)*180)
    return otp
