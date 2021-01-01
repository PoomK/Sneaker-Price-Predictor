#Importing libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

SpecialNamesArr = ['Yeezy Boost 350 V2', 'Yeezy Boost 380', 'Yeezy Boost 700', 'Yeezy 500', 'Yeezy 700 V3', 'Yeezy QNTM', 'Ultra Boost', 'Jordan 1 Retro High', 'Jordan 1 Mid', 'Jordan 1 Low', 'Jordan 3 Retro', 'Jordan 4 Retro', 'Jordan 5 Retro', 'Jordan 6 Retro', 'Jordan 11 Retro', 'Nike Air Max 90', 'Nike Air Max 95', 'Nike Dunk High', 'Nike Dunk Low', 'Nike SB Dunk Low', 'Nike SB Dunk High', 'Nike LD Waffle Sacai', 'Nike Blazer Mid', 'Nike Air Force 1 Low', 'Fear Of God']

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

#Path to Chrome Driver for windows
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#Open site
driver.get("https://stockx.com/sneakers")

#Click on the annoying pop-up
driver.implicitly_wait(10)
PopUpQuitButton = driver.find_element_by_xpath("//img[@src='//stockx-assets.imgix.net/AllInAsk/close (1).svg?auto=compress,format']").click()

SneakerNameArr = []

#For loop to loop over n amount of pairs and extract sneaker name and append to sneakernamearr array
for i in range(5):

    #Click on the i + 1 sneaker
    xpathstr = "//div[@class='tile browse-tile updated']["+str(i+1)+"]"
    SneakerSelect = driver.find_element_by_xpath(xpathstr).click()

    #Get the sneaker name append to array
    SneakerName = driver.find_element_by_xpath("//h1[@data-testid='product-name']").text
    SneakerNameArr.append(SneakerName)

    #Return to initial page and refresh
    driver.back()
    driver.refresh()

#Printing array
print(SneakerNameArr)

#Create special name array for each sneaker
for i in range(len(SneakerNameArr)):
    SpecialNameResultArr = splitSpecial(SneakerNameArr[i])
    print(SpecialNameResultArr)