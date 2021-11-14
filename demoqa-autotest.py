from selenium import webdriver
from selenium.webdriver.common.keys import Keys

userName2post = "UserTest1"
password2post = "Password_test"

def demoqa_user():

    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/register")

    can_create_page = driver.find_element_by_xpath("//h4[.='Register to Book Store']")
    print("Search register XPath:"+can_create_page)
    assert "Register" in can_create_page

    driver.get('https://demoqa.com/login')
    driver.find_element_by_xpath("//input[@id='userName']").send_keys("UserTest1")
    driver.find_element_by_xpath("//input[@id='password']").send_keys("UserTest1")
    driver.find_element_by_xpath("//button[@id='login']").click()
    userNameValue = driver.find_element_by_xpath("//label[@id='userName-value']").text
    print(userNameValue)
    assert "UserTest1" in userNameValue
    driver.close()

if __name__ == "__main__":
    demoqa_user()
