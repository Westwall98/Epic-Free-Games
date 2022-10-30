from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import requests
import os
from time import sleep

chromedriver = ChromeDriverManager().install()
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options,service=Service(chromedriver))

def log_in():
    driver.get('https://store.epicgames.com/login')
    sleep(5)
    driver.find_element(By.XPATH,"//div[@id=\"login-with-epic\"]").click()
    sleep(10)
    driver.find_element(By.XPATH,"//input[@type=\"email\"]").send_keys('ACCOUNT')
    sleep(10)
    driver.find_element(By.XPATH,"//input[@type=\"password\"]").send_keys('PASSWORD')
    sleep(10)
    driver.find_element(By.XPATH,"//button[@id=\"sign-in\"]").click()
    sleep(20)

def find():
    driver.get('https://store.epicgames.com/zh-CN/')

    free = driver.find_elements(By.CSS_SELECTOR,"div div div div span div div section div div div div a")

    global free1
    global free2

    free1 = free[0].get_attribute("href")
    free2 = free[1].get_attribute("href")

def collect():

    driver.get(free1)

    statis = driver.find_element(By.CSS_SELECTOR,"aside div div div div button span span").text

    if statis == "已在库中":
        print(statis)
    else:
        driver.find_element(By.CSS_SELECTOR,"aside div div div div button").click()

    sleep(10)

    driver.get(free2)

    statis = driver.find_element(By.CSS_SELECTOR,"aside div div div div button span span").text

    if statis == "已在库中":
        print(statis)
    else:
        driver.find_element(By.CSS_SELECTOR,"aside div div div div button").click()

log_in()
find()
collect()
