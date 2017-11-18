# 西刺代理爬虫

## 主要是爬取西刺代理的HTTP代理

## 主要文件介绍以及使用方法：

- ### 爬虫主程序，xici_spider.py:
1. 定义xici_pider类
2. 初始化xiciSpider实例，需要两个参数：
- pages:总共需要爬取的页面数量，默认为2
- originipfile:将爬取到的信息导出来的文件名
3. crawl方法运行爬虫

- ### 检查ip是否可用，xici_checker.py:
1. 定义xici_checker类
2. 初始化实例，3个参数：
- check_filename:待检查的ip所在的txt文件全名，包含txt后缀
- result_filename:检查结果保存的文件全名，包含txt后缀
- url：待测试的url
3. check方法运行ip检查程序
