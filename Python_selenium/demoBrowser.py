#browser exposes an executable file
#Through Selenium test we need to invoke the executable file which will then invoke actual browser
#driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
#driver=webdriver.Firefox(executable_path="C:\\geckodriver.exe")
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option('detach', True)
service_obj = Service("C:\selenium-drivers\chrome\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")  #get method to hit url on  browser

print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()









