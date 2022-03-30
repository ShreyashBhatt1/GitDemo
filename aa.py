from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver_service = Service(executable_path="C:/Users/ssc/ChromeDriver/chromedriver.exe")
driver = webdriver.Chrome(Service=driver_service)
driver.get("https://www.google.co.in/")