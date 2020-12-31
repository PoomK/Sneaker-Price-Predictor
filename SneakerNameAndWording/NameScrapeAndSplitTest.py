#Importing libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

#Path to Chrome Driver for windows
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#Open site
driver.get("https://stockx.com/sneakers")

#Click on the annoying pop-up
driver.implicitly_wait(10)
PopUpQuitButton = driver.find_element_by_xpath("//img[@src='//stockx-assets.imgix.net/AllInAsk/close (1).svg?auto=compress,format']").click()

SneakerNameArr = []

'''SneakerSelect = driver.find_element_by_xpath("//div[@class='tile browse-tile updated'][2]").click()
SneakerName = driver.find_element_by_xpath("//h1[@data-testid='product-name']").text
print(SneakerName)'''

for i in range(2):

    #Click on the first sneaker
    xpathstr = "//div[@class='tile browse-tile updated']["+str(i+1)+"]"
    SneakerSelect = driver.find_element_by_xpath(xpathstr).click()

    #Get the sneaker name and store words into array
    SneakerName = driver.find_element_by_xpath("//h1[@data-testid='product-name']").text
    SneakerNameArr.append(SneakerName)

    driver.back()
    driver.refresh()

print(SneakerNameArr)