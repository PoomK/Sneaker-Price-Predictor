#Returns an array of sneaker names from numpysneakernames.txt in specific order
SneakerNamesArr = []

with open("NumpySneakerNames.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        SneakerName = line.strip("\n")
        SneakerNamesArr.append(SneakerName)

print(SneakerNamesArr)