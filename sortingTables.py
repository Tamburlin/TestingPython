from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

chromeoptions = webdriver.ChromeOptions()
chromeoptions.add_experimental_option('detach', True)
chromeoptions.add_argument("--start-maximized")
service_obj = Service("C:\selenium-drivers\chrome\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chromeoptions)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
sortedVeggies = []
for veggie in veggieWebElements:
    sortedVeggies.append(veggie.text)

sortedList = sortedVeggies.copy()
sortedVeggies.sort()
assert sortedList == sortedVeggies
