# -*- coding: utf-8 -*-

import pdfkit
import os
import requests
from bs4 import BeautifulSoup
import time


# 获取标题列表
def get_title_list():
    soup = requests.get('http://www.yinwang.org')
    content = BeautifulSoup(soup.text,'html.parser')
    titles = []
    for text in content.find_all('li', 'list-group-item'):
        titles.append(text.a.string)
    return titles


# 获取所有页面url
def get_url_list():
    soup = requests.get('http://www.yinwang.org')
    content = BeautifulSoup(soup.text, 'html.parser')
    urls = []
    for li in content.find_all(class_='list-group-item'):
        urls.append("http://www.yinwang.org" + li.a.get('href'))
    return urls

# 将html页面保存到本地
def saveHtml(file_name, file_content):
    fp = open(file_name, "w+b")
    fp.write(file_content)
    fp.close()

# 将博客转化为pdf文件
def savePDF(url, file_name):
    options = {
        'page-size': 'A4',
        'zoom':'2.5'
    }
    pdfkit.from_url(url, file_name, options = options)

# 将当前所有文章url保存到文件里
def saveCurrUrList(urls, filename, mode = 'a'):
    file = open(filename,mode)
    for i in range(len(urls)):
        file.write(str(urls[i] + '\n'))
    file.close()

if __name__ == '__main__':
    urls = get_url_list()
    titles = get_title_list()
    start = 0
    end = len(urls)
    for i in range(start, end):
        soup = requests.get(urls[i])
        content = BeautifulSoup(soup.text, 'html.parser')
        saveHtml(os.getcwd() + '/html/' + titles[i] + '.html', content.encode())
        #savePDF(urls[i], os.getcwd() + '/pdf/' + titles[i] + ".pdf")
        print("第", i, "篇博客《", titles[i], "》成功保存!")




