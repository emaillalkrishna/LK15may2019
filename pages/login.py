# # # --------------------------------------------step 1--------------------------------------------------------------
# # # This file is Not Created in step 1

# # # --------------------------------------------step 2--------------------------------------------------------------
# # # This file is Not Created in step 2

# # # --------------------------------------------step 3--------------------------------------------------------------
# # # This file is Not Created in step 3

# # # --------------------------------------------step 4--------------------------------------------------------------
# # # This file is Not Created in step 4

# # # --------------------------------------------step 5--------------------------------------------------------------
# # # Directory Number 3 : Create a directory named as " pages "
# # # Create two python files under the directory " pages "
# # # File name 1: login
# # # File name 2: home

# # # The part which need to be copied to this file named as login from file "test_myfile_jenkins" is as shown below
# # # Line 1 :   driver.find_element_by_name("j_username").send_keys("admin")
# # # Line 2 :   driver.find_element_by_name("j_password").send_keys("manager")
# # # Line 3 :   driver.find_element_by_name("Submit").click()


# # # Now Create a class names as LoginPage and provide these 3 lines inside the class under 3 different methods
# # # Note: When we are doing so, don`t forget that we have to provide self parameter as shown below
# # # So there will 3 methods in this python file "login"
# # # Methods 1 : def enter_username(self)
# # # Methods 2 : def enter_password(self)
# # # Methods 3 : def click_signinbutton(self)

# # # class LoginPage:
# # #
# # #    def enter_username(self):
# # #         self.driver.find_element_by_name("j_username").send_keys("admin")
# # #
# # #     def enter_password(self):
# # #         self.driver.find_element_by_name("j_password").send_keys("manager")
# # #
# # #     def click_signinbutton(self):
# # #         self.driver.find_element_by_name("Submit").click()

# # # Then we have to create a constructor for the class where we will keep the static values used for the locators
# # #  1. self.un_by_name = "j_username"
# # #  2. self.pw_by_name = "j_password"
# # #  3. self.signinbutton_by_name = "Submit"
#
# class LoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.un_by_name = "j_username"
#         self.pw_by_name = "j_password"
#         self.signinbutton_by_name = "Submit"
#
#     def enter_username(self):
#         self.driver.find_element_by_name(self.un_by_name).send_keys("admin")
#
#     def enter_password(self):
#         self.driver.find_element_by_name(self.pw_by_name).send_keys("manager")
#
#     def click_signinbutton(self):
#         self.driver.find_element_by_name(self.signinbutton_by_name).click()

# # # --------------------------------------------step 6--------------------------------------------------------------
# # # Here as we are receiving the inputs from the page named as "data"
# # # so we have to import file named as "data"  to this file "login"
# # # File imported 1 : from testdata.data import *

# from testdata.data import *
#
# class LoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#
#         self.un_by_name = "j_username"
#         self.pw_by_name = "j_password"
#         self.signinbutton_by_name = "Submit"
#
#     def enter_username(self):
#         self.driver.find_element_by_name(self.un_by_name).send_keys(UN)
#
#     def enter_password(self):
#         self.driver.find_element_by_name(self.pw_by_name).send_keys(PW)
#
#     def click_signinbutton(self):
#         self.driver.find_element_by_name(self.signinbutton_by_name).click()


# # # --------------------------------------------step 7--------------------------------------------------------------
# # # In this step there is no change in the code

# from testdata.data import *
#
# class LoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#
#         self.un_by_name = "j_username"
#         self.pw_by_name = "j_password"
#         self.signinbutton_by_name = "Submit"
#
#     def enter_username(self):
#         self.driver.find_element_by_name(self.un_by_name).send_keys(UN)
#
#     def enter_password(self):
#         self.driver.find_element_by_name(self.pw_by_name).send_keys(PW)
#
#     def click_signinbutton(self):
#         self.driver.find_element_by_name(self.signinbutton_by_name).click()


# # # --------------------------------------------step 8--------------------------------------------------------------
# # # In this step there is no change in the code

# from testdata.data import *
#
# class LoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#
#         self.un_by_name = "j_username"
#         self.pw_by_name = "j_password"
#         self.signinbutton_by_name = "Submit"
#
#     def enter_username(self):
#         self.driver.find_element_by_name(self.un_by_name).send_keys(UN)
#
#     def enter_password(self):
#         self.driver.find_element_by_name(self.pw_by_name).send_keys(PW)
#
#     def click_signinbutton(self):
#         self.driver.find_element_by_name(self.signinbutton_by_name).click()


# # # --------------------------------------------step 9--------------------------------------------------------------
# # # In this step there is no change in the code

# from testdata.data import *
#
# class LoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#
#         self.un_by_name = "j_username"
#         self.pw_by_name = "j_password"
#         self.signinbutton_by_name = "Submit"
#
#     def enter_username(self):
#         self.driver.find_element_by_name(self.un_by_name).send_keys(UN)
#
#     def enter_password(self):
#         self.driver.find_element_by_name(self.pw_by_name).send_keys(PW)
#
#     def click_signinbutton(self):
#         self.driver.find_element_by_name(self.signinbutton_by_name).click()

# # # --------------------------------------------step 10--------------------------------------------------------------
# # # In this step there is no change in the code

# from testdata.data import *
#
# class LoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#
#         self.un_by_name = "j_username"
#         self.pw_by_name = "j_password"
#         self.signinbutton_by_name = "Submit"
#
#     def enter_username(self):
#         self.driver.find_element_by_name(self.un_by_name).send_keys(UN)
#
#     def enter_password(self):
#         self.driver.find_element_by_name(self.pw_by_name).send_keys(PW)
#
#     def click_signinbutton(self):
#         self.driver.find_element_by_name(self.signinbutton_by_name).click()
