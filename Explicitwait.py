import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="F:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element_by_xpath("//input[@class='search-keyword']").send_keys("ber")
time.sleep(2)
buttons=driver.find_elements_by_css_selector("div[class='product-action'] button")

for button in buttons:
    button.click()

driver.find_element_by_xpath("//a[@class='cart-icon']/img").click()
driver.find_element_by_xpath("// button[text()='PROCEED TO CHECKOUT']").click()
wait=WebDriverWait(driver, 8)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,  "//input[@class='promoCode']")))
driver.find_element_by_xpath("//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element_by_xpath("//button[@class='promoBtn']").click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//span[@class='promoInfo']")))
message=driver.find_element_by_xpath("//span[@class='promoInfo']").text

assert message=="Code applied ..!"