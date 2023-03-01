# loong-dimon@gmail.com
# 123456

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep

import wikipedia

keyword = ['honda', 'suzuki', 'mercedez benz', 'bmw']

driver = webdriver.Chrome()
url = "http://uncle-machine.com/login/"

driver.get(url)

# login page

username = 'loong-dimon@gmail.com'
password = '123456'

username_ele = driver.find_element(By.NAME, 'username')
username_ele.send_keys(username)

password_ele = driver.find_element(By.ID, 'password')
password_ele.send_keys(password)

button_path = "/html/body/div[2]/form/button"
submit_button = driver.find_element(By.XPATH, button_path)
submit_button.click()


url2 = 'http://uncle-machine.com/addproduct/'

for k in keyword:
    driver.get(url2)
    wiki_detail = wikipedia.summary(k)
    sleep(1)

    try:
        product_name = driver.find_element(By.ID, 'name')
        product_name.send_keys(k)

        product_price = driver.find_element(By.ID, 'price')
        product_price.send_keys('2000')

        product_detail = driver.find_element(By.ID, 'detail')
        product_detail.send_keys(wiki_detail)

        if k == 'suzuki':
            filepath = r"C:\Users\saich\Documents\RPA_course\durian.jpg"
            photo = driver.find_element(By.ID, "photo")
            photo.send_keys(filepath)
            sleep(2)
        

        b2_path = 'html/body/div[2]/form/button'
        product_button = driver.find_element(By.XPATH, b2_path)
        product_button.click()

        sleep(1)
    except:
        print('Keyword Error: ', k)





driver.close()
