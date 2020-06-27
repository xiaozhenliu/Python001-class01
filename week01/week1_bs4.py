import requests
from bs4 import BeautifulSoup as bs

fname = 'maoyan_response.html'

f = open(fname, 'r', encoding='utf-8')
response = f.read()

bs_info = bs(response, 'html.parser')

movieinfo = bs_info.find("div",class_="movies-list")
movie_hover = movieinfo.find_all("div",class_="movie-hover-title")

top10 = 'maoyan_top10.csv'
with open(top10, 'w',encoding='utf-8-sig') as file_object:
    file_object.write("电影名称,电影类型,上映时间"+'\n')
    for line in range(40):
        info = movie_hover[line].get_text() #获取鼠标移到电影上时显示的信息
        if line%4 == 0: # 电影名称
            file_object.write(info.split()[0]+',')
        if line%4 == 1: # 电影类型
            file_object.write(info.split()[1]+',') 
        if line%4 == 3: # 上映时间
            file_object.write(info.split()[1]+'\n')  
