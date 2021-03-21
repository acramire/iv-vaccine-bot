import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.ui import Select
import twitterBot 

import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

#PATH = "/Users/alejandroramirez/Desktop/chromeDriverSpot/chromedriver"
#driver = webdriver.Chrome(PATH)


driver.get("https://myturn.ca.gov")

time.sleep(1)

#First page, begin button
registerButton = driver.find_element_by_xpath("/html/body/div/div/main/div[1]/div/div[2]/div[3]/button")
registerButton.click()

#Following are check marks
ofAgeCheck = driver.find_element_by_xpath("/html/body/div/div/main/div/form/span[1]")
ofAgeCheck.click()

healthDataCheck  = driver.find_element_by_xpath("/html/body/div/div/main/div/form/span[2]")
healthDataCheck.click()

accuracyCheck = driver.find_element_by_xpath("/html/body/div/div/main/div/form/span[3]" )	
accuracyCheck.click()

privacyCheck = 	driver.find_element_by_xpath("/html/body/div/div/main/div/form/span[4]" )	
privacyCheck.click()


#Category Button
ageCategoryCheck = driver.find_element_by_xpath("/html/body/div/div/main/div/form/span[5]/div/fieldset/div[2]/label[4]/input")
ageCategoryCheck.click()

#Yes or no buttons
underlyingConditionsCheck = driver.find_element_by_xpath("/html/body/div/div/main/div/form/span[6]/div/fieldset/div[3]/label[1]/input")
underlyingConditionsCheck.click()

disabilityCheck = driver.find_element_by_xpath("/html/body/div/div/main/div/form/span[7]/div/fieldset/div[2]/label[2]/input")
disabilityCheck.click()

#Dropdowns
businessDropdown = Select( driver.find_element_by_xpath("/html/body/div/div/main/div/form/span[8]/div/select"))
businessDropdown.select_by_visible_text("Food and Agriculture")

countyDropdown = Select( driver.find_element_by_xpath("/html/body/div/div/main/div/form/span[9]/div/select"))
countyDropdown.select_by_visible_text("Imperial")

#continue button (onto next page)
continueButton = driver.find_element_by_xpath("/html/body/div/div/main/div/form/div/button[1]")
continueButton.click()

# =-=-=-=-=-=- NEXT PAGE (Page 2) -=-=-=-=-=-=
time.sleep(1) #wait to load

#enter zip code
zipcodeInput = driver.find_element_by_xpath("/html/body/div/div/main/div/div[3]/input")
zipcodeInput.send_keys("93277")
#driver.quit()

#Visalia: 93277

continue2Button = driver.find_element_by_xpath("/html/body/div/div/main/div/div[5]/button[1]")
continue2Button.click()

time.sleep(2)

i = 1

while True:
	try:
		time.sleep(1)
		buttonXpath = "//*[@id='root']/div/main/div[1]/div[2]/div[" + str(i) + "]/div[2]/button"
		driver.find_element_by_xpath(buttonXpath).click()
		
		try:
			time.sleep(1)
			test = driver.find_element_by_xpath("/html/body/div/div/main/div/div[2]/div[2]/div/div[2]/h3").text
			twitterBot.sendTweet(test)					 
		except NoSuchElementException:
			print("none available")

		time.sleep(1)
		#Click back
		driver.find_element_by_xpath("/html/body/div/div/main/div/div[3]/div/button[2]").click() 

		print(i)
		i = i + 1
	except NoSuchElementException:
		print("None available")
		break;


	

