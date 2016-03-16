#!/usr/bin/env python
#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':

    driver = webdriver.Firefox()

    driver.get('http://www.baidu.com')
    print "浏览器最大化"
    driver.maximize_window() #将浏览器最大化显示
    driver.set_window_size(480, 800)
    driver.find_element_by_id('kw').send_keys('selenium')
    driver.find_element_by_id('kw').send_keys(Keys.ENTER)
