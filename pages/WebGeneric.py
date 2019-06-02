# # # # --------------------------------------------Level 2 -- step 13---------------------------------------------------
# # # # Create a file under the Pages named as WebGeneric
# # # # Create a class in that file with the name WebGeneric it self
# # # #
#
#
# class WebGeneric:
#     def __init__(self,driver):
#         self.driver = driver
#
#     def enter_val(self,loc, data):
#         self.driver.find_element_by_name(loc).send_keys(data)
#
#     def click(self,loc):
#         self.driver.find_element_by_name(loc).click()


# # # --------------------------------------------Level 2 -- step 14---------------------------------------------------

from pages.LocGeneric import *

class WebGeneric(LocGeneric):
    def __init__(self, driver):
        # self.driver = driver
        LocGeneric.__init__(self, driver)

        global loc
        loc = LocGeneric(driver)

    def enter_val(self, loc_type, loc_val, data):
        # self.driver.find_element_by_name(loc).send_keys(data)
        loc.locator(loc_type, loc_val).send_keys(data)

    def click(self, loc_type, loc_val):
        # self.driver.find_element_by_name(loc).click()
        loc.locator(loc_type, loc_val).click()
