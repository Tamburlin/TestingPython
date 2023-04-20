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
        card.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary'").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

alertText = driver.find_element(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible").text
assert "Success! Thank you" in alertText

