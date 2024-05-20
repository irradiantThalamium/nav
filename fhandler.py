# handles .con and .log files

def conRead(file):
    lfile = open(file, "r")
    cfgs = lfile.readlines()
    
    fncfg = 0
    
    for i in cfgs:
        x = x = i.split()
        if x[0] == "fullscreen" and int(x[1]) == 1:
            fncfg += -2147483648 # this alone is making me regret doing this in python
                                 # WHY ARE THERE NO UNSIGNED INTEGERS
                                 # fml
        elif x[0] == "autoscale" and int(x[1]) == 1:
            fncfg += 512
        elif x[0] == "bordered" and int(x[1]) == 0:
            fncfg += 32

    return fncfg
    
    