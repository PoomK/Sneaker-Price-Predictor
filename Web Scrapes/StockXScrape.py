#Load Libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

#Set up driver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#Get the website
driver.get('https://stockx.com/sneakers')

#Close the annoying pop-up
driver.find_element_by_xpath("//img[@class='WhereAreYouModal__CloseButton-sc-1qz03s6-7 eyPglK']").click()