import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url_textbox = "https://demoqa.com/text-box"
value_url_textbox = "Text Box"
xpath_url_textbox = "//div[@class='main-header']"
xpath_response_frame="//div[@class='border col-md-12 col-sm-12']"

#xpath_submit = "//button[@id='submit']"
xpath_submit = "//*[@id='submit']"
#Values to send
value_fullname = "Andrew"
value_email = "a1@q1.com"
value_current_address = "Arizona"
value_permanent_address = "Washington"

#Send value XPath
xpath_fullname = "//input[@id='userName']"
xpath_email = "//input[@id='userEmail']"
xpath_current_address = "//textarea[@id='currentAddress']"
xpath_permanent_address = "//textarea[@id='permanentAddress']"

#Response XPath
xpath_response_fullname = "//p[@id='name']"
xpath_response_email = "//p[@id='email']"
xpath_response_current_address = "//p[@id='currentAddress']"
xpath_response_permanent_address = "//p[@id='permanentAddress']"

class demoqa_TextBox(unittest.TestCase):

    def validate_response(self, name_search, value_search, response_xpath):
        response_to_return = self.driver.find_element_by_xpath(response_xpath).text
        if value_search in response_to_return:
         return True
        else:
            r1 = "name_search: " + name_search + "; value_search: " + value_search + "; response_to_return:" + response_to_return
            print(r1)
            return False


    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_textbox(self):
        self.driver.get(url_textbox)
        get_can_create_page = self.driver.find_element_by_xpath(xpath_url_textbox).text
        if value_url_textbox in get_can_create_page:
            print("Search register XPath:" + get_can_create_page)
            self.driver.find_element_by_xpath(xpath_fullname).send_keys(value_fullname)
            self.driver.find_element_by_xpath(xpath_email).send_keys(value_email)
            self.driver.find_element_by_xpath(xpath_current_address).send_keys(value_current_address)
            self.driver.find_element_by_xpath(xpath_permanent_address).send_keys(value_permanent_address)
            self.driver.find_element_by_xpath(xpath_submit).send_keys(Keys.RETURN)
            #time.sleep(2)
            #Check response frame
            get_response_frame = self.driver.find_element_by_xpath(xpath_response_frame)
            if get_response_frame:
                print("Response frame create")
                #Validate send value to responsed value

                q1 = self.validate_response("Response Fullname", value_fullname, xpath_response_fullname)
                assert q1, "Test fail"
                q1 = self.validate_response("Response email", value_email, xpath_response_email)
                assert q1, "Test fail"
                q1 = self.validate_response("Current address",value_current_address,xpath_response_current_address)
                assert q1, "Test fail"
                q1 = self.validate_response("Permanet address", value_permanent_address, xpath_response_permanent_address)
                assert q1, "Test fail"

                #Testing to fail
                # q1 = self.validate_response("Response Fullname but false value", "Name1", xpath_response_fullname)
                # assert q1, "Test fail"
            else:
                print("Response frame not create")
        else:
            print("This is not register page")

    def tearDown(self):
        # close the browser window
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()