from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

FB_EMAIL = "tablet"
FB_PASSWORD = "Jyt=og"

driver = webdriver.Chrome()

driver.get("https://192.168.1.103:6150/?onepasswdfill=E393059F71954B619ED7E87023B37F10&onepasswdvault=FFDAE69715284BD8AC3CE978276A0485#/signin")


sleep(5)

#Login and hit enter
email = driver.find_element(By.XPATH, value='//*[@id="dsm-user-fieldset"]/div/div/div[1]/input')
login_button = driver.find_element(By.XPATH, value='//*[@id="sds-login-vue-inst"]/div/span/div/div[2]/div[2]/div/div[3]/div[2]/div/div[2]/div[3]/div[1]')
login_button.click()


sleep(10)











# https://gist.github.com/TheMuellenator/dea97ee173821bd79184d281f41d79c3
