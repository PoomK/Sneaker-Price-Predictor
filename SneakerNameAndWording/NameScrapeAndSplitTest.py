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

#Click on the first sneaker
SneakerSelect = driver.find_element_by_xpath("//div[@class='tile css-1bonzt1 e1yt6rrx0'][1]").click()

#Get the sneaker name and store words into array
SneakerName1 = driver.find_element_by_xpath("//h1[@data-testid='product-name']").text
print(SneakerName1)
SneakerNameWordsArr = SneakerName1.split(" ")
print(SneakerNameWordsArr)