from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="D:\Selenium_Drivers\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="D:\Selenium_Drivers\geckodriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
Parentmousehover = driver.find_element_by_css_selector("#mousehover")
action.move_to_element(Parentmousehover).perform()
Childmousehover = driver.find_element_by_link_text("Reload")
action.move_to_element(Childmousehover).click().perform()

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action.double_click(driver.find_element_by_id("double-click")).perform()