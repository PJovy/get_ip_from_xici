# -*- coding: utf-8 -*-
# @Time    : 2017/11/18 14:14
# @Author  : Jovy
# @Site    : 
# @File    : test_os.py
# @Software: PyCharm Community Edition

import os

def ls_files(path=os.getcwd()):
    L = [file for file in os.listdir(path)]
    for i in range(len(L)):
        print(str(i+1)+'.' + L[i] + '\t' + '(' + os.path.join(path,L[i]) + ')')

if __name__ == '__main__':
    ls_files()

