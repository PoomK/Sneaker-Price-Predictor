#Virtual environment: env
from selenium import webdriver

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
SneakerSelect = driver.find_element_by_xpath("//div[@class='tile css-1bonzt1 e1yt6rrx0'][1]").click()

driver.find_element_by_xpath("//a[@data-testid='product-viewallsales']").click()

while True:
    try:
        load_more_button = driver.find_element_by_xpath("//button[@class='button button-block button-white']").click()
    except:
        break

table = driver.find_element_by_xpath("//table[@id='480']").text

with open ("Tableinfo.txt", "w") as f:
    f.write(table)