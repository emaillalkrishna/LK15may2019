# # # --------------------------------------Step 1-------------------------------------
# # # Directory Number 1 : Create a directory named as "drivers"
# # # Copy and paste the driver.exe file inside this directory
# # # Directory Number 2 : Create a directory named as "tests"
# # # Create a python files  named as "myfile1_jenkins" under the directory " tests "
# # # Should call all the functions at the end
# # # Execution By : Should Run the file directly

# import time
# from selenium import webdriver
#
# driver =webdriver.Chrome(executable_path="C:/Users/LAL KRISHNA/PycharmProjects/15may2019/drivers/chromedriver.exe")
# driver.get("http://localhost:8080/login?from=%2F")
# driver.maximize_window()
# driver.implicitly_wait(30)
#
# driver.find_element_by_name("j_username").send_keys("admin")
# driver.find_element_by_name("j_password").send_keys("manager")
# driver.find_element_by_name("Submit").click()
#
# time.sleep(5)
# driver.find_element_by_xpath("//*[text()='log out']").click()

# # # --------------------------------------Step 2-------------------------------------
# # # Keep different functionalities under different functions
# # # As we have 3 different functionalities to perform we have 3 different functions
# # # Function Number 1 : def launch_browser():
# # # Function Number 2 : def login():
# # # Function Number 3 : def logout():
# # # Should call all the functions at the end
# # # Execution By : Should Run the file directly

# import time
# from selenium import webdriver
#
#
# def launch_browser():
#     global driver
#     driver = webdriver.Chrome("C:/Users/LAL KRISHNA/PycharmProjects/15may2019/drivers/chromedriver.exe")
#     driver.get("http://localhost:8080/login?from=%2F")
#     driver.maximize_window()
#     driver.implicitly_wait(30)
#
#
# def login():
#     driver.find_element_by_name("j_username").send_keys("admin")
#     driver.find_element_by_name("j_password").send_keys("manager")
#     driver.find_element_by_name("Submit").click()
#
#
# def logout():
#     time.sleep(5)
#     driver.find_element_by_xpath("//*[text()='log out']").click()
#
#
# launch_browser()
# login()
# logout()

# # # --------------------------------------Step 3-------------------------------------
# # # Now Change the name of the file by adding a suffix "test_" to it.
# # # So file name will be come : "test_myfile1_jenkins"
# # # Similarly Change the name of the functions adding a suffix "test_" to it.
# # # Function Number 1 : def test_launch_browser():
# # # Function Number 2 : def test_login():
# # # Function Number 3 : def test_logout():
# # # Should call all the functions at the end

# # # Execution By : Should Run the file directly

# from selenium import webdriver
# import time
#
#
# def test_launch_browser():
#    global driver
#    driver = webdriver.Chrome("C:/Users/LAL KRISHNA/PycharmProjects/15may2019/drivers/chromedriver.exe")
#    driver.get(url="http://localhost:8080/login?from=%2F")
#    driver.maximize_window()
#    driver.implicitly_wait(10)
#
#
# def test_login():
#    driver.find_element_by_name("j_username").send_keys("admin")
#    driver.find_element_by_name("j_password").send_keys("manager")
#    driver.find_element_by_name("Submit").click()
#
#
# def test_logout():
#    time.sleep(5)
#    driver.find_element_by_xpath("//*[text()='log out']").click()
#
#
# test_launch_browser()
# test_login()
# test_logout()

# # # --------------------------------------Step 4-------------------------------------
# # # Install pytest in to the project
# # # Add the code " @pytest.fixture(scope="session") " above the Function Number 1 : def test_launch_browser():
# # # Provide the "test_launch_browser" inside the parenthesis of the other two functions
# # # Function Number 1 :
# # #                     @pytest.fixture(scope="session")
# # #                     def test_launch_browser():
# # # Function Number 2 : def test_login(test_launch_browser):
# # # Function Number 3 : def test_logout(test_launch_browser):
# # # In step 3 we mentioned : Should call all the functions at the end --> This Calling need to be removed for all 3 functions

# # # Execution : Should run the file in Terminal and use the “python -m pytest -v"

