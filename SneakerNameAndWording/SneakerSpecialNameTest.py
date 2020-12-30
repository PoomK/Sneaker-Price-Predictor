specialNames = ["Jordan 1 Retro High","Yeezy Boost 350 V2","Jordan 1 Mid","Nike Air Force 1"]
yeezyBredName = "adidas Yeezy Boost 350 V2 Black Red (2017/2020)"

def strip(s):
    return s.strip()

def splitSpecial(sneakerName):
    #iterate through specialNames
    for s in specialNames:
        #check if special name is in sneaker name
        if s in sneakerName:
            nameArray = sneakerName.split(s)
            nameArray.insert(1, s)
            nameArray = list(map(strip, nameArray))

            #Check for space in 3rd element and split if there is space
            if "" in nameArray[2]:
                element2 = nameArray[2]
                del nameArray[2]
                newArr2 = element2.split()
                for i in range(len(newArr2)):
                    position2 = 2+i
                    value2 = newArr2[i]
                    nameArray.insert(position2,value2)

            #Check for space in 1st element and split if there is space
            if "" in nameArray[0]:
                element1 = nameArray[0]
                del nameArray[0]
                newArr1 = element1.split()
                for i in range(len(newArr1)):
                    position1 = i
                    value1 = newArr1[i]
                    nameArray.insert(position1,value1)

            return nameArray
    return sneakerName

a = splitSpecial(yeezyBredName)
print(a)