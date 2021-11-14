import unittest
import time
from selenium import webdriver

class demoqa_SearchText(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
       # self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_register_user(self):
        self.driver.get("https://demoqa.com/register")
        get_can_create_page = self.driver.find_element_by_xpath("//h4[.='Register to Book Store']").text
        if 'Register' in get_can_create_page:
            captcha_id="//label[@id='recaptcha-anchor-label']"
            print("Search register XPath:" + get_can_create_page)
            self.driver.find_element_by_xpath("//input[@id='firstname']").send_keys("FirstName1")
            self.driver.find_element_by_xpath("//input[@id='lastname']").send_keys("lastName1")
            self.driver.find_element_by_xpath("//input[@id='userName']").send_keys("userName1")
            self.driver.find_element_by_xpath("//input[@id='password']").send_keys("password1")
            self.driver.find_element_by_xpath(captcha_id).click()


            #time.sleep(2)
            #Not work
            #self.driver.find_element_by_xpath("//button[@id='register']").click()
        else:
            print("This is not register page")

    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()