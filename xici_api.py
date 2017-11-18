# -*- coding: utf-8 -*-
# @Time    : 2017/11/18 11:01
# @Author  : Jovy
# @Site    : 
# @File    : API_proxy.py
# @Software: PyCharm Community Edition
import random



class API_proxy(object):

    def __init__(self):
        self.name = API_proxy

    def get_proxy(self):
        with open('proxies_extract_checked.txt') as fr:
            proxy = random.choice(fr.readlines())
            return proxy.strip()

def main():
    pass



if __name__ == '__main__':
    main()