#debug only, delete this file before release
#or keep it in for the funny ;3

import random

def genRand():
    ugh = open("random.rnd", "w")
    this = []
    while len(this) < 256:
        j = random.randint(0,256)
        if j not in this:
            this.append(j)
    print(this)
    print(len(this))
    ugh.write(str(this))
    ugh.close()