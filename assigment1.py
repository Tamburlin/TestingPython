from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

options = Options()
options.add_experimental_option('detach', True)
service_obj = Service("C:\selenium-drivers\chrome\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()
windowsOpen = driver.window_handles

driver.switch_to.window(windowsOpen[1])
textp = driver.find_element(By.CSS_SELECTOR, ".im-para.red").text
# Please email us at mentor@rahulshettyacademy.com with below template to receive response
mail = textp.split("at")[1].strip().split(" ")[0]
driver.close()

driver.switch_to.window(windowsOpen[0])
driver.find_element(By.CSS_SELECTOR, "#username").send_keys(mail)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
message = driver.find_element(By.CSS_SELECTOR, ".alert-danger").text
print(message)
