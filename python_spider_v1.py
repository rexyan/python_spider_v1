#-*-coding:utf-8 -*-
#---------------------------------------
#   程序：智联招聘爬虫
#   版本：1.0
#   作者：rexyan
#   日期：2016-5-20
#   语言：Python 3
#   操作：输入相关职业
#   功能：在电脑的C:/py/sipder下生成三个文件夹，保存城市,公司名,工资
#---------------------------------------

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import os

def spider(jobname):
    n=0
    citydata=[]
    companydata=[]
    salarydata=[]

    while n<99:
        n+=1
        url='http://sou.zhaopin.com/jobs/searchresult.ashx?jl=none&kw='+jobname+'&sb=1&sm=0&p='+str(n)+'&isfilter=0&fl=489&isadv=0'
        print("爬虫1号正在努力跳转下一个链接")
        print(url)
        request=urlopen(url)
        result=BeautifulSoup(request)
        company=result.findAll("td",{"class":{"gsmc"}})
        salary=result.findAll("td",{"class":{"zwyx"}})
        city=result.findAll("td",{"class":{"gzdd"}})
        i,j,l=0,0,0
        for companyname in company:
            print (companyname.get_text())
            i+=1
            print (i)
            companydata.append(companyname.get_text())

        for salary1 in salary:
            print (salary1.get_text())
            j += 1
            print(j)
            salarydata.append(salary1.get_text())

        for city1 in city:
            print(city1.get_text())
            l += 1
            print(l)
            citydata.append(city1.get_text())

    print(citydata)
    for x in citydata:
        with open("C:/py/spider/citydata.txt", 'a') as k:
            k.write(x)
            k.write('\n')

    print(companydata)
    for y in companydata:
        with open("C:/py/spider/companydata.txt", 'a') as k:
            k.write(y)
            k.write('\n')

    print(salarydata)
    for z in salarydata:
        with open("C:/py/spider/salarydata.txt", 'a') as k:
            k.write(z)
            k.write('\n')

def main():
    print("这是关于爬虫1号的说明，只出现一次，请仔细阅读：")
    print("1，本次抓取为智联招聘网站")
    print("2，你可自定义抓取的工作名称")
    print("3，本爬虫默认从智联招聘的第一页开始出发，99页结束")
    print("4，若智联招聘网站发生变动，则爬虫1号无法爬取")

    name=["python","java","ios","php","web","c++","android","c",".net"]
    for x in name:
        print (x)
        func=spider(x)
        with open("C:/py/spider/citydata.txt", 'a') as k:
            k.write('========以上是========='+x+'=========的信息=========')
            k.write('\n')
        with open("C:/py/spider/companydata.txt", 'a') as k:
            k.write('========以上是========='+x+'=========的信息=========')
            k.write('\n')
        with open("C:/py/spider/salarydata.txt", 'a') as k:
            k.write('========以上是========='+x+'=========的信息=========')
            k.write('\n')
        print ('爬虫上一个任务已完成')


if __name__=='__main__':
    main()