from datetime import datetime

def get_price():
    with open("Tableinfo.txt","r") as f:
        lines =f.readlines()
        for line in lines:
            if "$" in line:
                LineList = line.split("$")
                price = LineList[1].strip()

def extract_date(dateString):
    #Remove "Sunday,"
    dateString = ",".join(dateString.split(",")[1:]).strip()
    datetimeObj = datetime.strptime(dateString, "%B %d, %Y %I:%M %p")
    return datetimeObj

#Extract date tester
# dateString1 = "Sunday, November 12, 2017 10:03 AM "
# print(extract_date(dateString1))