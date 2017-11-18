# -*- coding: utf-8 -*-
# @Time    : 2017/11/18 1:00
# @Author  : Jovy
# @Site    : 
# @File    : check_xici_ip.py
# @Software: PyCharm Community Edition
import requests

from ls_files import ls_files, get_file


# 检查代理IP是否可用
class xici_checker(object):
    def __init__(self, check_filename, result_filename, url):
        # check_filename是保存了待检查代理信息的txt文件，result_filename是检查后的代理信息txt文件，url是待检查的url
        self.check_filename = check_filename
        self.result_filename = result_filename
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/62.0.3202.89 Safari/537.36'
        }


    def check(self, proxy):
        try:
            requests.get(url=self.url, proxies=proxy, timeout=1, headers=self.headers)
        except Exception as e:
            print('失败：',e)
        else:
            self.write_to_file(proxy['http'] + '\n')


    def get_proxy(self):
        # 根据开始抓取的结果返回一个proxy (generator)
        with open(self.check_filename,'r',encoding='utf-8') as fr:
            for ip_port in fr.readlines():
                ip_port = ip_port.split('\t')
                proxy = {
                    'http': ip_port[0]+':'+ip_port[1]
                }
                yield proxy


    def write_to_file(self,content):
        with open(self.result_filename, 'a', encoding='utf-8') as fw:
                fw.writelines(content)



def main():
    print('当前目录下有以下文件或目录,请选择序号：')
    for no in range(len(ls_files())):
        print(str(no+1) + ':' + ls_files()[no])
    check_filename = get_file(input('请输入待检查ip文件所在序号：'))
    print(check_filename)
    result_filename = input('输入检查结果文件名：')
    url = 'https://www.lagou.com/'
    checker = xici_checker(check_filename=check_filename,result_filename=result_filename,url=url)
    for proxy in checker.get_proxy():
        checker.check(proxy)


if __name__ == '__main__':
    pass
