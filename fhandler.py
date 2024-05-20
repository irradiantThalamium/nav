# handles .con and .log files

from datetime import datetime

def conRead(file):
    lfile = open(file, "r")
    cfgs = lfile.readlines()
    
    fncfg=[0]
    
    for i in cfgs:
        x = x = i.split()
        if x[0] == "fullscreen" and int(x[1]) == 1:
            fncfg[0] += -2147483648 # this alone is making me regret doing this in python
                                 # WHY ARE THERE NO UNSIGNED INTEGERS
                                 # fml
        elif x[0] == "autoscale" and int(x[1]) == 1:
            fncfg[0] += 512
        elif x[0] == "bordered" and int(x[1]) == 0:
            fncfg[0] += 32

    return fncfg
    
now = datetime.now()

def startLog():
    logInit = now.strftime("%d-%m-%Y-%H%M%S")
    logfl = open("logs/"+logInit+".txt", "w")
    logfl.write(f"-- LOG START --\n- Time: {logInit} -\n")
    logfl.close()
    
def log(txt):
    logfl = open("logs/"+now.strftime("%d-%m-%Y-%H%M%S")+".txt", "a")
    logfl.write(f"--{txt}\n")
    logfl.close()
    print(txt)
    
def endLog():
    logFin = now.strftime("%d-%m-%Y-%H%M%S")
    logfl = open("logs/"+logFin+".txt", "a")
    logfl.write(f"-- LOG END --\n- Time: {logFin} -\n")
    logfl.close()
    
