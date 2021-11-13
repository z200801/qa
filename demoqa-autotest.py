from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://demoqa.com/login')

driver.find_element_by_xpath("//input[@id='userName']").send_keys("UserTest1")
driver.find_element_by_xpath("//input[@id='password']").send_keys("UserTest1")

driver.find_element_by_xpath("//buttun[@id='login']").click()

userNameValue=driver.find_element_by_xpath("//label[@id='userNmae-value']").text

print(userNameValue)

assert "UserTest1" in userNameValue

driver.close()
