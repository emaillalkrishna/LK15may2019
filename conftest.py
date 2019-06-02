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
# # # In this As this is the conftest , we must provide the word "rrquest" insted of self
# # # As this file is conftest we have to provide a extra line which is "request.cls.driver = driver"
#
# from selenium import webdriver
# import pytest
# from testdata.data import *
# #
# #
# # @pytest.fixture(scope="class")
# @pytest.fixture(scope='session')
# def test_launchbrowser(request):
#     global driver
#     driver = webdriver.Chrome(Executable_Path)
#     driver.get(URL)
#     driver.maximize_window()
#     driver.implicitly_wait(30)
#
#     request.cls.driver = driver
#
#     yield
#     driver.quit()


# # # --------------------------------------------step 11--------------------------------------------------------------
# # #  Provide the def test_launchbrowser(request):

# from selenium import webdriver
# import pytest
# from testdata.data import *
#
#
# # @pytest.fixture(scope="class")
# @pytest.fixture(scope='session')
# def test_launchbrowser(request):
#     global driver
#     driver = webdriver.Chrome(Executable_Path)
#     driver.get(URL)
#     driver.maximize_window()
#     driver.implicitly_wait(30)
#     request.cls.driver = driver
#     yield
#     driver.quit()

# # # --------------------------------------------step 12--------------------------------------------------------------
# # # In this step there is no change in the code



# # # # --------------------------------------------Level 2 step 13-------------------------------------------------------------
#
# from selenium import webdriver
# import pytest
# from testdata.data import *
#
#
# @pytest.fixture(scope="class")
# # @pytest.fixture(scope='session')
# def test_launchbrowser(request):
#     global driver
#     driver = webdriver.Chrome(Executable_Path)
#     driver.get(URL)
#     driver.maximize_window()
#     driver.implicitly_wait(30)
#     request.cls.driver = driver
#     yield
#     driver.quit()


# # # --------------------------------------------Level 2 step 14-------------------------------------------------------------
# # # No change in this step
from selenium import webdriver
import pytest
from testdata.data import *


@pytest.fixture(scope="class")
# @pytest.fixture(scope='session')
def test_launchbrowser(request):
    global driver
    driver = webdriver.Chrome(Executable_Path)
    driver.get(URL)
    driver.maximize_window()
    driver.implicitly_wait(30)
    request.cls.driver = driver
    yield
    driver.quit()