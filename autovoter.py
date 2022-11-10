from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random

for i in range(0, 10):
    #browser exposes an executable file
    #Through Selenium test we will invoke the executable file which will then #invoke actual browser
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    # to maximize the browser window
    driver.maximize_window()
    #get method to launch the URL
    driver.get("https://news.scorebooklive.com/south-carolina/2022/10/16/vote-now-who-should-be-sblives-south-carolina-athlete-of-the-week-oct-10-15")
    #to refresh the browser
    # driver.refresh()
    time.sleep(10)
    time.sleep(random.randint(0,5))
    # identifying the checkbox with xpath, then click
    firstElement = driver.find_element(By.ID, 'PDI_answer51289409')
    firstElement.click()
    # driver.find_element(By.ID, "PDI_answer51289409").click()
    # to close the browser
    secondElement = driver.find_element(By.ID, 'pd-vote-button11221085')
    driver.execute_script("arguments[0].click();", secondElement)
    driver.close()
