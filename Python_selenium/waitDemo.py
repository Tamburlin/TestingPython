import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.add_experimental_option('detach', True)
service_obj = Service("C:\selenium-drivers\chrome\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)  # waiting for elements to add to list, list can be empty, so implicitly wait won't work, need sleep

# products = driver.find_elements(By.XPATH, "//h4[@class='product-name']")
# productsNames = []
# for product in products:
#    productsNames.append(product.text)

# print(productsNames)

expectedNames = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actualNames = driver.find_elements(By.XPATH, "//h4[@class='product-name']")
namesText: list[str] = []
for names in actualNames:
    namesText.append(names.text)

assert expectedNames == namesText

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0
for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

#  Sum validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
suma = 0
for price in prices:
    suma = suma + int(price.text)

print(suma)
assert suma == int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait = WebDriverWait(driver, 10)  # when you need to wait for specific element longer, increasing global wait is no good
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

assert int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text) > \
       float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
