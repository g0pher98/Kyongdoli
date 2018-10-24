# -*- coding: utf-8 -*-
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
contents = {}
#deep4
#deep3
#deep2
contents['대학 연락처']=['융합교양대학', '휴먼인재융합대학', '지식정보서비스대학', '융합과학대학', '창의공과대학', '관광문화대학']
contents['기관 연락처']=['대학본부', '부속기관', '부설교육기관', '기타기관']
contents['고양이 버스']=['노선 & 시간표', '버스 노선', '버스 시간표']
#deep1
contents['날씨'] = ['전체 날씨', '오늘 날씨', '내일 날씨']
contents['학식'] = ['전체 학식', '이스퀘어', '감성코어', '교직원식당', '기숙사']
contents['편의시설'] = ['고양이 버스', '증명서 발급기 위치', '프린터기 위치', 'ATM기 위치']
contents['연락처'] = ['대학 연락처', '기관 연락처']
contents['문의'] = ['건의사항', '오류신고']


def response(user_key, c_type, content):
	if c_type == 'text':
		res = ps1Text(content)
	else :
		res = psPhoto()
	return res

def ps1Text(content):
	menu = findMenu(content)
'''
	if content in contents:
		keyboard = { 'type' : 'buttons', 'buttons' : contents[content] }
	else :
		keyboard = buttons()
'''
	if menu[0] == '날씨':
		msg = ps2Weather()
	elif menu[0] == '학식':
		msg = ps2Food()
	elif menu[0] == '편의시설':
		msg = ps2Facilities(menu)
	elif menu[0] == '연락처':
		msg = ps2Contact()
	elif menu[0] == '챗봇':
		msg = ps2Chatbot()
	elif menu[0] == '문의':
		msg = ps2Question()
	else:
		print("요거는 텍스트인 경우")
'''
	res = {
		'message' : { 'text' : msg },
		'keyboard' : keyboard
	}
'''
	return msg

def ps2Weather():
	f = open("./info/weather", 'r')
	msg = {
		'message':
		{
			'text':f.read()
		},
		'keyboard': 
			buttons()
	}
	return f.read()

def ps2Food():
	f = open("./info/food", 'r')
	msg = {
		'message':
		{
			'text':f.read()
		}, 
		'keyboard' : buttons()
	}
	return f.read()

def ps2Facilities(menu):
	if len(menu) < 2 :
		msg = {
			'message':
			{
				'text':'편의시설 세부 메뉴를 선택해주세요'
			},
			'keyboard' : contents['편의시설']
		}
	elif menu[1] == '고양이 버스':
		msg == ps3catBus(menu)
	elif menu[1] == '증명서 발급기 위치':
		msg == ps3certificate()
	elif menu[1] == '프린터기 위치':
		msg == ps3printer()
	elif menu[1] == 'ATM기 위치':
		msg == ps3ATM()
	return msg

def ps3catBus(menu):
	if len(menu) < 3:
		msg = {
			'message':
			{
				'text' : '고양이 버스 세부 메뉴를 선택해주세요'
			},
			'keyboard' : contents['고양이 버스']
		}
	elif menu[2] == '노선 & 시간표':
		msg = ps4wayNtime()
	elif menu[2] == '버스 노선':
		msg = ps4busWay()
	elif menu[2] == '버스 시간표':
		msg = ps4busTime()
	return msg

def ps4wayNtime():
	return "노선 & 시간표"
def ps4busWay():
	return "버스 노선"
def ps4busTime():
	return "버스 시간표"


def ps3certificate():
	return "증명서 발급기 위치"
def ps3printer():
	return "프린터기 위치"
def ps3ATM():
	return "ATM기 위치"

def ps2Contact():
	if len(menu) < 2:
		msg = {
			'message':
			{
				'text' : '연락처 세부 메뉴를 선택해주세요'
			},
			'keyboard': contents['연락처']
		}
	elif menu[1] == '대학 연락처':
		msg = ps3CallUniv()
	elif menu[1] == '기관 연락처':
		msg = ps3CallCenter()
	return msg

