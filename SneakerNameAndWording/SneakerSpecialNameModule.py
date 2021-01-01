#Returns an array of special sneaker names
SpecialNamesArr = []

with open("SneakerSpecialNames.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        SpecialName = line.strip("\n")
        SpecialNamesArr.append(SpecialName)

def strip(s):
    return s.strip()

def splitSpecial(sneakerName):
    #iterate through specialNames
    for s in SpecialNamesArr:
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

#To get special name, special name array = splitSpecial(SneakerName)

print(splitSpecial("Nike Air Max 95 OG Neon (2020)"))