#!/usr/bin/env python
#coding:utf-8

from selenium.webdriver.common.keys import Keys
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import os
import time
import csv
'''

   
class ABC:    
    def login(self,a,b,c):
        
        a.find_element_by_link_text("登录").click()
        a.find_element_by_link_text("使用密码登录").click()
        a.find_element_by_id("login").clear()
        a.find_element_by_id("login").send_keys(b)
        a.find_element_by_id("password").clear()
        a.find_element_by_id("password").send_keys(c)
        a.find_element_by_id("login_submit").send_keys(Keys.ENTER)
        
        
