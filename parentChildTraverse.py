from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s=Service("C:\Selenium_webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://login.salesforce.com/")
print(driver.find_element(By.XPATH, "//form[@name='login']/div[1]/label").text)
print(driver.find_element(By.CSS_SELECTOR, "form[name='login'] label:nth-child(3)").text)
