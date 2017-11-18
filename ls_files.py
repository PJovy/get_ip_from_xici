# -*- coding: utf-8 -*-
# @Time    : 2017/11/18 14:14
# @Author  : Jovy
# @Site    : 
# @File    : test_os.py
# @Software: PyCharm Community Edition
import os


def ls_files(path=os.getcwd()): # list files in specific dir.(default current working directory)
    L = [file for file in os.listdir(path)]
    return L


def get_file(no):
    return ls_files()[int(no)-1]



if __name__ == '__main__':
    pass

