from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

options = Options()
# options.add_experimental_option('detach', True) <- firefox does not close on its own
# firefox was installed in custom location, without line below selenium cant find it
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
service_obj = Service(executable_path=r"C:/selenium-drivers/firefox/geckodriver.exe")
driver = webdriver.Firefox(service=service_obj, options=options)
driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
windowsOpen = driver.window_handles


driver.switch_to.window(windowsOpen[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
