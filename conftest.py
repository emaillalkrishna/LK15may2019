# # # --------------------------------------------step 1--------------------------------------------------------------
# #  This file is Not Created in step 1

# # # --------------------------------------------step 2--------------------------------------------------------------
# #  This file is Not Created in step 2

# # # --------------------------------------------step 3--------------------------------------------------------------
# #  This file is Not Created in step 3

# # # --------------------------------------------step 4--------------------------------------------------------------
# #  This file is Not Created in step 4

# # # --------------------------------------------step 5--------------------------------------------------------------
# #  This file is Not Created in step 5

# # # --------------------------------------------step 6--------------------------------------------------------------
# #  This file is Not Created in step 6

# # # --------------------------------------------step 7--------------------------------------------------------------
# #  This file is Not Created in step 7

# # # --------------------------------------------step 8--------------------------------------------------------------
# #  This file is Not Created in step 8

# # # --------------------------------------------step 9--------------------------------------------------------------
# #  This file is Not Created in step 9

# # # --------------------------------------------step 10--------------------------------------------------------------
# # # Create a python file directly under the project name it exactly as "conftest"
# # # Copy the "test_launchbrowser(self)" method from the file "test_myfile1_jenkins" to "conftest"

# from selenium import webdriver
# import pytest
# from testdata.data import *
#
#
# # @pytest.fixture(scope="class")
# @pytest.fixture(scope='session')
# def test_launchbrowser(self):
#     global driver
#     driver = webdriver.Chrome(Executable_Path)
#     driver.get(URL)
#     driver.maximize_window()
#     driver.implicitly_wait(30)
#     yield
#     driver.quit()
