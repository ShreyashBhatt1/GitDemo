import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Selenium_webdrivers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements_by_css_selector("li[class ='ui-menu-item'] a")
print (len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break

print (driver.find_element_by_id("autosuggest").text) # It will not print the value, because when the page load selenium stores the dom and after that we update the value so that selenium do not have idea about that updation until the page get loads
assert driver.find_element_by_id("autosuggest").get_attribute('value') == "India"