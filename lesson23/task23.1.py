from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


ser = Service(".\chromedrive.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)


driver.get('https://skysmart.ru/programmirovanie-dlya-detej/python')
div = driver.find_element(by=By.CLASS_NAME, value='blocks-wrapper')
span = div.find_elements(by=By.TAG_NAME, value='span')


a, b = span[0].text, span[1].text
print(a)
print(b)

