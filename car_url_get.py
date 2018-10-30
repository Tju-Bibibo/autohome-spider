#coding==utf-8
import requests
import os
import re
from bs4 import BeautifulSoup

def htmlparser(url):#解析网页的函数
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    headers = {'User-agent': user_agent}#加上header伪装成浏览器防止被封
    r = requests.get(url, headers=headers)#get请求
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    content = r.text
    return content

def car_url_spider():
    begin_url = "https://car.autohome.com.cn/AsLeftMenu/As_LeftListNew.ashx?typeId=1%20&brandId=36%20&fctId=152%20&seriesId=0"
    content = htmlparser(begin_url)
    soup = BeautifulSoup(content,"html.parser")
    ul = soup.find_all("ul")
    li = soup.find_all("li")
    for i in li:
        h3 = i.find("h3")
        a = h3.find('a')
        car_url = a["href"]
        print(car_url)
        car_name = h3.get_text()
        print(car_name)
        dist ={}
        with open("car_url.txt",'a') as f:
            f.write(car_url+"\n")
        li = []
        with open("car_url_name.txt",'a',encoding="utf-8") as f:
            f.write(car_name+"\n")
        #写入中文字符老是出错,解决方案：with里面加了一个encoding=“utf-8”。
        #原因：car_name调用get_text()得到的是deccoding的unicode字符串
car_url_spider()
