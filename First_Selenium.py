from selenium import webdriver
from selenium.webdriver.chrome.service import Service
op = webdriver.ChromeOptions()

driver = webdriver.Chrome(executable_path="C:\Selenium_webdrivers\chromedriver.exe", options=op)
#driver = webdriver.Firefox(executable_path="D:\Selenium_Drivers\geckodriver.exe")
#driver = webdriver.Ie(executable_path="D:\Selenium_Drivers\IEDriverServer.exe")
driver.maximize_window()
driver.get("https://www.google.com/")

print (driver.title)
print (driver.current_url)

driver.get("https://w3schools.com")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()