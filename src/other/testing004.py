#!/user/bin/env python
#encoding:utf-8

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class 11111(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://testing.sso.backend.yongche.org/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_11111(self):
        driver = self.driver
        driver.get(self.base_url + "/auth/login?done=http%3A%2F%2Ftesting.sso.backend.yongche.org%2F")
        driver.find_element_by_id("J_login").clear()
        driver.find_element_by_id("J_login").send_keys("jinzongjie")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("Zaq12345")
        driver.find_element_by_css_selector("input.x-submit").click()
        driver.find_element_by_css_selector("div.icon.icon-erp").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | content | ]]
        driver.find_element_by_id("cellphone").clear()
        driver.find_element_by_id("cellphone").send_keys("16891919004")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
