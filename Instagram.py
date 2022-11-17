from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser=webdriver.Firefox()
browser.get("https://www.instagram.com/")
time.sleep(2)

username=browser.find_element(By.NAME,"username")
password=browser.find_element(By.NAME,"password")

username.send_keys("--Your Username--")
password.send_keys("-Your Password--")

login=browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div")
time.sleep(5)
login.click()





