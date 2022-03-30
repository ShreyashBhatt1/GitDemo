import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="D:\Selenium_Drivers\chromedriver.exe")
list1 =[]
list2 =[]
#driver = webdriver.Firefox(executable_path="D:\Selenium_Drivers\geckodriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_xpath("//input[@type='search']").send_keys("ber")
time.sleep(2)

count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
buttons =  driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in buttons:
    button.click()


productName = driver.find_elements_by_css_selector("h4[class='product-name']")
for v in productName:
    list1.append(v.text)

driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//div[@class='action-block']/button").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
Prodcts2ndPage = driver.find_elements_by_css_selector("p[class='product-name']")
for j in Prodcts2ndPage:
    list2.append(j.text)

assert list1 == list2

driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
promotext = driver.find_element_by_class_name("promoInfo").text

assert promotext == "Code applied ..!"
