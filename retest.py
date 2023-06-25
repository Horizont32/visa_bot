import re

from pypasser import reCaptchaV3

# lnk = 'https://recaptcha.net/recaptcha/api2/anchor?ar=1&k=6LdJReUUAAAAAPR1hddg-9JUC_TO13OrlKVpukHL&co=aHR0cHM6Ly92aXNhLnZmc2dsb2JhbC5jb206NDQz&hl=en&v=SglpK98hSCn2CroR0bKRSJl5&size=invisible&cb=e0cuygl9fzv'
# src = 'https://recaptcha.net/recaptcha/api2/anchor?ar=1&k=6LfDUY8bAAAAAPU5MWGT_w0x5M-8RdzC29SClOfI&co=aHR0cHM6Ly92aXNhLnZmc2dsb2JhbC5jb206NDQz&hl=en&v=SglpK98hSCn2CroR0bKRSJl5&size=normal&cb=u1vnfv2kg62i'
# print(re.findall('k=*', lnk))
# is_checked = reCaptchaV3(src)
# print(is_checked)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://visa.vfsglobal.com/rus/en/fra/login")
el = WebDriverWait(driver, 10).until(lambda p: p.find_element(By.XPATH, '//form/button'))
print()