SneakerSpecNameArr = []

with open("SneakerSpecialNames.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        SpecialName = line.strip("\n")
        SneakerSpecNameArr.append(SpecialName)

print(SneakerSpecNameArr)