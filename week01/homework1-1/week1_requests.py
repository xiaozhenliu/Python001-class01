# 使用requests库获取猫眼电影前10热门，并保存为网页
# Created by Xiaozhen Liu. Edited on 2020/06/28 09:59 UTC+

import requests
from bs4 import BeautifulSoup as bs

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

header = {'user-agent':user_agent}

myurl = 'https://maoyan.com/films?showType=3'

response = requests.get(myurl,headers=header)

fname = 'maoyan_response.html'
with open(fname, 'w',encoding='utf-8') as file_object:
    file_object.write(response.text)

print(f'返回码是: {response.status_code}')