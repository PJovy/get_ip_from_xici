# -*- coding: utf-8 -*-
# @Time    : 2017/11/18 1:00
# @Author  : Jovy
# @Site    : 
# @File    : check_xici_ip.py
# @Software: PyCharm Community Edition
import requests


# 检查代理IP是否可用



def get_proxy(filename):
    # 初始抓取ip(未检查)的生成器，方便后面遍历调用检查

    with open(filename,'r',encoding='utf-8') as fr:
        for ip_port in fr.readlines():
            proxy = {
                'http':ip_port.strip()
            }
            yield proxy

def check_ip(proxy,url,outfilename):
    # 根据传入IP，进行判断后返回相应值，可用返回200，不可用返回None
    myheaders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
    }
    try:
        requests.get(url=url, proxies=proxy, timeout=1,headers=myheaders)
    except Exception as e:
        print(e)
    else:
        write_to_file(proxy['http']+'\n',outfilename)


def write_to_file(content,outfilename):
    with open(outfilename, 'a', encoding='utf-8') as fw:
            fw.writelines(content)

def main():
    filename = input("待测试ip的文件名：")
    outfilename = input("输出测试结果的文件名：")
    url = input('要测试的网址：')
    for ip in get_proxy(filename):
        check_ip(ip,url,outfilename)



if __name__ == '__main__':
    main()
