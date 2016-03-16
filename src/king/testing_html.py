#!/usr/bin/env python
#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
import csv
from testing003 import ABC
import unittest
from HTMLTestRunner import HTMLTestRunner


class DEF(unittest.TestCase):#循环输出每一行信息
    def dingdan(self):
        data=csv.reader(open('D:\\data.csv','r'))
        for user in data:
            driver=webdriver.Firefox()
            
            driver.get("http://www.yongche.com")
            # 获得 cookie 信息
            cookie= driver.get_cookies()
            #将获得 cookie 的信息打印
            print cookie
            time.sleep(3)
            d=ABC()
            d.login(driver,user[0],user[1]) 
            data1=csv.reader(open('D:\\data1.csv','r'))
            for user1 in data1:
                driver.find_element_by_link_text("在线订车").click()
                driver.find_element_by_name("datetime").clear()
                driver.find_element_by_name("datetime").send_keys("2016-03-18") 
                driver.find_element_by_name("datetime").send_keys(Keys.TAB)
                driver.find_element_by_name('start_position').send_keys(user1[0])
        
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="start_position_dropNode"]/div[2]/ul[2]/li[2]/a').click()
                
                driver.find_element_by_name('end_position').send_keys(user1[1])
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="end_position_dropNode"]/div[2]/ul[2]/li[2]/a').click()
                driver.find_element_by_xpath('//*[@id="product_hour"]/div/div[4]/a/span/input').click()
                driver.find_element_by_xpath('//*[@id="main"]/div[1]/form/ul/li[1]/div[2]/p/span[2]').click()
                driver.find_element_by_xpath('//*[@id="fixed_submit"]/div[2]/div/input').click()   
        
if __name__ == '__main__':
    
    testunit = unittest.TestSuite()
    testunit.addTest(DEF("dingdan"))
    fp = open('D:\\result.html','wb')
    runner = HTMLTestRunner(stream=fp,title=u'易到用车下单',description=u'用例执行情况：')
    runner.run(testunit)
    fp.close()