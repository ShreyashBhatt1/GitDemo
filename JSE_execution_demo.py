from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\Selenium_Drivers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Hello")
print (driver.execute_script('return document.getElementsByName("name")[0].value'))
shopbutton = driver.find_element_by_link_text("Shop")
driver.execute_script('arguments[0].click();', shopbutton)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

