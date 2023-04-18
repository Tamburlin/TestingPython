from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option('detach', True)
service_obj = Service("C:\selenium-drivers\chrome\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

action = ActionChains(driver)
# action.click_and_hold(driver.find_element(By.ID, "")) <- lost of useful methods in action.
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()  # with action. we need perform() at the end
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()