# import time
# from selenium import webdriver
# import pytest
#
# @pytest.fixture(scope="session")
# def test_launchbrowser():
#    global driver
#    driver = webdriver.Chrome(executable_path="C:/Users/LAL KRISHNA/PycharmProjects/15may2019/drivers/chromedriver.exe")
#    driver.get("http://localhost:8080/login?from=%2F")
#    driver.maximize_window()
#    driver.implicitly_wait(30)
#
# def test_login(test_launchbrowser):
#    driver.find_element_by_name("j_username").send_keys("admin")
#    driver.find_element_by_name("j_password").send_keys("manager")
#    driver.find_element_by_name("Submit").click()
#
#
# def test_logout(test_launchbrowser):
#    time.sleep(5)
#    driver.find_element_by_xpath("//*[text()='log out']").click()


# # # --------------------------------------Step 5-------------------------------------
# # # Directory Number 3 : Create a directory named as " pages "
# # # Create two python files under the directory " pages "
# # # File name 1: login
# # # File name 2: home
# # # Now go to the file login and home and perform code change in that pass as explained in that pages in Step 5

# # # Here as we are receiving the inputs from the file named as "login"  and "home" to our file named as "test_myfile1_jenkins"
# # # so we have to import file named as "data"  to this file "test_myfile1_jenkins"
# # # File imported 1 : from pages.home import HomePage
# # # File imported 2 : from pages.login import LoginPage

# # # Under the functions 1. test_login(test_launchbrowser) create objects using the class LoginPage and call the methods of the class LoginPage using the objects created
# # # Under the functions 2. test_Logout(test_launchbrowser) create objects using the class HomePage and call the methods of the class HomePage using the objects created

# # # Execution : Should run the file in Terminal and use the “python -m pytest -v"


# from selenium import webdriver
# import pytest
#
# from pages.home import HomePage
# from pages.login import LoginPage
#
#
# @pytest.fixture(scope="session")
# def test_launchbrowser():
#     global driver
#     driver = webdriver.Chrome(executable_path="C:/Users/LAL KRISHNA/PycharmProjects/15may2019/drivers/chromedriver.exe")
#     driver.get("http://localhost:8080/login?from=%2F")
#     driver.maximize_window()
#     driver.implicitly_wait(30)
#
#
# def test_login(test_launchbrowser):
#     lp = LoginPage(driver)
#     lp.enter_username()
#     lp.enter_password()
#     lp.click_signinbutton()
#
#
# def test_Logout(test_launchbrowser):
#     hp = HomePage(driver)
#     hp.click_on_logout()

# # #  --------------------------------------Step 6-------------------------------------
# # # Directory Number 4 : Create a directory named as " testdata "
# # # Create one python files under the directory " testdata "
# # # File name 1: data
# # # Now go to the file named as data and  perform code change

# # # Here as we are receiving the inputs from the page named as "data"
# # # so we have to import file named as "data"  to this file "test_myfile1_jenkins"
# # # File imported 3 : from testdata.data import *

# # # Execution : Should run the file in Terminal and use the “python -m pytest -v"


# from selenium import webdriver
#
# import pytest
#
# from pages.login import LoginPage
# from pages.home import HomePage
# from testdata.data import *
#
# @pytest.fixture(scope="session")
# def test_launchbrowser():
#     global driver
#     driver = webdriver.Chrome(Executable_Path)
#     driver.get(URL)
#     driver.maximize_window()
#     driver.implicitly_wait(30)
#
#
# def test_login(test_launchbrowser):
#     lp = LoginPage(driver)
#     lp.enter_username()
#     lp.enter_password()
#     lp.click_signinbutton()
#
#
# def test_Logout(test_launchbrowser):
#     hp = HomePage(driver)
#     hp.click_on_logout()


# # #  --------------------------------------Step 7-------------------------------------
# # # Provide the function "test_launch_browser()" in side a class names as "JenkinLogin"
# # # So function "test_launch_browser()" becomes a method inside the class "JenkinLogin"
# # # Change the code @pytest.fixture(scope="session") to @pytest.fixture(scope="class") which was provided above the Method Number 1 : test_launch_browser()
# # # Then the Method Number 1 will be as shown below :
# # #                                                       class JenkinLogin:
# # #                                                           @pytest.fixture(scope="class")
# # #                                                           def test_launchbrowser(self):

