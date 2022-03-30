import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\Selenium_webdrivers\chromedriver.exe")
list = []
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.co.in/")
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//input[@class='gLFyf gsfi']").send_keys("Java")
list = driver.find_element(By.XPATH, "//ul/li[@class='sbct']")





