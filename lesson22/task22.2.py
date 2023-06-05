from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.options import Options
import os

#
chrome_options = Options()
chrome_options.add_experimental_option("detach", True) #оставляет страницу браузера открытой
driver = webdriver.Chrome(chrome_options=chrome_options, service_log_path=os.devnull)
driver.set_window_position(0, 0)  # местоположение окна браузера на экране

#driver.implicitly_wait(10)  # время ожидания загрузки страницы

driver.get('https://klik-test.ru/schetchik-klikov')  # гет запрос к сайту

# driver.driver.find_elements(By.TAG_NAME, "button") #ищем все элементы по tegu
# driver.find_elements(By.ID, 'click-plus') #ищем все элементы по id
# driver.find_elements(By.CLASS_NAME, 'btn-left') #ищем все элементы по классу

# driver.driver.find_element(By.TAG_NAME, "button")[0] #ищем первый элемент по tegu
# driver.find_element(By.ID, 'click-plus') #ищем первый элемент по id
# driver.find_element(By.CLASS_NAME, 'btn-left') #ищем первый элемент по классу

a = driver.find_element(By.ID, 'click-plus')
for i in range(100):
    a.click()


# driver.quit() #завершить работу браузера
#os.system("cls")  # очищает консоль после отработки программы
