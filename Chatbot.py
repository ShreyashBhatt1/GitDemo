import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\Selenium_webdrivers\chromedriver.exe")
driver.get("https://teams.microsoft.com/_?lm=deeplink&lmsrc=NeutralHomePageWeb&cmpid=WebSignIn&culture=en-in&country=in#/conversations/19:4e8114ae-91e3-442f-8a09-594f04d7840f_efbedd3f-a4cc-41e8-b973-d5f5457d01be@unq.gbl.spaces?ctx=chat")
driver.implicitly_wait(70)
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("shreyash.bhatt@celebaltech.com")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Qwerty@291296")
time.sleep(5)
driver.find_element(By.XPATH, "//input[@type='submit']").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
driver.find_element(By.XPATH, "//div[text()='Text +XX XXXXXXXX81‎']").click()

driver.find_element(By.XPATH, "//input[@name='otc']").send_keys("")
time.sleep(20)
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(10)
driver.find_element(By.XPATH, "//input[@type='submit']").click()
driver.find_element(By.ID, "CancelLinkButton").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(50)
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[2]").click()
driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
driver.find_element(By.XPATH, "//body[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/p[1]").send_keys("hi")
driver.find_element(By.XPATH, "//button[@name='send']").click()
driver.find_element(By.XPATH, "//body[@class='exp-density-view initialized hide-messages power-bar-visible loadingscreendone']/div[@id='outer-shell']/div[@id='wrapper']/div[@id='page-content-wrapper']/div[@class='flex-fill']/div[@class='ts-middle-pane flex-fill']/messages-header[@class='messages-header flex-fill']/div[@class='ts-tab-content flex-fill']/div[@class='ts-embedded-container flex-fill']/message-pane[@class='content-child flex-fill']/div[@class='message-pane flex-fill with-chat-bubbles new-typing-indicator']/div[@class='ts-middle-messages-container flex-fill']/div[@class='ts-middle-messages-body flex-fill']/div[@class='ts-message-content flex-fill']/message-list[@class='flex-fill message-list-common smooth-highlight chat-style']/div[@class='flex-fill']/virtual-repeat[@class='ts-message-list no-animation simple-scrollbar not-at-top overflow-visible']/div[@class='list-wrap list-wrap-v3 ts-message-list-container']/div[@class='item-wrap ts-message-list-item']/div[@id='t1646976893931']/thread[@class='ts-expanded-message']/div[@class='ts-message acc-message-list-focusable']/div[@class='conversation-common conversation-start conversation-not-collapsed']/thread-body[@ng-if='!msgCtrl.thread.firstMessage.isDeleted']/div[@id='m1646976893931']/div[@class='ts-message-thread-body']/div[@id='messageBody']/div[@class='ts-card-thread-body']/div[@class='message-body-container padded-content']/div[@oc-lazy-load='adaptive-card']/adaptive-card[@card='ctrl.cards[0]']/div[@class='ts-adaptive-card card-acc-border adaptive-card-responsive']/div[@style='position:relative;']/div[@class='card-border-placeholder card-border']/div[@class='card-body']/div[@class='ac-container ac-adaptiveCard']/div[@class='ac-columnSet']/div[1]/div[1]/div[1]/div[1]/button[1]")
#time.sleep(10)
#driver.find_element(By.XPATH, "//input[@name='title']").send_keys("Hello testing")
#driver.find_element(By.XPATH, "//input[@name='description']").send_keys("Hello Description")

