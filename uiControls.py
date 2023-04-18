from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option('detach', True)
service_obj = Service("C:\selenium-drivers\chrome\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()

radiobuttons = driver.find_elements(By.NAME, "radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()


assert driver.find_element(By.ID, "displayed-text").is_displayed()

driver.find_element(By.ID, "hide-textbox").click()

assert not driver.find_element(By.ID,"displayed-text").is_displayed()




