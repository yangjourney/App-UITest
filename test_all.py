#coding=utf-8
import unittest
import HTMLTestRunner
import time
import sys

#解决htmltestrunner中显示乱码的问题
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

#注意使用套件时，在单个py文件中下的多个用例用  (类名（"方法名")),
#导入多个py的类下，用（py名.类名）


all_case = '/Users/xintudoutest/appium/AppiumUI/all_test_case'
def CreateSuite():                                                        #产生测试套件
    test_suite = unittest.TestSuite()                                     #使用discover找出用例文件夹下all_test_case的所有用例
    discover = unittest.defaultTestLoader.discover(all_case,              #查找的文件夹路径
    pattern = 'ios_*.py', top_level_dir=None)                             #要测试的模块名，以start开头的.py文件
                                                                          #测试模块的顶层目录，即测试用例不是放在多级目录下，设置为none

    for suite in discover:  #使用for循环出suite,再循环出case
        for case in suite:
            test_suite.addTests(case)
            print test_suite
    return test_suite


#下面语句用来生成测试报告
all_case_names = CreateSuite()
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
filename = '/Users/xintudoutest/appium/AppiumUI/report/'+now+"Myreport.html"
fp = file(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'测试用例结果', tester=u'宇宙超级无敌大圈圈')
runner.run(all_case_names)
fp.close()
