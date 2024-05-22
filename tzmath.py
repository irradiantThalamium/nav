# math stuff

import math

def hypoCalc(sda,sdb): # a^2 + b^2 = c^2, so invert this
    sdc = math.sqrt((sda**2)+(sdb**2)) # i am a motherfucking idiot lmaoooo
    return sdc

def degToRad(inp):
    otp = (inp/180)*3.14
    return otp

def radToDeg(inp):
    otp = round((inp/3.14)*180)
    return otp