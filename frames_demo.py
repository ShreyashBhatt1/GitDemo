from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\Selenium_webdrivers\chromedriver.exe")

driver = webdriver.Chrome(service=s)
driver.get("https://the-internet.herokuapp.com/")
driver.find_element(By.LINK_TEXT, "Frames").click()
driver.find_element(By.LINK_TEXT, "iFrame").click()
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.CSS_SELECTOR, "#tinymce").clear()
driver.find_element(By.CSS_SELECTOR, "#tinymce").send_keys("Hi there, I am inside Frame...........")
driver.switch_to.default_content()
headline = driver.find_element(By.TAG_NAME, "h3").text
assert headline == "An iFrame containing the TinyMCE WYSIWYG Editor"
