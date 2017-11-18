# -*- coding: utf-8 -*-
# @Time    : 2017/11/17 23:45
# @Author  : Jovy
# @Site    :
# @File    : new.py
# @Software: PyCharm Community Edition
import requests
from bs4 import BeautifulSoup


class xiciSpider(object):
    # 初始化
    # myheaders信息,需要自定义
    # 总共需要爬取的页面数量，默认为2
    def __init__(self,pages=2, originipfile='originipfile'):
        self.pages = pages
        self.originipfile = originipfile


    # 爬取具体页码的ip信息
    def get_html(self, page):
        myheaders = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/62.0.3202.89 Safari/537.36'
        }
        s = requests.Session()
        xici_url = 'http://www.xicidaili.com/wt/{}'.format(page)
        html = s.get(url=xici_url, headers=myheaders).text
        return html


    # 返回一个代理信息的list，每个tr都是一个完整的代理信息，包括ip，端口，协议等
    # 用yield返回一个代理信息生成器，在后面的方法调用的时候，降低内存占用
    def get_ips(self, html):
        soup = BeautifulSoup(html, 'lxml')
        trs = soup.find_all('tr', class_=True)
        for tr in trs:
            yield [td.string.strip() for td in tr if td.string is not None]


    # 将内容写入txt文件的方法
    def write_to_file(self,originipfile,content):
        with open('{}.txt'.format(originipfile), 'a', encoding='utf-8') as fw:
            fw.writelines(content)


    # 汇总方法，遍历，将所有的我们需要的ip信息抓取并写入txt
    def make_original_proxies_txt(self):
        for page in range(1, self.pages+1):
            for ip in self.get_ips(self.get_html(str(page))):
                for info in ip[2:len(ip)-1]:
                    if info is ip[len(ip)-2]:
                        self.write_to_file(self.originipfile, info + '\n')
                    elif info is not '':
                        self.write_to_file(self.originipfile, info + '\t')


def crawl_xici():
    pages = int(input('请输入你需要爬取的总页数(默认抓2页)：'))
    originipfile = input('请输入保存的txt文件名：')
    print("starting crawl......")
    spider = xiciSpider(pages=pages,originipfile=originipfile)
    spider.make_original_proxies_txt()
    print("finish crawl......")


def main():
    crawl_xici()


if __name__ == '__main__':
    main()
