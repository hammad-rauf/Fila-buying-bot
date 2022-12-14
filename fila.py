import csv
from parsel import Selector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import os

# --kiosk

file = open('account.txt','r')
file_data  =  file.readlines()
username = file_data[0].replace("\n","")
password = file_data[1].replace("\n","")
file.close()


file = open('input.txt','r')
file_data  =  file.readlines()
url = file_data[0].replace("\n","")
size = file_data[1].replace("\n","")
file.close()



options = webdriver.ChromeOptions()
options.add_argument('--disable-backgrounding-occluded-windows')
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

try:
    path = os.path.join(os.path.abspath(os.getcwd()),'chromedriver')

    driver = webdriver.Chrome(options=options,executable_path=path)
except:
    path = os.path.join(os.path.abspath(os.getcwd()),'chromedriver.exe')

    driver = webdriver.Chrome(options=options,executable_path=path)


driver.get('https://www.fila.com/account')

WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CSS_SELECTOR , 'div[data-required-text="Please enter your email address"] input')))
driver.find_element(By.CSS_SELECTOR,'div[data-required-text="Please enter your email address"] input').send_keys(username)

sleep(1)

WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CSS_SELECTOR , 'div[data-required-text="Please enter your password"] input')))
driver.find_element(By.CSS_SELECTOR,'div[data-required-text="Please enter your password"] input').send_keys(password)
   
sleep(1) 

WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH , "//button[contains(text(),'Sign In')]")))
driver.find_element(By.XPATH,"//button[contains(text(),'Sign In')]").click()
  
sleep(2.5)

link = None
while True:

    driver.get(url)

    try:
        WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH , f"//ul[@class='swatches size']//span[normalize-space() = '{size}']//parent::a")))
        
        link = driver.find_element(By.XPATH,f"//ul[@class='swatches size']//span[normalize-space() = '{size}']//parent::a").get_attribute('href')

        break

    except:
        print('waiting for 30 sec, no size available.')
        sleep(30)


driver.get(link)

WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH , "//button[@id='add-to-cart']")))
driver.find_element(By.XPATH,"//button[@id='add-to-cart']").click()


sleep(3)


driver.get("https://www.fila.com/on/demandware.store/Sites-FILA-Site/en_US/COCustomer-Start")

WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH , '//span[contains(text(),"Select")]/parent::span//span[1]')))
driver.find_element(By.XPATH,'//span[contains(text(),"Select")]/parent::span//span[1]').click()
sleep(1)
driver.find_element(By.XPATH,'//div[@id="ui-id-3"]').click()

sleep(1)

element = driver.find_element(By.XPATH,'//button[@class="button-fancy-large button-solid"]')
driver.execute_script("return arguments[0].scrollIntoView(true);",element)
sleep(0.5)
element.click()

sleep(3)


WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CSS_SELECTOR , 'input[placeholder="Card Number"]')))
driver.find_element(By.CSS_SELECTOR,'input[placeholder="Card Number"]').send_keys('4263982640269299')

sleep(1)

WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CSS_SELECTOR , 'input[placeholder="Security code"]')))
driver.find_element(By.CSS_SELECTOR,'input[placeholder="Security code"]').send_keys('123')

sleep(1)

WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CSS_SELECTOR , 'input[placeholder="Name on Card"]')))
driver.find_element(By.CSS_SELECTOR,'input[placeholder="Name on Card"]').send_keys('python work')

sleep(1)

driver.find_element(By.XPATH,"//span[contains(text(),'January')]//parent::span//span[1]").click()
sleep(0.5)
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH , "//div[contains(text(),'February')]")))
driver.find_element(By.XPATH,"//div[contains(text(),'February')]").click()

sleep(1)

driver.find_element(By.XPATH,"//span[contains(text(),'2022')]//parent::span//span[1]").click()
sleep(0.5)
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH , "//div[contains(text(),'2023')]")))
driver.find_element(By.XPATH,"//div[contains(text(),'2023')]").click()

sleep(1)

element = driver.find_element(By.XPATH,'//span[contains(text(),"Continue to Review Order")]')
driver.execute_script("return arguments[0].scrollIntoView(true);",element)
sleep(0.5)
element.click()

sleep(2020)