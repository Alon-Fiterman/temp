#0558858288

import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

path = '/Users/alonfiterman/IdeaProjects/test/chromedriver'
driver = webdriver.Chrome(path)
driver.get('http://students-aid.org:9222/')

join = driver.find_element(By.ID, "register").click()
WebDriverWait(driver, timeout=5)
driver.implicitly_wait(5)
driver.find_element(By.ID, "firstname").send_keys("John")
driver.find_element(By.ID, "lastname").click()
driver.find_element(By.ID, "lastname").send_keys("Doe")
driver.find_element(By.ID, "personalId").click()
driver.find_element(By.ID, "personalId").send_keys("123123123")
driver.find_element(By.ID, "phone").click()
driver.find_element(By.ID, "phone").send_keys("0545789565")
driver.find_element(By.ID, "dateOfBirth").click()
driver.find_element(By.ID, "dateOfBirth").send_keys("06011994")
driver.find_element(By.XPATH, '//*[@id="form-register"]/div[1]/div[4]/div[2]/div/div/div[1]').click()
driver.find_element(By.ID, "agreeTerms").click()
driver.find_element(By.XPATH,'//*[@id="form-buttons"]/div/button').click()

