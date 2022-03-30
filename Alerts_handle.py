import time

from selenium import webdriver
validateText = "Option3"
driver = webdriver.Chrome(executable_path="D:\Selenium_Drivers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_css_selector("input[name='enter-name']").send_keys("Option3")
driver.find_element_by_css_selector("input[value='Confirm']").click()
alert1 = driver.switch_to.alert
time.sleep(5)
alert1.dismiss()

driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert

alert_text = alert.text
assert validateText in alert_text
time.sleep(2)
alert.accept()
