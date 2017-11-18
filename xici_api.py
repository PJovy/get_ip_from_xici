# -*- coding: utf-8 -*-
# @Time    : 2017/11/18 11:01
# @Author  : Jovy
# @Site    : 
# @File    : API_proxy.py
# @Software: PyCharm Community Edition
import random

from funcs import ls_files, get_file


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
    print('当前目录下有以下文件或目录,请选择序号：')
    for no in range(len(ls_files())):
        print(str(no+1) + ':' + ls_files()[no])
    check_filename = get_file(input('请输入待检查ip文件所在序号：'))
    api = api_proxy(check_filename)
    api.get_proxy()



if __name__ == '__main__':
    pass