from selenium import webdriver

def get_driver(url):
  options = webdriver.ChromeOptions()
  # Adds additional command line arguments when launching Chrome browser to make browsing easier
  argList = ['disable-infobars', 'start_maximized', 'disable-dev-smh-usage', 'no-sandbox', 'disable-blink-features=AutomationControlled']
  for arg in argList:
    options.add_argument(arg)
  options.add_experimental_option('excludeSwitches', ['enable-automation'])
  driver = webdriver.Chrome(options=options)
  driver.get(url)
  return driver

def main(url, xpath):
  driver = get_driver(url)
  element = driver.find_element(by='xpath', value=xpath)
  return element.text


print(main(url='http://automated.pythonanywhere.com', xpath='/html/body/div[1]/div/h1[1]'))
