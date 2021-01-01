#Returns an array of special sneaker names
SpecialNamesArr = []

with open("SneakerSpecialNames.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        SpecialName = line.strip("\n")
        SpecialNamesArr.append(SpecialName)

print(SpecialNamesArr)