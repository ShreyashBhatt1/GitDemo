from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\Selenium_webdrivers\chromedriver.exe")
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver)
action.double_click(driver.find_element_by_id("double-click")).perform()

alert = driver.switch_to.alert
assert alert.text == "You double clicked me!!!, You got to be kidding me"
alert.accept()
action.context_click(driver.find_element_by_id("double-click")).perform()
driver.close()