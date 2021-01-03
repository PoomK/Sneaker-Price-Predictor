import csv

YzyBredArr = ["adidas", "Yeezy Boost 350 V2", "Black", "Red", "(2017/2020)"]
Jordan1MochaArr = ["Air", "Jordan 1 Retro High", "Dark", "Mocha"]

def GetSneakerNameArray():

    with open("SneakerNameArr.csv", mode="r") as f:
        reader = csv.reader(f)
        row1 = next(reader)

    return row1

def GetNumpyArray(SpecificNameArr):

    #Returns an array of sneaker names from numpysneakernames.txt in specific order
    SneakerNamesArr = []

    with open("NumpySneakerNames.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            SneakerName = line.strip("\n")
            SneakerNamesArr.append(SneakerName)

    #Sneaker name arr for testing
    TrueCount = 0 #Counter
    NumpyArr = [] #Numpy array for sneaker

    #For loop to check if the value is true in sneaker name arr, returns 1 if true and 0 if false
    for i in range(len(SneakerNamesArr)):
        if SpecificNameArr[TrueCount] == SneakerNamesArr[i]:
            NumpyArr.append(1)
            if TrueCount != len(SpecificNameArr)-1:
                TrueCount = TrueCount + 1
        else:
            NumpyArr.append(0)

    return NumpyArr

#Calling array to test
#print(GetSneakerNameArray())
#This allows to get numpy array from calling sneaker array
print(GetNumpyArray(GetSneakerNameArray()))