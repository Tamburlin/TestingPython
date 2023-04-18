import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option('detach', True)
service_obj = Service("C:\selenium-drivers\chrome\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.get("https://www.makemytrip.com/")
driver.find_element(By.ID, "fromCity").click()
driver.find_element(By.CSS_SELECTOR, "input[placeholder='From']").send_keys("del")
time.sleep(2)
cities = driver.find_elements(By.CSS_SELECTOR,"p[class*='blackText']")
print(len(cities))
for city in cities:
    if city.text =="Del Rio, United States":
        city.click()
        break


driver.find_element(By.XPATH, "//p[text()='Delhi, India']").click()



