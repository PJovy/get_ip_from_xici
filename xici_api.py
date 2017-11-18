# -*- coding: utf-8 -*-
# @Time    : 2017/11/18 11:01
# @Author  : Jovy
# @Site    : 
# @File    : API_proxy.py
# @Software: PyCharm Community Edition
import random



class api_proxy(object):

    def __init__(self, filename):
        self.name = 'api_proxy'
        self.filename = filename
        self.L = self.get_proxy_list()

    def get_proxy_list(self):
        with open(self.filename,'r',encoding='utf-8') as fr:
            return fr.readlines()


    def get_proxy(self):
        return random.choice(self.L).strip()


def main():
    api = api_proxy('result.txt')
    print(api.get_proxy())



if __name__ == '__main__':
    pass