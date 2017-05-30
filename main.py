import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def set_up(url, browser="chrome"):
  if (browser = "chrome"):
    options = Options() 
    options.add_argument("--start-maximized") 
    driver = webdriver.Chrome(chrome_options=options)
  
  
  elif (browser = "firefox"):
    driver = webdriver.firefox()  
  
  driver.get(url)
  return driver


driver = set_up(url)
