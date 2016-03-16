#!/usr/bin/env python
#coding:utf-8

from selenium import webdriver

if __name__ == '__main__':

    browser = webdriver.Firefox()

    browser.get('http://www.baidu.com')
    attribute=browser.find_element_by_id("kw").get_attribute('type')
    print attribute
    result=browser.find_element_by_id("kw").is_displayed()
    print result
