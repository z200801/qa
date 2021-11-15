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

#Array response name
array_response_name = ['name','email','currentAddress', 'permanentAddress']

ar1 = array_response_name
#Response XPath
xpath_response_fullname = "//p[@id='"+ar1[0]+"']"
xpath_response_email = "//p[@id='"+ar1[1]+"']"
xpath_response_current_address = "//p[@id='"+ar1[2]+"']"
xpath_response_permanent_address = "//p[@id='"+ar1[3]+"']"


#Array contains [fullname, email, current_address, permanent_address]
array_values_to_send = [value_fullname, value_email, value_current_address, value_permanent_address]

#Array contains XPath for send values_to_send
array_xpath_to_send = [xpath_fullname, xpath_email, xpath_current_address,xpath_permanent_address]

#Array contains XPath to response from frame xpath_response_frame
array_xpath_to_response_frame = [xpath_response_fullname, xpath_response_email, xpath_response_current_address, xpath_response_permanent_address]

class demoqa_TextBox(unittest.TestCase):

    def validate_response(self, name_search, value_search, response_xpath):
        response_to_return = self.driver.find_element_by_xpath(response_xpath).text
        if value_search in response_to_return:
         return True
        else:
            r1 = "name_search: " + name_search + "; value_search: " + value_search + "; response_to_return:" + response_to_return
            print(r1)
            return False

    def tst_values(self, array_to_test):
        ar_values = array_to_test
        ar_xpath = array_xpath_to_send
        for i in range(len(ar_values)):
            # print("Values at #:", i, " values:", ar_values[i])
            # print("XPath at #:", i, " values:", ar_xpath[i])
            self.driver.find_element_by_xpath(ar_xpath[i]).send_keys(ar_values[i])
        self.driver.find_element_by_xpath(xpath_submit).send_keys(Keys.RETURN)
        # sleeping 3 sec
        time.sleep(3)

        # Check response frame
        get_response_frame = self.driver.find_element_by_xpath(xpath_response_frame)
        if get_response_frame:
            print("Response frame create")
            # Validate send value to responsed value
            ar_rs_xpath = array_xpath_to_response_frame
            for i in range(len(ar_rs_xpath)):
                q1 = self.validate_response("Response " + array_response_name[i], array_values_to_send[i],
                                            ar_rs_xpath[i])
                assert q1, "Test fail"
            # Testing to fail
            # q1 = self.validate_response("Response Fullname but false value", "Name1", xpath_response_fullname)
            # assert q1, "Test fail"

            # sleeping 3 sec
            time.sleep(3)
        else:
                print("Response frame not create")

    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(30)
        self.driver.maximize_window()

#Main function
    def test_textbox(self):
        self.driver.get(url_textbox)
        get_can_create_page = self.driver.find_element_by_xpath(xpath_url_textbox).text
        if value_url_textbox in get_can_create_page:
            print("Search register XPath:" + get_can_create_page)
            #Testing value from array
            self.tst_values(array_values_to_send)
        else:
            print("This is not register page")

    def tearDown(self):
        # close the browser window
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()