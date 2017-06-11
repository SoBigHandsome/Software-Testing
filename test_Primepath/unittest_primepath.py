# encoding=utf-8
import unittest,time
import sys
import test_primepath
from HTMLTestRunner import HTMLTestRunner


def getAnswer(filePath):
    with open(filePath, 'r') as fr:
        answers = []
        for line in fr:
            if line[-1] == '\r\n' or line[-1]=='\n':
                line = line[:-1]
            line = line[1:-1]
            if line[-1]==']':
                line=line[:-1]
            if line.strip() != "":
                line = line.strip().replace(' ','')
                data = line.split(',')
                answers.append(list(data))
    answers = sorted(answers, key = lambda a:(len(a),a))
    return answers

class Testprime(unittest.TestCase):

    def setUp(self):
        print("test case start")
    def tearDown(self):
        print("test case end")
    def test_prime(self):
        path = sys.path[0]
        pathName = path + '/answer6.txt'
        answers = getAnswer(pathName)
        primePath = test_primepath.PrimePath()
        print(self.assertEqual(primePath.getPrimepath(), answers))
if __name__ == "__main__":
    #unittest.main()

    testunit = unittest.TestSuite()
    testunit.addTest(Testprime("test_prime"))
    # 按照一定格式获取当前时间
    now = time.strftime("%Y-%m-%d %H-%M-%S")

    # 定义报告存放路径
    # filename = './report/result.html'
    filename = './report-Testprime' + now + '-result.html'
    fp = open(filename, 'wb')

    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,  # 指定测试报告文件
                            title='自动化测试报告',  # 定义测试报告标题
                            description='用例执行状况：')  # 定义测试报告副标题
    reload(sys)
    sys.setdefaultencoding('utf8')
    runner.run(testunit)
    # 运行测试用例
    fp.close()  # 关闭报告文件