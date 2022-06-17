from selenium import webdriver

driver=webdriver.Chrome(executable_path="F:\\chromedriver.exe")
driver.get("https://login.salesforce.com/?locale=us")
print(driver.find_element_by_xpath("// form[@name='login']/div[1]/label").text)
print(driver.find_element_by_xpath("// form[@name='login']/label").text)
driver.find_element_by_xpath("//a [@id='forgot_password_link']").click()
driver.find_element_by_xpath("//input [@name='cancel']").click()
driver.find_element_by_id("username").send_keys("xyz")
driver.find_element_by_id("password").send_keys("xyz")
#driver.find_element_by_xpath("//*[@id='password']").send_keys("xyz")
