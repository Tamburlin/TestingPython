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

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR, ".nav-link[href*='shop']").click()
cards = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for card in cards:
    cardName = card.find_element(By.XPATH, "div/h4/a").text
    if cardName == "Blackberry":
