# coding:utf-8
import requests
import webbrowser
import time
# api指定了follow的这个人star的所有项目，该用户是kennethreitz
api = "https://api.github.com/users/kennethreitz/starred"
# 先访问一次api，获取star列表
info = requests.get(api).json()
starred = []
# 将star列表中的项目id存到list变量中
for i in info:
    starred.append(i['id'])

while True:
    # 获取star的项目
    info = requests.get(api).json()
    for i in info:
        # 如果当前项目id在list变量中不存在，则说明是刚刚star的项目
        if not i['id'] in starred:
            starred.append(i['id'])
            # 获取项目名称
            repo_name = i['name']
            # 获取作者名称
            owner = i['owner']['login']
            # 在浏览器中打开项目
            web_page = "https://github.com/" + owner + "/" + repo_name
            webbrowser.open(web_page)
    # 每隔600秒（10分钟）检查一次
    time.sleep(600)