def ps3CallUniv():
	if len(menu) < 3:
		msg = {
			'message':
			{
				'text' : '대학 연락처 세부 메뉴를 선택해주세요'
			},
			'keyboard': contents['대학 연락처']
		}
	elif menu[2] == '융합교양대학':
		msg = ps4Univ1()
	elif menu[2] == '휴먼인재융합대학':
		msg = ps4Univ2()
	elif menu[2] == '지식정보서비스대학':
		msg = ps4Univ3()
	elif menu[2] == '융합과학대학':
		msg = ps4Univ4()
	elif menu[2] == '창의공과대학':
		msg = ps4Univ5()
	elif menu[2] == '관광문화대학':
		msg = ps4Univ6()
	return msg

def ps4Univ1():
def ps4Univ2():
def ps4Univ3():
def ps4Univ4():
def ps4Univ5():
def ps4Univ6():

def ps2Question():
	if len(menu) < 2:
		msg = {
			'message':
			{
				'text' : '문의 세부 메뉴를 선택해주세요'
			},
			'keyboard': contents['문의']
		}
	elif menu[1] == '건의사항':
		msg = ps3Feedback()
	elif menu[1] == '오류신고':
		msg = ps3Bug()
	return msg

def ps3Feedback():
def ps3Bug():

def findMenu(content):
	content = [content]
	for i in contents:
		if content[0] in contents[i]:
			content = [i]+ content
	return content

def psPhoto():
	res = {
		'message' : { 'text' : 'psPhoto() 서비스 준비중입니다' },
		'keyboard' : buttons()
	}
	return res

def buttons():
	data = {
		'type' : 'buttons',
		'buttons' : ['날씨', '학식', '편의시설', '연락처', '챗봇', '문의']
	}
	return data



'''
def response(menu):
	menu = menu.encode('utf-8')
	w=["학교 날씨"]
	f=["오늘의 학식"]
	b=["고양이 버스"]
	res = {}
	if menu in w:
		res = weather(menu)
	elif menu in f:
		res = food(menu)
	elif menu in b:
		res = bus(menu)
	else:
		res = {
			"message" : {"text" : "이해하지 못함"},
			"keyboard" : buttons()
		}
	return res	

def buttons():
	data = {
		"type" : "buttons",
		"buttons" : [
			"학교 날씨",
			"오늘의 학식",
			"고양이 버스"
		]
	}
	return data


def weather(menu):
	data={}
	f=open("./info/weather",'r')
	data['message'] = {'text' : f.read()}
	data['keyboard'] = buttons()
	f.close()
	return data

def food(menu):
	data={}
	f=open("./info/food",'r')
	data['message']={'text' : f.read()}
	data['keyboard'] = buttons()
	f.close()
	return data


def catBusTime() :
    yeonmu = '연무동\n08:30\n08:30\n08:35\n08:40\n08:45\n08:50\n08:55\n09:50\n11:30\n11:40\n11:50\n11:30\n11:40\n11:50\n\n'
    kwangkyo = '광교(경기대)\n11:30\n11:40\n11:50\n11:30\n11:40\n11:50\n13:30\n13:45\n\n'
    dormitory = '기숙사\n08:30\n08:35\n08:40\n08:45\n08:50\n08:55\n09:50\n11:30\n11:40\n11:50\n13:30\n13:40\n13:50\n'
    
    return yeonmu + kwangkyo + dormitory

def catBusRouteMap() :
    yeonmu = '● 연무동\nㅣ\n● 경기탑\nㅣ\n● 종합강의동\nㅣ\n● 제2공학관\n\n\n\n'
    kwangkyo = '● 광교역\nㅣ\n● 테니스장\nㅣ\n● 경기탑\nㅣ\n● 종합강의동\nㅣ\n● 제2공학관\n\n\n\n'
    dormitory = '● 기숙사 사거리\nㅣ\n● 정문\nㅣ\n● 텔레컨벤션센터\n'

    return yeonmu + kwangkyo + dormitory

def catBusAllPrint() :
    allView = catBusTime() + '\n\n\n\n' + catBusRouteMap()
    return allView

def bus(menu):
	data={}
	data['message'] = {'text':catBusAllPrint()}
	data['keyboard'] = buttons()
	return data

'''
