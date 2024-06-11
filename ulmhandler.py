# load level data

from fhandler import conRead, log, findPath

config = conRead("startup.con")

def ULMparse(file):
    if file.endswith(".ulm"):
        if findPath(file, "levels/") == True:
            log("Failed to load level. Error code TZ-4 (File not found)")
            raise TypeError("Err TZ-4 (File not found)")
        lpath = findPath(file, "levels/").replace("\\", "/")
        rlm = open(lpath, "r")
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
            dat[idx] = dat[idx].rstrip("\n")
            print(idx)
            if idx == 0 and dat[0] != "-- ULevel Map --":       # Check to see if the header is correct
                log("Failed to load level. Error code TZ-1 (Incorrect or missing header)")
                raise TypeError("Err TZ-1 (Incorrect or missing header)")
            if idx == 1:
                tdat = dat[idx].lstrip("Author: ")
                info.append(tdat)
            if idx == 2:
                tdat = dat[idx].lstrip("MapName: ")
                info.append(tdat)
            if idx == 3:
                info.append(dat[3])
            
        
        
        
    else:
        log("Failed to load level. Error code TZ-0 (Incorrect file type)")
        raise TypeError("Err TZ-0 (Incorrect file type)")
    
    lvldat = [info, vrts, lnes, sdes, scts, scrs]
    
    print(lvldat)
    
    return lvldat

ULMparse("tt_default.ulm")