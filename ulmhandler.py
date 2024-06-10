# load level data

from fhandler import conRead, log

config = conRead("startup.con")

def ULMparse(file):
    if file.endswith(".ulm"):
        rlm = open(file, "r")
        dat = rlm.readlines()
        
        info = []
        vrts = []
        lnes = []
        sdes = []
        scts = []
        scrs = []
        print(dat)
        for i in dat:
            idx = dat.index(i)
            print(idx)
            if idx == 0 and dat[0] != "-- ULevel Map --\n":       # Check to see if the header is correct
                log("Failed to load level. Error code TZ-1 (Incorrect or missing header)")
                raise TypeError("Err TZ-1 (Incorrect or missing header)")
            if idx in range(1,3):
                tdat = dat[idx].split()
                info.append(tdat[1])
            if idx == 3:
                info.append(dat[3].rstrip("\n"))
            
        
        
        
    else:
        log("Failed to load level. Error code TZ-0 (Incorrect file type)")
        raise TypeError("Err TZ-0 (Incorrect file type)")
    
    lvldat = [info, vrts, lnes, sdes, scts, scrs]
    
    return lvldat

ULMparse("levels/tt_default.ulm")