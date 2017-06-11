#coding:utf-8
import unittest

class TestBdd(unittest.TestCase):
    def setUp(self):
        print("test TestBdd :")

    def test_ccc(self):
        print("test ccc")

    def test_aaa(self):
        print("test aaa")

    def tearDown(self):
        pass

class TestAdd(unittest.TestCase):
    def setUp(self):
        print("test TestAdd :")

    def test_bbb(self):
        print("test bbb")

    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()