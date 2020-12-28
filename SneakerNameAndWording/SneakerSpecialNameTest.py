SpecialNameArr = ["Jordan 1 Retro High","adidas Yeezy Boost 350 V2","Jordan 1 Mid","Nike Air Force 1"]
yeezyBredName = "adidas Yeezy Boost 350 V2 Black Red (2017/2020)"

def strip(s):
    return s.strip()

def splitSpecial(sneakerName):
    for s in sneakerName:
        if s in sneakerName:
            nameArray = sneakerName.split(s)
            nameArray.insert(1, s)
            nameArray = list(map(strip, nameArray))
            return nameArray
        return sneakerName

a = splitSpecial(yeezyBredName)
print(a)