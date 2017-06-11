from selenium import webdriver
import unittest, time
from HTMLTestRunner import HTMLTestRunner



if __name__ == "__main__":
    
    testunit = unittest.TestSuite()
    testunit.addTest(Baidu("test_baidu_search"))

    # 按照一定格式获取当前时间
    now = time.strftime("%Y-%m-%d %H-%M-%S")

    # 定义报告存放路径
    # filename = './report/result.html'
    filename = './report-' + now + '-result.html'
    fp = open(filename, 'wb')

    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,                  # 指定测试报告文件
                        title='自动化测试报告',        # 定义测试报告标题
                        description='用例执行状况：')    # 定义测试报告副标题
    runner.run(testunit)    # 运行测试用例
    fp.close()  # 关闭报告文件