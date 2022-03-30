from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="D:\Selenium_Drivers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_xpath("//input[@name='name']").send_keys("Shreyash")
driver.find_element_by_xpath("//input[@name='email']").send_keys("bhatt.shrey96@gmail.com")
#driver.find_element_by_css_selector("input[id='exampleInputPassword1']").send_keys("XYZZZZZZZZ")
driver.find_element_by_xpath("//input[@id='exampleCheck1']").click()
driver.find_element_by_xpath("//input[@type='submit']").click()

dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
#dropdown.select_by_visible_text("Female")
dropdown.select_by_index(1)




#driver.find_elements_by_class_name("form-check-input").click()
#driver.find_element_by_name("name").send_keys("Shreyash")
#driver.find_element_by_name("email").send_keys("Shreyash.bhatt@gmail.com")
#driver.find_element_by_id("exampleInputPassword1").send_keys("12345678")
# driver.find_element_by_id("exampleChec356k1").click()
# driver.find_element_by_id("exampleFormControlSelect1").click("Female")
# driver.find_element_by_xpath("//input[@type='c']")
#driver.find_element_by_css_selector("input[name='name']").send_keys("AAA")
#print (driver.find_element_by_class_name("alert-success").text)
message = driver.find_element_by_class_name("alert-success").text
assert "success" in message
#//*[contains(@class,'alert-success')]   xpath with regular expression
#[class*='alert-success'] CSS with regular expression