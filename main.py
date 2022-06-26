from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import threading
from datetime import datetime


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

  
def extract_clean_text(driver, by, value):
  ''' Returns cleaned element text'''
  element = driver.find_element(by=by, value=value)
  output = float(element.text.split(': ')[1])
  return output


def log_in(login_url, home_url, username, password):
  ''' Logs into website and returns to home screen'''
  driver = get_driver(login_url)
  driver.find_element(by='id', value='id_username').send_keys(username)
  time.sleep(2)
  driver.find_element(by='id', value='id_password').send_keys(password + Keys.RETURN)
  time.sleep(2)
  driver.find_element(by='xpath', value='/html/body/nav/div/a').click()
  time.sleep(2)
  driver = get_driver(home_url)
  time.sleep(2)
  return driver


def main():
  ''' Main function to log in, scrape average temperature, and save data to .txt files'''
  numIterations = 20
  pauseSeconds = 5
  home_url = 'http://automated.pythonanywhere.com'
  login_url = 'http://automated.pythonanywhere.com/login/'
  xpath_h1_2 = '/html/body/div[1]/div/h1[2]'
  # User logs in once
  driver = log_in(login_url=login_url, home_url=home_url, username='automated', password='automatedautomated')
  # Saves data to .txt files every 5 seconds. Stops at 20 files
  i = 0
  while i <= numIterations:
    with open('{}.txt'.format(datetime.now()), 'w+') as file:
      file.write(str(extract_clean_text(driver=driver, by='xpath', value=xpath_h1_2)))
      file.close()
    time.sleep(pauseSeconds)
    i += 1
  print(' Process Complete')


main()