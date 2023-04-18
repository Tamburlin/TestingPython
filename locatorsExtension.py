from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option('detach', True)
service_obj = Service("C:\selenium-drivers\chrome\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.get("https://login.salesforce.com/")
driver.find_element(By.CSS_SELECTOR, "#username").send_keys("Rahul")
driver.find_element(By.CSS_SELECTOR, ".password").send_keys("shetty")
driver.find_element(By.CSS_SELECTOR, ".password").clear()
driver.find_element(By.LINK_TEXT, "Forgot Your Password?").click()
#//tagname[text()=’xxx’]
driver.find_element(By.XPATH, "//a[text()='Cancel']").click()
print(driver.find_element(By.XPATH, "//form[@name='login']/div[1]/label").text)
print(driver.find_element(By.CSS_SELECTOR, "form[name='login'] label:nth-child(3)").text)





