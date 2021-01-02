with open("TableInfo.txt","r") as f:
    lines =f.readlines()
    for line in lines:
        if "$" in line:
            LineList = line.split("$")
            print(LineList[1].strip())
