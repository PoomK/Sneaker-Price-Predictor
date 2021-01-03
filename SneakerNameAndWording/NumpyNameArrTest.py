#Returns an array of sneaker names from numpysneakernames.txt in specific order
SneakerNamesArr = []

with open("NumpySneakerNames.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        SneakerName = line.strip("\n")
        SneakerNamesArr.append(SneakerName)

print(SneakerNamesArr)

#Sneaker name arr for testing
YzyBredArr = ["adidas", "Yeezy Boost 350 V2", "Black", "Red", "(2017/2020)"]
Jordan1MochaArr = ["Air", "Jordan 1 Retro High", "Dark", "Mocha"]
TrueCount = 0 #Counter
NumpyArr = [] #Numpy array for sneaker

for i in range(len(SneakerNamesArr)):
    if Jordan1MochaArr[TrueCount] == SneakerNamesArr[i]:
        NumpyArr.append(1)
        if TrueCount == len(Jordan1MochaArr)-1:
            TrueCount = TrueCount
        else:
            TrueCount = TrueCount + 1
    else:
        NumpyArr.append(0)

print(NumpyArr)