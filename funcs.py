# -*- coding: utf-8 -*-
# @Time    : 2017/11/18 14:14
# @Author  : Jovy
# @Site    : 
# @File    : test_os.py
# @Software: PyCharm Community Edition
import os
import re




def ls_files(path=os.getcwd()): # list files in specific dir.(default current working directory)
    L = [file for file in os.listdir(path)]
    return L


def get_file(no):
    return ls_files()[int(no)-1]


def get_url(msg):
    url = input(msg)
    pattern = re.compile('(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]')
    if pattern.match(url):
        return url
    else:
        return '输入有误'










if __name__ == '__main__':
    print(get_url('输入网址:'))