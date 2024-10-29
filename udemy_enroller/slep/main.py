from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

FB_EMAIL = "tablet"
FB_PASSWORD = "Jyt=og"

driver = webdriver.Chrome()

driver.get("https://192.168.1.103:6150/?onepasswdfill=E393059F71954B619ED7E87023B37F10&onepasswdvault=FFDAE69715284BD8AC3CE978276A0485#/signin")


sleep(2)

#Login and hit enter
email = driver.find_element(By.XPATH, value='//*[@id="dsm-user-fieldset"]/div/div/div[1]/input')


password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)







#Allow location
allow_location_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

#Disallow notifications
notifications_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

#Allow cookies
cookies = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()





https://gist.github.com/TheMuellenator/dea97ee173821bd79184d281f41d79c3
