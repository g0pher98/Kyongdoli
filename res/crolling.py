# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
import datetime

def foodCrolling():
    #html 요청
    url = 'http://www.kyonggi.ac.kr/webRestMenu.kgu?mzcode=K00M04038500&restGb=suwon'
    cookie = {'JSESSIONID':'LLC5ii1WodtoW1o4gNKfNMoakEA0VjDTHISAwE799SncjDLj0vma3or9KX9BI0EQ.webwas_servlet_engine1'}
    res = requests.get(url, cookies=cookie)
    #soup 설정
    soup = BeautifulSoup(res.text,'lxml')
    base = soup.find_all('tbody',{'class' : 'text_center'})
    output("food_esquare.txt",foodMenu(base[0]))
    output("food_emotionalcore.txt",foodMenu(base[1]))
    output("food_schoolcafeteria.txt",foodMenu(base[2]))

def dormCrolling():
    #html 요청
    dt = datetime.datetime.now()
    url = "http://dorm.kyonggi.ac.kr/Khostel/mall_main.php"
    data = {}
    data['viewform'] = 'B0001_foodboard_view'
    data['board_no'] = 1
    weekpoint = dt - datetime.timedelta(days=dt.weekday())
    for i in range(6):
        data['food_at'] = (weekpoint + datetime.timedelta(days=i)).strftime("%Y-%m-%d")
        res = requests.get(url, params = data)
        soup = BeautifulSoup(res.text,'lxml', from_encoding='euc-kr')
        foods = soup.find_all('td',{'class':'padding-6'})
        #foods[0] 조식
        #foods[1] 중식
        #foods[2] 석식
        #foods[3] 운영시간

def foodMenu(raw):
    menu = OrderedDict()
    date = ''
    food = OrderedDict()
    for i in raw.find_all('tr'):
        if i.find('th') != None:
            if date != '':
                menu[date] = food
                food = {}
            date = getText(i.find('th'))
        td = i.find_all('td')
        food[getText(td[0])] = getText(td[1])
    menu[date] = food
    return menu

def getText(raw):
    raw = raw.get_text()
    raw = raw.replace('\t','')
    raw = raw.replace('\n','')
    raw = raw.replace('\r','')
    return raw

def output(filename,content):
    with open(filename, 'w') as f:
        for i in content:
            f.write('\n['+i.encode('utf-8')+']\n')
            for j in content[i]:
                if content[i][j] != ' ':
                    f.write('(밥)'+j.encode('utf-8')+'\n')
                    for k in content[i][j].replace(' ','').split('|'):
                        f.write('- '+k.encode('utf-8')+'\n')
                else :
                    f.write("- None\n")

def weatherCrolling():
    url = ""
    code = requests.get(url).test


#foodCrolling()
dormCrolling()