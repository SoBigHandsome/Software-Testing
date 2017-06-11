import unittest
import sys
import test_primepath

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
                data = map(int, line.split(','))
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
        i=0
        while(i<=14):
            pathName = path + '/answer'+str(i)+'.txt'
            answers = getAnswer(pathName)
            primePath = test_primepath.PrimePath()
            print(self.assertEqual(primePath.getPrimepath(i), answers))

if __name__ == "__main__":
    unittest.main()