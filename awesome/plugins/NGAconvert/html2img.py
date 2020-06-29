import sys
import time
import os
from os import path

from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait


def html2png(tid):
    # print('into html2png')

    url = 'file:///' + path.join(path.dirname(__file__), str(tid), 'cvt.html')
    # "file:///D:/source/ngapost2md/22143850/cvt.html"
    save_fn = path.join(path.dirname(__file__), str(tid), 'cvt.png')

    option = Options()
    option.add_argument('--headless')
    option.add_argument('--disable-gpu')
    option.add_argument("--window-size=800,600")
    option.add_argument("--hide-scrollbars")

    driver = Firefox(executable_path='geckodriver', firefox_options=option)
    # print(url)
    driver.get(url)
    # print(driver.title)

    scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
    scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    driver.set_window_size(scroll_width, scroll_height)
    # try:
    driver.save_screenshot(save_fn)
    # except:
    #     print("ERROR")
    driver.quit()
    time.sleep(5)
    os.system("taskkill /F /IM firefox.exe")
    # os.system("rd %s /s /q" % path.join(path.dirname(__file__), str(tid)))


if __name__ == '__main__':
    html2png(123456)
