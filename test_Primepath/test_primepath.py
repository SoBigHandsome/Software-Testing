#coding:utf-8
import copy
import os
import sys

class PrimePath:

    def __init__(self):
        self.graph = dict()
        self.simplePath = []
        self.primePath =[]

    def Init(self,fileName):
        path = os.path.dirname(__file__)
        filePath = path + "/" + fileName
        with open(filePath, 'r') as fr:
            i = 0
            for line in fr:
                if line[-1] == '\n':
                    line = line[:-1]
                if line.strip() != "":
                    line = line.strip().replace(' ', '')
                    if line != '-1':
                        #data = map(int, line.split(','))
                        data = line.split(',')
                        self.graph[str(i)] = data
                    else:
                        self.graph[str(i)] = []
                    i += 1
        return

    def Repeat(self,path, node):
        # 判断路径中是否有节点重复
        pathtemp = copy.deepcopy(path)
        if len(pathtemp) > 0:
            pathtemp.pop(0)
        while len(pathtemp) > 0:
            if pathtemp[0] == node:
                return True
            pathtemp.pop(0)
        return False

    def DFS(self,path, key):  # 深度优先遍历
        value = self.graph[key]
        for i in value:
            while self.Repeat(path, i) == False:
                path.append(i)
                self.simplePath.append(copy.deepcopy(path))
                if path[0] != i:
                    self.DFS(copy.deepcopy(path), i)
            while path[-1] != key:
                path.pop()
        path.pop()
        return



    def SimplePath(self):  # 用DFS生成simplepath
        for key in self.graph.keys():
            path = []
            path.append(key)
            self.simplePath.append(copy.deepcopy(path))
            self.DFS(copy.deepcopy(path), key)
            path.pop()
        return


    def PrimePath(self):  # 求primepath
        self.primePath = copy.deepcopy(self.simplePath)
        i = 0
        while (i != len(self.primePath)):
            for j in range(0, len(self.primePath)):
                flag = False
                if i == j:
                    pass
                else:
                    if ','.join(self.primePath[i]) in ','.join(self.primePath[j]):
                        del (self.primePath[i])
                        flag = True
                        break
            if flag == False:
                i += 1
            self.primePath = sorted(self.primePath, key=lambda a: (len(a), a))


    def getPrimepath(self):
        self.Init(r'case6.txt')
        #self.Init(r'case'+str(i)+'.txt')
        self.SimplePath()
        self.PrimePath()
        return self.primePath

if __name__ == '__main__':
    pm = PrimePath()
    pm.getPrimepath()