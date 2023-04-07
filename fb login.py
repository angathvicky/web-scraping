from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://mbasic.facebook.com")
# Creating a Reference of Form For Finding Email and Password
form = driver.find_element('xpath', "//form[@id ='login_form']")
email = form.find_element('name', "email")
password = form.find_element('name', "pass")
email.send_keys("remesh222@gmail.com")
password.send_keys("valarmorghulis")
submit_button = driver.find_element('xpath', "//input[@type ='submit']")

submit_button.click()