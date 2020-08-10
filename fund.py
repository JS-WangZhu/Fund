#!/usr/bin/env python
# coding: utf-8
# author: JS-WangZhu


# 查询具体基金

import os
import pickle
import requests
from bs4 import BeautifulSoup
import re
import prettytable as pt

# 获取所有基金信息
def get_allinfo():
    url = 'http://fund.eastmoney.com/allfund.html'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER'}
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.content, 'lxml',from_encoding="gb18030")
    all_info = soup.find_all('ul', class_='num_right')

    fund_info = [[],[],[]]
    for e in all_info:
        el = e.find_all('a')
        for single in el:
            try:
                s_url = single['href']
                s_text = single.get_text()
                number = s_text.split('）')[0][1:]
                name = s_text.split('）')[1]
            except:
                continue
            fund_info[0].append(number)
            fund_info[1].append(name)
            fund_info[2].append(s_url)

    pickle.dump(fund_info,open('fund_info.pkl','wb'))
    

if os.path.exists('./fund_info.pkl'):
    fund_info = pickle.load(open('fund_info.pkl','rb'))
#     print('INFO--基金信息缓存导入成功')
else:
    print('正在创建基金信息表')
    get_allinfo()
    print('INFO--基金信息表创建成功')
    fund_info = pickle.load(open('fund_info.pkl','rb'))
    print('INFO--基金信息缓存导入成功')


# 获取净值和估值 
def get_value(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER'}
    proxies={'http':'http://113.195.20.205:9999','http':'http://123.55.102.44:9999'}
    #res = requests.get(url,headers=headers,proxies=proxies)
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser',from_encoding="gb18030")
    dataOfFund = soup.find_all('div', class_='dataOfFund')
    guzhi = dataOfFund[0].select('#gz_gszzl')[0].get_text()
    gutime = dataOfFund[0].select('#gz_gztime')[0].get_text()[4:-1]

    jing = dataOfFund[0].find_all('span',class_='ui-font-middle')[4]
    jingzhi = jing.get_text()

    jingzhi_t = soup.find_all('dl', class_='dataItem02')
    jingtime = re.findall('\</span>(.*?)\)',str(jingzhi_t[0]))[0][14:]
    return guzhi,gutime,jingzhi,jingtime

def getUrl(no):
    ind = 0
    for index in range(len(fund_info[0])):
        if str(fund_info[0][index])==str(no):
            ind = index
    return fund_info[1][ind],fund_info[2][ind]

        

if os.path.exists('./my.txt'):
    f = open('./my.txt','r')
    tb = pt.PrettyTable()
    tb.field_names = ["基金代码", "基金名称", "估值", "估值更新", "净值", "净值更新"]
    tb.padding_width = 1

    content = f.readlines()
    for i in content:
        if str(i).endswith('\n'):
            i = i[:-1]
        tmpName,tmpUrl = getUrl(str(i))
        try:
            guzhi,gutime,jingzhi,jingtime = get_value(tmpUrl)
        except:
            continue
        
        tb.add_row([i,tmpName,guzhi,gutime,jingzhi,jingtime])
    tb.reversesort = True
    print(tb)
    
else:
    print('请在执行目录下创建my.txt,并按格式写入内容')
    print('格式：每行填写一个基金号码,结尾不留空行,以utf-8编码保存')
    print('创建成功后请重新执行此程序')




