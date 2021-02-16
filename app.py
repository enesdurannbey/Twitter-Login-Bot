#importing modules
from selenium import webdriver
import time

#input username & password
username = input("Enter Your Username or Email for twitter: ")
password = input("Enter Your Password for twitter: ")

#login with browser = webdriver.Firefox()
try:
    browser = webdriver.Firefox()
    browser.get("https://twitter.com/")
    time.sleep(3)
    login_button_xpath = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div")
    login_button_xpath.click()
    time.sleep(3)
    username_input_name = browser.find_element_by_name("session[username_or_email]")
    password_input_name = browser.find_element_by_name("session[password]")
    username_input_name.send_keys(username)
    password_input_name.send_keys(password)
    login_button = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span")
    login_button.click()
#error printing
except Exception as e:
    print(" Error  \n ",e)
