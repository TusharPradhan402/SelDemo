from selenium import webdriver



driver=webdriver.Chrome(executable_path="F:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
#driver.find_element(by.className("name")).send_keys("check")
#driver.find_element_by_name("name").send_keys("check")
driver.find_element_by_css_selector("input[name='name']").send_keys("check")
driver.find_element_by_css_selector("input[name='email']").send_keys("email")
driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_xpath("//input[@type='submit']").click()
msg=driver.find_element_by_xpath("//*[@class='alert alert-success alert-dismissible']").text
assert "Success" in msg
