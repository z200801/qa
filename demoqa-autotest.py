from selenium import webdriver

userName2post = "UserTest"
password2post = "Password_test"

driver = webdriver.Chrome()

driver.get('https://demoqa.com/login')

driver.find_element_by_xpath("//input[@id='userName']").send_keys("UserTest1")
driver.find_element_by_xpath("//input[@id='password']").send_keys("UserTest1")

driver.find_element_by_xpath("//button[@id='login']").click()

userNameValue = driver.find_element_by_xpath("//label[@id='userName-value']").text

print(userNameValue)

assert "UserTest1" in userNameValue

driver.close()
