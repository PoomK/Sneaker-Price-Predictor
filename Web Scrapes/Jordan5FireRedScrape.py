from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
 
driver.get("https://www.nike.com/th/launch/t/womens-air-zoom-spiridon-cage-2-university-blue")

productTitle = driver.find_element_by_xpath("//h1[@class='test-subtitle ncss-brand text-color-grey u-uppercase mb-1-sm mb0-md fs14-sm fs16-md']").text
testTitle = driver.find_element_by_xpath("//h5[@class='test-title ncss-brand pb1-sm u-uppercase mb-1-sm mb0-md fs30-sm fs40-md']").text
price = driver.find_element_by_xpath("//div[@class='ncss-brand pb6-sm fs14-sm fs16-md']").text
releaseDate = driver.find_element_by_xpath("//div[@class='available-date-component ncss-brand pb6-sm u-uppercase fs14-sm fs16-md']").text

if os.path.exists("NikeReleases.txt"):
    os.remove("NikeReleases.txt")
else:
    print("File has been created")

print(productTitle)
print(testTitle)
print(price)
print(releaseDate)

driver.close()