from selenium import webdriver

Chrome_Option = webdriver.ChromeOptions()
#Chrome_Option.add_argument("--start-maximized")
#Chrome_Option.add_argument("headless")
#Chrome_Option.add_argument("--ignore-certificate-errors")


driver = webdriver.Chrome(executable_path="D:\Selenium_Drivers\chromedriver.exe", options=Chrome_Option)
driver.get("https://mail.essindia.com/")
print (driver.title)