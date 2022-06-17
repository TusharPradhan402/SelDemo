import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="F:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.implicitly_wait(5)
driver.find_element_by_xpath("//input[@class='search-keyword']").send_keys("ber")
time.sleep(2)
buttons=driver.find_elements_by_css_selector("div[class='product-action'] button")

for button in buttons:
    button.click()

driver.find_element_by_xpath("//a[@class='cart-icon']/img").click()
driver.find_element_by_xpath("// button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element_by_xpath("//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element_by_xpath("//button[@class='promoBtn']").click()
message=driver.find_element_by_xpath("//span[@class='promoInfo']").text

assert message=="Code applied ..!"







