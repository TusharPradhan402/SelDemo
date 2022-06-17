import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="F:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise//")
driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(2)
countries=driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print(len(countries))

for Country in countries:
    if Country.text == "India":
        Country.click()
        break

msg=driver.find_element_by_id("autosuggest").get_attribute('value')
assert msg=="India"