# # # Then the Method Number 2 will be as shown below :
# # #                                                           def test_login(self, test_launchbrowser):

# # # Then the Method Number 3 will be as shown below :
# # #                                                           def test_Logout(self, test_launchbrowser):


# # #  Execution : Should run the file in Terminal and use the “python -m pytest -v"



# from selenium import webdriver
# import pytest
# from pages.login import LoginPage
# from pages.home import HomePage
# from testdata.data import *
#
# class JenkinLogin:
#     @pytest.fixture(scope="class")
#     def test_launchbrowser(self):
#         global driver
#         driver = webdriver.Chrome(Executable_Path)
#         driver.get(URL)
#         driver.maximize_window()
#         driver.implicitly_wait(30)
#
#
#     def test_login(self, test_launchbrowser):
#         lp = LoginPage(driver)
#         lp.enter_username()
#         lp.enter_password()
#         lp.click_signinbutton()
#
#
#     def test_Logout(self, test_launchbrowser):
#         hp = HomePage(driver)
#         hp.click_on_logout()


# # # --------------------------------------Step 8 -------------------------------------
# # # At the bottom of the method "test_launchbrowser()" add a key word "yield"

# # # Execution : Should run the file in Terminal and use the “python -m pytest -v"

# from selenium import webdriver
# import pytest
# from pages.login import LoginPage
# from pages.home import HomePage
# from testdata.data import *
#
# class JenkinLogin:
#     @pytest.fixture(scope="class")
#     def test_launchbrowser(self):
#         global driver
#         driver = webdriver.Chrome(Executable_Path)
#         driver.get(URL)
#         driver.maximize_window()
#         driver.implicitly_wait(30)
#         yield
#
#
#     def test_login(self, test_launchbrowser):
#         lp = LoginPage(driver)
#         lp.enter_username()
#         lp.enter_password()
#         lp.click_signinbutton()
#
#
#     def test_Logout(self, test_launchbrowser):
#         hp = HomePage(driver)
#         hp.click_on_logout()


# # # --------------------------------------Step 9-------------------------------------
# # # In this step there is no change in the code
# # # Directory Number 5 : Create a directory named as " reports "
# # # Execution : Should run the file in Terminal and use the “python -m pytest -v --html=reports/rep1.html”

# from selenium import webdriver
# import pytest
# from pages.login import LoginPage
# from pages.home import HomePage
# from testdata.data import *
#
# class JenkinLogin:
#     @pytest.fixture(scope="class")
#     def test_launchbrowser(self):
#         global driver
#         driver = webdriver.Chrome(Executable_Path)
#         driver.get(URL)
#         driver.maximize_window()
#         driver.implicitly_wait(30)
#         yield
#         driver.quit()
#
#
#     def test_login(self, test_launchbrowser):
#         lp = LoginPage(driver)
#         lp.enter_username()
#         lp.enter_password()
#         lp.click_signinbutton()
#
#
#     def test_Logout(self, test_launchbrowser):
#         hp = HomePage(driver)
#         hp.click_on_logout()

# # # --------------------------------------Step 10-------------------------------------
# # # Create a python file directly under the project name it exactly as "conftest"
# # # Cut and paste the "test_launchbrowser(self)" method from the file "test_myfile1_jenkins" to "conftest"
# # # Use the line " @pytest.mark.usefixtures("test_launchbrowser") " above "class JenkinLogin:"
# # # As the "test_launchbrowser(self)" method is moved from the file "test_myfile1_jenkins" to "conftest" so remove it from other two methods parenthesis
# # # So the other two methods will as shown below
# # # In step 9   : def test_login(self, test_launchbrowser):   &  def test_Logout(self, test_launchbrowser):
# # # In step 10  : def test_login(self):                       &  def test_Logout(self):


# import pytest
# from pages.login import LoginPage
# from pages.home import HomePage
#
# @pytest.mark.usefixtures("test_launchbrowser")
# class JenkinLogin:
#
#     def test_login(self):
#         driver = self.driver
#         lp = LoginPage(driver)
#         lp.enter_username()
#         lp.enter_password()
#         lp.click_signinbutton()
#
#
#     def test_Logout(self):
#         driver = self.driver
#         hp = HomePage(driver)
#         hp.click_on_logout()
