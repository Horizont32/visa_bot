# import time, os, re, json
# import telebot as tb
import time
from pypasser import reCaptchaV2, reCaptchaV3
import configparser


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# Importing config
config = configparser.ConfigParser()
config.read('cfg.ini')
URL = config.get('LoginData', 'url')
EMAIL = config.get('LoginData', 'email')
PASSWORD = config.get('LoginData', 'pwd')
driver = webdriver.Chrome()

driver.get(URL)
el = WebDriverWait(driver, 100).until(lambda p: p.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]'))
# Create an instance of webdriver and open the page has recaptcha v2
# ...
time.sleep(8)
email_form = driver.find_element(By.ID, 'mat-input-0').send_keys(EMAIL)
pass_form = driver.find_element(By.ID, 'mat-input-1').send_keys(PASSWORD)
# pass the driver to reCaptchaV2
# is_checked = reCaptchaV2(driver) # it returns bool
is_checked = reCaptchaV3(el.get_attribute('src'))
query = f"___grecaptcha_cfg.clients['0'].O.O.callback('{is_checked}');"
print(query)
driver.execute_script(query)
# is_checked = reCaptchaV3('https://www.recaptcha.net/recaptcha/api2/anchor?ar=1&k=6LfDUY8bAAAAAPU5MWGT_w0x5M-8RdzC29SClOfI&co=aHR0cHM6Ly92aXNhLnZmc2dsb2JhbC5jb206NDQz&hl=en&v=SglpK98hSCn2CroR0bKRSJl5&size=normal&cb=v3n9p9ydwh61')
print(is_checked)
driver.execute_script(f'document.getElementById("g-recaptcha-response").innerHTML="{is_checked}";')
driver.execute_script(f'document.getElementById("g-recaptcha-response-100000").innerHTML="{is_checked}";')
time.sleep(2)
driver.find_element(By.XPATH, '//form/button').click()
time.sleep(6)
start_app_btn = driver.find_element(By.XPATH, '//app-dashboard/section[1]/div/div[1]/div[@class="position-relative"]/button')
print(start_app_btn.text, '------')
if start_app_btn:
    start_app_btn.click()
print(dir(el))
print(el.get_attribute('src'))
captcha_key = el.get_attribute('src').split('&')
driver.quit()