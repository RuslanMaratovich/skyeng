from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import random


def wait():
    wait_time = [1, 3, 5]
    result = random.choice(wait_time)
    return result


ser = Service(".\chromedrive.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get('https://skysmart.ru/programmirovanie-dlya-detej/python')


div = driver.find_element(by=By.CLASS_NAME, value='form')
time.sleep(wait())
inputs = div.find_elements(by=By.TAG_NAME, value='input')

name = 'Igor'
phone = '8 (919) 102-36-54'
email = 'test1@gmail.com'

time.sleep(wait())
inputs[0].send_keys(name)  # передает значение name в форму
time.sleep(wait())
inputs[1].send_keys(phone)  # передает phone значение name в форму
time.sleep(wait())
inputs[2].send_keys(email)  # передает email значение name в форму

time.sleep(random.randint(20, 30))

print('done')
