import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="D:\Selenium_Drivers\chromedriver.exe")
list1 = []
list2 = []
# driver = webdriver.Firefox(executable_path="D:\Selenium_Drivers\geckodriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_xpath("//input[@type='search']").send_keys("ber")
time.sleep(2)

count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in buttons:
    list1.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()

driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//div[@class='action-block']/button").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
Prodcts2ndPage = driver.find_elements_by_css_selector("p[class='product-name']")
for prodName in Prodcts2ndPage:
    list2.append(prodName.text)

assert list1 == list2
totalamt = driver.find_element_by_css_selector(".discountAmt").text
print (totalamt)
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
discAmt = driver.find_element_by_css_selector(".discountAmt").text
print (discAmt)
assert float(discAmt) < int(totalamt)

promotext = driver.find_element_by_class_name("promoInfo").text

assert promotext == "Code applied ..!"


Amounts = driver.find_elements_by_xpath("//tr/td[5]/p")
sum = 0
for amount in Amounts:
    sum = sum  + int(amount.text)
print ("{} {}".format("Sum is ",sum))

totalA = int(driver.find_element_by_class_name("totAmt").text)
assert sum == totalA


