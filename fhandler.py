# handles .con and .log files, and importing the random list

from datetime import datetime

def randInit():
    lst = open("def.rnd", "r")
    lst=lst.readlines()[0]
    fin = []
    for i in range(0,len(lst[1:-1].split(", "))):
        fin.append(int(lst[1:-1].split(", ")[i]))
    return fin
        

def conRead(file):
    lfile = open(file, "r")
    cfgs = lfile.readlines()
    
    fncfg=[0,False]
    
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
        elif x[0] == "logging" and int(x[1]) == 1:
            fncfg[1] = True

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
    
