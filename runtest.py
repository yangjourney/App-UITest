# coding=utf-8

import os
import time
import unittest
import HTMLTestRunner
from common.sendEmail import send_email
from Case.Login import LoginTest
from Case.BackHome import DemoTest

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

def testsuit():
    suite = unittest.TestSuite()
    suite.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(LoginTest), ])
    suite.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(DemoTest), ])

    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    filename = 'D:\\Study-Appium\\report\\' + now + "Myreport.html"
    # filename = '/Users/xintudoutest/github/Appium/report/' + now + "Myreport.html"
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'测试用例结果', tester=u'宇宙超级无敌大圈圈')
    runner.run(suite)
    fp.close()

def email():
    send_email()

if __name__ == "__main__":

    testsuit()
    email()

