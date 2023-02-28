from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import chromedriver_autoinstaller
from time import sleep



chromedriver_autoinstaller.install()


option = webdriver.ChromeOptions()
option.add_argument("window-size=1280x768")
option.add_argument('headless')
option.add_argument('disable-gpu')
# option.add_argument('disable-infobars')



provinces = ["ระยอง", "กรุงเทพ", "จันทบุรี", "ฉะเชิงเทรา"]


driver = webdriver.Chrome(options=option)



url = "http://www.gooogle.com"

for p in provinces:
    driver.get(url)

    search = driver.find_element(By.NAME, 'q')

    search_text = "อุณหภูมิจังหวัด{}".format(p)
    search.send_keys(search_text)
    search.send_keys(Keys.ENTER)

    sleep(1)
    driver.save_screenshot('weather_{}.png'.format(p))



driver.close()
