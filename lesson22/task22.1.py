from selenium import webdriver
import os

driver = webdriver.Chrome(service_log_path=os.devnull)
driver.set_window_position(0, 0) #местоположение окна браузера на экране
driver.implicitly_wait(10) #время ожидания загрузки страницы

driver.get('https://www.google.com') #гет запрос к сайту
driver.quit() #завершить работу браузера
os.system("cls") #очищает консоль после отработки программы