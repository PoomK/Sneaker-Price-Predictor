#Virtual environment: env
from selenium import webdriver
from datetime import datetime

#Path to Chrome Driver for mac
#PATH = "/applications/chromedriver"
#Path to Chrome Driver for windows
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#Open site
driver.get("https://stockx.com/sneakers")

#Click on the annoying pop-up
driver.implicitly_wait(10)
PopUpQuitButton = driver.find_element_by_xpath("//img[@src='//stockx-assets.imgix.net/AllInAsk/close (1).svg?auto=compress,format']").click()

#Click on the first sneaker
SneakerSelect = driver.find_element_by_xpath("//div[@class='tile browse-tile updated'][1]").click()

#Get the release date and its timestamp
ReleaseDateStr = driver.find_element_by_xpath("//span[@data-testid='product-detail-release date']").text
print(ReleaseDateStr)
RDDateTimeObj = datetime.strptime(ReleaseDateStr, "%d/%m/%Y")
print(RDDateTimeObj)
RDTTimeStamp = RDDateTimeObj.timestamp()
print(RDTTimeStamp)