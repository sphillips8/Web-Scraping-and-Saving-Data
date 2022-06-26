from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# User Can Get Xpath by inspecting HTML elements, hover over element, right click, and Copy Full Xpath

def get_driver(url):
  ''' Gets Chrome driver and adds additional options'''
  options = webdriver.ChromeOptions()
  # Adds additional command line arguments when launching Chrome browser to make browsing easier
  argList = ['disable-infobars', 'start_maximized', 'disable-dev-smh-usage', 'no-sandbox', 'disable-blink-features=AutomationControlled']
  for arg in argList:
    options.add_argument(arg)
  options.add_experimental_option('excludeSwitches', ['enable-automation'])
  driver = webdriver.Chrome(options=options)
  driver.get(url)
  return driver

  
def clean_text(text):
  ''' Extracts only temperature from text'''
  output = float(text.split(': ')[1])
  return output

  
def extract_text(url, by, value):
  ''' Returns element text'''
  driver = get_driver(url)
  time.sleep(2) # Waits for average world temperature to load
  element = driver.find_element(by=by, value=value)
  return element.text

def log_in(url, username, password):
  ''' Returns element text'''
  driver = get_driver(url)
  driver.find_element(by='id', value='id_username').send_keys(username)
  time.sleep(2)
  driver.find_element(by='id', value='id_password').send_keys(password + Keys.RETURN)
  time.sleep(2)
  driver.find_element(by='xpath', value='/html/body/nav/div/a').click()
  return driver.current_url

home_url = 'http://automated.pythonanywhere.com'
login_url = 'http://automated.pythonanywhere.com/login/'
xpath_h1_1 = '/html/body/div[1]/div/h1[1]'
xpath_h1_2 = '/html/body/div[1]/div/h1[2]'

# Extracting Text Exercises
print(extract_text(url=home_url, by='xpath', value=xpath_h1_1))
print(extract_text(url=home_url, by='xpath', value=xpath_h1_2))
print('Temperature Only: {}'.format(clean_text(text=extract_text(url=home_url, by='xpath', value=xpath_h1_2))))

# Logging In Exercises
print(log_in(url=login_url, username='automated', password='automatedautomated'))