from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import time
with open('account.txt','r') as file:
    content = file.read()
    content = eval(content)
    print(type(content))
admin = content['admin']
passwd = content['passwd']
driver = webdriver.Edge() 
driver.get('https://tenek.vip/#/') 
mail_adress = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div/div[2]/div/form/div[1]/div/input')))
mail_adress_input = admin
mail_adress.send_keys(mail_adress_input)
password = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div/div[2]/div/form/div[2]/div/input')))
password_input = passwd
password.send_keys(password_input)
login = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div[2]/div/div[2]/a')))
login.click()
try:
    mine = WebDriverWait(driver,1800).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div[2]/div[2]/div[3]/a/div')))
    mine.click()
    time.sleep(3)
finally:
    driver.quit()
