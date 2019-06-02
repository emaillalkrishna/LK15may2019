# # # --------------------------------------------Level 2 -- step 14--------------------------------------------------loc_val-

class LocGeneric:
    def __init__(self, driver):
        self.driver = driver

    def locator(self, loc_type, loc_val):
        try:
            if (loc_type == "name"):
                ele = self.driver.find_element_by_name(loc_val)
                return ele
            elif (loc_type == "id"):
                ele = self.driver.find_element_by_id(loc_val)
                return ele
            elif (loc_type == "classname"):
                ele = self.driver.find_element_by_class_name(loc_val)
                return ele
            elif (loc_type == "xpath"):
                ele = self.driver.find_element_by_xpath(loc_val)
                return ele
        except AssertionError as e:
            print("report fail")
        except:
            print("fail")
