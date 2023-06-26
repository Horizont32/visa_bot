# import time, os, re, json
# import telebot as tb
import time
from pypasser import reCaptchaV2, reCaptchaV3
import configparser
import undetected_chromedriver as uc

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# Importing config
config = configparser.ConfigParser()
config.read('cfg.ini')
URL = config.get('LoginData', 'url')
EMAIL = config.get('LoginData', 'email')
PASSWORD = config.get('LoginData', 'pwd')
# driver = webdriver.Chrome()
driver = uc.Chrome()


driver.get(URL)
el = WebDriverWait(driver, 100).until(lambda p: p.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]'))
# Create an instance of webdriver and open the page has recaptcha v2
# ...
time.sleep(8)


#accepting all cookies
cookie_acceptor = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
if cookie_acceptor:
    cookie_acceptor.click()

email_form = driver.find_element(By.ID, 'mat-input-0').send_keys(EMAIL)
pass_form = driver.find_element(By.ID, 'mat-input-1').send_keys(PASSWORD)
# pass the driver to reCaptchaV2
# is_checked = reCaptchaV2(driver) # it returns bool
is_checked = reCaptchaV3(el.get_attribute('src'))
query = f"___grecaptcha_cfg.clients['0'].O.O.callback('{is_checked}');"
# print(query)
driver.execute_script(query)
# is_checked = reCaptchaV3('https://www.recaptcha.net/recaptcha/api2/anchor?ar=1&k=6LfDUY8bAAAAAPU5MWGT_w0x5M-8RdzC29SClOfI&co=aHR0cHM6Ly92aXNhLnZmc2dsb2JhbC5jb206NDQz&hl=en&v=SglpK98hSCn2CroR0bKRSJl5&size=normal&cb=v3n9p9ydwh61')
# print(is_checked)
driver.execute_script(f'document.getElementById("g-recaptcha-response").innerHTML="{is_checked}";')
driver.execute_script(f'document.getElementById("g-recaptcha-response-100000").innerHTML="{is_checked}";')
time.sleep(2)
driver.find_element(By.XPATH, '//form/button').click()

#Dashboard page
time.sleep(4)

#Unix-based driver implementation
start_app_btn = driver.find_element(By.XPATH, '//app-dashboard/section[1]/div/div[@class="position-relative"]/button')

#Windows driver implementation
# start_app_btn = driver.find_element(By.XPATH, '//div[@class="col-12 col-sm-auto d-lg-none"]/button')
print(start_app_btn.tag_name, '------')
if start_app_btn:
    start_app_btn.click()

#Appointment details page
time.sleep(4)

location_selector = driver.find_element(By.XPATH, '//mat-select[@formcontrolname="centerCode"]')
location_selector.click()
time.sleep(1)
# Unix-based driver implementation
# driver.find_element(By.XPATH, '//div[@role="listbox"]/mat-option[@id="mat-option-6"]').click()
WebDriverWait(driver, 10).until(lambda p: p.find_element(By.XPATH, '//div[@role="listbox"]/mat-option[@id="mat-option-6"]')).click()

#Windows driver implementation
# driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-option-6"]/span'))))

time.sleep(3)


# visaCat = driver.find_element(By.XPATH, '//mat-select[@formcontrolname="selectedSubvisaCategory"]')
visaCat = WebDriverWait(driver, 10).until(lambda p: p.find_element(By.XPATH, '//mat-select[@formcontrolname="selectedSubvisaCategory"]'))
visaCat.click()
time.sleep(1)
# Unix-based driver implementation
WebDriverWait(driver, 10).until(lambda p: p.find_element(By.XPATH, '//div[@role="listbox"]/mat-option[@id="mat-option-20"]')).click()
# driver.find_element(By.XPATH, '//div[@role="listbox"]/mat-option[@id="mat-option-20"]').click()

#Windows driver implementation
# driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-option-20"]/span'))))

time.sleep(3)

visaCatCode = driver.find_element(By.XPATH, '//mat-select[@formcontrolname="visaCategoryCode"]')
visaCatCode.click()
# driver.execute_script("arguments[0].click();", visaCatCode)
time.sleep(1)
print('before executing last checkbox script')
# Unix-based driver implementation
driver.find_element(By.XPATH, '//div[@role="listbox"]/mat-option[@id="mat-option-23"]').click()

#Windows driver implementation
# driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-option-23"]/span'))))

time.sleep(3)

continue_btn = driver.find_element(By.XPATH, '//app-eligibility-criteria/section/form/mat-card[2]/button')
print(continue_btn.tag_name, '------')
if continue_btn:
    continue_btn.click()

time.sleep(3)

driver.find_element(By.XPATH, '//input[@data-placeholder="Enter your first name"]').send_keys(config.get('AppointmentData', 'name'))
driver.find_element(By.XPATH, '//input[@data-placeholder="Please enter last name."]').send_keys(config.get('AppointmentData', 'lastName'))
driver.find_element(By.XPATH, '//app-dynamic-form/div/div/app-dynamic-control[4]/div/div[1]/div/app-dropdown/div/mat-form-field/div/div[1]/div[3]/mat-select').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div/div/mat-option[2]').click()
time.sleep(5)
driver.find_element(By.ID, 'dateOfBirth').send_keys(config.get('AppointmentData', 'bday'))

driver.find_element(By.XPATH, '//app-dynamic-form/div/div/app-dynamic-control[5]/div/div/div/app-dropdown/div/mat-form-field/div/div[1]/div[3]/mat-select').click()
time.sleep(3)

driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div/div/mat-option[172]').click()
driver.find_element(By.XPATH, '//input[@data-placeholder="Enter passport number"]').send_keys(config.get('AppointmentData', 'pnum'))
driver.find_element(By.ID, 'passportExpirtyDate').send_keys(config.get('AppointmentData', 'pex'))
driver.find_element(By.XPATH, '//input[@data-placeholder="44"]').send_keys(config.get('AppointmentData', 'phonecode'))
driver.find_element(By.XPATH, '//input[@data-placeholder="012345648382"]').send_keys(config.get('AppointmentData', 'phonenum'))
driver.find_element(By.XPATH, '//input[@type="email"]').send_keys(config.get('AppointmentData', 'email'))


save_btn = driver.find_element(By.XPATH, '//app-dynamic-control/div/div/div[2]/button').click()
time.sleep(10)
# print(dir(el))
# print(el.get_attribute('src'))
# captcha_key = el.get_attribute('src').split('&')
driver.quit()