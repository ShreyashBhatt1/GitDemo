import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\Selenium_Drivers\chromedriver.exe")
driver.implicitly_wait(10)
#driver = webdriver.Firefox(executable_path="D:\Selenium_Drivers\geckodriver.exe")

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_xpath("//input[@type='search']").send_keys("ber")
time.sleep(2)

count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
buttons =  driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in buttons:
    button.click()

driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//div[@class='action-block']/button").click()
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()
promotext = driver.find_element_by_class_name("promoInfo").text

assert promotext == "Code applied ..!"
