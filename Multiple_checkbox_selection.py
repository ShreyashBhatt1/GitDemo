
from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\Selenium_Drivers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#To select all checkboxes

checkboxes_list = driver.find_elements_by_xpath("//input[@type='checkbox']")
print (len(checkboxes_list))
#for checkbox in checkboxes_list:
    #checkbox.click()
    #assert checkbox.is_selected()

#To select sengle checkbox option

for checkbox in checkboxes_list:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()

radioButtons = driver.find_elements_by_xpath("//input[@type='radio']")
radioButtons[0].click()

assert driver.find_element_by_id("displayed-text").is_displayed()
driver.find_element_by_id("hide-textbox").click()
assert not driver.find_element_by_id("displayed-text").is_displayed()

driver.close()