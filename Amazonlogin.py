import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\Selenium_webdrivers\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.amazon.com/")
action = ActionChains(driver)
SignInMousehover = driver.find_element_by_css_selector("#nav-link-accountList")
action.move_to_element(SignInMousehover).perform()
ChildSignIn = driver.find_element_by_xpath("//div[@id='nav-flyout-ya-signin']/a/span")
action.move_to_element(ChildSignIn).click().perform()
driver.find_element_by_name("email").send_keys("bhatt.shrey96@gmail.com")
driver.find_element_by_xpath("//input[@type='submit']").click()
driver.find_element_by_name("password").send_keys("05812514035")
driver.find_element_by_id("signInSubmit").click()
#time.sleep(10)
driver.find_element_by_css_selector("#twotabsearchtextbox").send_keys("Samsung")
driver.find_element_by_css_selector("#nav-search-submit-button").click()
driver.find_element_by_link_text("Samsung Galaxy M12 (Blue,6GB RAM, 128GB Storage) 6 Months Free Screen Replacement "
                                 "for Prime").click()
childwindow = driver.window_handles[1]
driver.switch_to.window(childwindow)
#ss = driver.find_element_by_xpath("//h2[text()='Buy it with']").text
#print (ss)
driver.find_element_by_css_selector("#buy-now-button").click()

driver.find_element_by_xpath("//div[@class='a-box-inner']/fieldset[1]/div[2]/span/div").click()
driver.find_element_by_xpath("//input[@aria-labelledby='orderSummaryPrimaryActionBtn-announce']").click()

print("Hi I am adding new line of code here1")
print("Hi I am adding new line of code here2")
print("Hi I am adding new line of code here3")
