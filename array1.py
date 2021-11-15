#import unittest
#import time
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys


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

#Array contains [fullname, email, current_address, permanent_address]
array_values_to_send = [value_fullname, value_email, value_current_address, value_permanent_address]

#Array contains XPath for send values_to_send
array_xpath_to_send = [xpath_fullname, xpath_email, xpath_current_address,xpath_permanent_address]

#Array contains XPath to response from frame xpath_response_frame
array_xpath_to_response_frame = [xpath_response_fullname, xpath_response_email, xpath_response_current_address, xpath_response_permanent_address]

ar1 = array_values_to_send
for i in range(len(ar1)): print("Values at #:",i," is:",ar1[i])

ar1 = array_xpath_to_send
for i in range(len(ar1)): print("Values at #:",i," is:",ar1[i])

ar1 = array_xpath_to_response_frame
for i in range(len(ar1)): print("Values at #:",i," is:",ar1[i])

