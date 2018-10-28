# -*- coding:utf-8 -*-
import _chatBot
import _menuInfo


MSG_PREPARE = " 서비스 준비중입니다."
MSG_CHOICE = " 세부 메뉴를 선택해주세요."

def main(user_key, c_type, content):
    if c_type == 'text':
        path = _menuInfo.findMenuPath(content, _menuInfo.menu)
        if path != []:
            res = ps1Text(path)
        elif content[0] == '!':
            res = ps1Question(content)
        else:
            res = _chatBot.bot(content)
    else:
        res = ps1Photo()
    return res

# deep1(clear)
def ps1Text(path):
    if path[0] == '날씨':
        msg = ps2Weather(path)
    elif path[0] == '학식':
        msg = ps2Food(path)
    elif path[0] == '편의시설':
        msg = ps2Facilities(path)
    elif path[0] == '연락처':
        msg = ps2Contact(path)
    elif path[0] == '챗봇':
        msg = ps2Chatbot()
    elif path[0] == '문의':
        msg = ps2Question()
    else:
        print("텍스트인 경우 " + MSG_PREPARE)
    return msg
def ps1Question(text):
    msg = {}
    msg['message'] = {'text': '문의' + MSG_PREPARE}
    msg['keyboard'] = {
        'type' : 'buttons',
        'buttons' : list(_menuInfo.menu.keys())
    }
    return msg
def ps1Photo():
    msg = {}
    msg['message'] = {'text': '이미지' + MSG_PREPARE}
    msg['keyboard'] = {
        'type' : 'buttons',
        'buttons' : list(_menuInfo.menu.keys())
    }
    return msg

# deep2(clear)
def ps2Weather(path):
    msg = {}
    if len(path) < 2:
        msg['message'] = {'text': '날씨' +MSG_CHOICE}
        msg['keyboard'] = {
            'type' : 'buttons',
            'buttons' : list(_menuInfo.menu['날씨'].keys())
        }
    elif path[1] == '전체 날씨':
        msg = ps3AllWeather()
    elif path[1] == '오늘 날씨':
        msg = ps3WeatherToday()
    elif path[1] == '내일 날씨':
        msg = ps3WeatherTomorrow()
    return msg
def ps2Food(path):
    msg = {}
    if len(path) < 2:
        msg['message'] = {'text': '학식'+MSG_CHOICE}
        msg['keyboard'] = {
            'type' : 'buttons',
            'buttons' : list(_menuInfo.menu['학식'].keys())
        }
    elif path[1] == '전체 학식':
        msg = ps3AllFood()
    elif path[1] == '이스퀘어':
        msg = ps3Esquare()
    elif path[1] == '감성코어':
        msg = ps3EmotionalCore()
    elif path[1] == '교직원식당':
        msg = ps3SchoolCafeteria()
    elif path[1] == '기숙사':
        msg = ps3Dormitory()
    return msg
def ps2Facilities(path):
    msg = {}
    if len(path) < 2:
        msg['message'] = {'text': '편의시설' +MSG_CHOICE}
        msg['keyboard'] = {
            'type' : 'buttons',
            'buttons' : list(_menuInfo.menu['편의시설'].keys())
        }
    elif path[1] == '고양이 버스':
        msg = ps3catBus(path)
    elif path[1] == '증명서 발급기 위치':
        msg = ps3certificate()
    elif path[1] == '프린터기 위치':
        msg = ps3printer()
    elif path[1] == 'ATM기 위치':
        msg = ps3ATM()
    return msg
def ps2Contact(path):
    msg = {}
    if len(path) < 2:
        msg['message'] = {'text': '연락처' + MSG_CHOICE}
        msg['keyboard'] = {
            'type' : 'buttons',
            'buttons' : list(_menuInfo.menu['연락처'].keys())
        }
    elif path[1] == '대학 연락처':
        msg = ps3CallUniv(path)
    elif path[1] == '기관 연락처':
        msg = ps3CallCenter(path)
    return msg
def ps2Chatbot():
    msg = {}
    msg['message'] = {'text':'안녕하세요! 경돌이입니다.'}
    return msg
def ps2Question():
    msg = {}
    msg['message'] = {'text':'문의 내용 앞에 느낌표(!)를 붙여주셔야 반영됩니다.'}
    return msg

# deep3(clear)
def ps3AllWeather():
    msg = {}
    f1 = open("./res/weather_today.txt", 'r')
    f2 = open("./res/weather_tomorrow.txt", 'r')
    msg['message'] = {'text':f1.read().decode('cp949').encode('utf-8') + f2.read().decode('cp949').encode('utf-8')}
    msg['keyboard'] = {
        'type' : 'buttons',
        'buttons' : list(_menuInfo.menu.keys())
    }
    f1.close()
    f2.close()
    return msg
def ps3WeatherToday():
    msg = {}
    f = open("./res/weather_today.txt", 'r')
    msg['message'] = {'text':f.read().decode('cp949').encode('utf-8')}
    msg['keyboard'] = {
        'type' : 'buttons',
        'buttons' : list(_menuInfo.menu.keys())
    }
    f.close()
    return msg
def ps3WeatherTomorrow():
    msg = {}
    f = open("./res/weather_tomorrow.txt", 'r')
    msg['message'] = {'text':f.read().decode('cp949').encode('utf-8')}
    msg['keyboard'] = {
        'type' : 'buttons',
        'buttons' : list(_menuInfo.menu.keys())
    }
    f.close()
    return msg

def ps3AllFood():
    msg = {}
    f1 = open("./res/food_esquare.txt", 'r')
    f2 = open("./res/food_emotionalcore.txt", 'r')
    f3 = open("./res/food_schoolcafeteria.txt", 'r')
    f4 = open("./res/food_dormitory.txt", 'r')
    msg['message'] = {
        'text':
            "● E-스퀘어 ●\n" + f1.read().decode('utf-8').encode('utf-8') +
            "\n● 감성코어 ●\n" + f2.read().decode('utf-8').encode('utf-8') +
            "\n● 교직원식당 ●\n" + f3.read().decode('utf-8').encode('utf-8') +
            "\n● 기숙사 ●\n" + f4.read().decode('utf-8').encode('utf-8')
    }
    msg['keyboard'] = {
        'type' : 'buttons',
        'buttons' : list(_menuInfo.menu.keys())
    }
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    return msg
def ps3Esquare():
    msg = {}
    f = open("./res/food_esquare.txt", 'r')
    msg['message'] = {'text':f.read().decode('utf-8').encode('utf-8')}
    msg['keyboard'] = {
        'type' : 'buttons',
        'buttons' : list(_menuInfo.menu.keys())
    }
    f.close()
    return msg
def ps3EmotionalCore():
    msg = {}
    f = open("./res/food_emotionalcore.txt", 'r')
    msg['message'] = {'text':f.read().decode('utf-8').encode('utf-8')}
    msg['keyboard'] = {
        'type' : 'buttons',
        'buttons' : list(_menuInfo.menu.keys())
    }
    f.close()
    return msg
def ps3SchoolCafeteria():
    msg = {}
    f = open("./res/food_schoolcafeteria.txt", 'r')
    msg['message'] = {'text':f.read().decode('utf-8').encode('utf-8')}
    msg['keyboard'] = {
        'type' : 'buttons',
        'buttons' : list(_menuInfo.menu.keys())
    }
    f.close()
    return msg
def ps3Dormitory():
    msg = {}
    f = open("./res/food_dormitory.txt", 'r')
    msg['message'] = {'text':f.read().decode('utf-8').encode('utf-8')}
    msg['keyboard'] = {
        'type' : 'buttons',
        'buttons' : list(_menuInfo.menu.keys())
    }
    f.close()
    return msg

def ps3catBus(menu):
    msg={}
    if len(menu) < 3:
        msg['message'] = {'text':'고양이 버스'+ MSG_CHOICE}
        msg['keyboard'] = {
            'type' : 'buttons',
            'buttons' : list(_menuInfo.menu['편의시설']['고양이 버스'].keys())
        }
    elif menu[2] == '노선 & 시간표':
        msg = ps4MapNtime()
    elif menu[2] == '버스 노선':
        msg = ps4BusMap()
    elif menu[2] == '버스 시간표':
        msg = ps4BusTime()
    return msg
def ps3certificate():
    msg = {}
    f = open("./res/certificate.txt", 'r')
    msg['message'] = {'text':f.read().decode('cp949').encode('utf-8')}
    msg['keyboard'] = {
        'type' : 'buttons',
        'buttons' : list(_menuInfo.menu.keys())
    }
    f.close()
    return msg
def ps3printer():
    msg = {}
    f = open("./res/printer.txt", 'r')
    msg['message'] = {'text':f.read().decode('cp949').encode('utf-8')}
    msg['keyboard'] = {
        'type' : 'buttons',
        'buttons' : list(_menuInfo.menu.keys())
    }
    f.close()
    return msg
def ps3ATM():
    msg = {}
    f = open("./res/atm.txt", 'r')
    msg['message'] = {'text':f.read().decode('cp949').encode('utf-8')}
    msg['keyboard'] = {
        'type' : 'buttons',
        'buttons' : list(_menuInfo.menu.keys())
    }
    f.close()
    return msg

def ps3CallUniv(menu):
    msg={}
    if len(menu) < 3:
        msg['message'] = {'text':'대학 연락처' +MSG_CHOICE}
        msg['keyboard'] = {
            'type' : 'buttons',
            'buttons' : list(_menuInfo.menu['연락처']['대학 연락처'].keys())
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
def ps3CallCenter(menu):
    msg={}
    if len(menu) < 3:
        msg['message'] = {'text':'기관 연락처'+ MSG_CHOICE}
        msg['keyboard'] = {
            'type' : 'buttons',
            'buttons' : list(_menuInfo.menu['연락처']['기관 연락처'].keys())
        }
    elif menu[2] == '대학본부':
        msg = ps4Center1()
    elif menu[2] == '부속기관':
        msg = ps4Center2()
    elif menu[2] == '부설교육기관':
        msg = ps4Center3()
    elif menu[2] == '기타기관':
        msg = ps4Center4()
    return msg


# deep4
def ps4MapNtime():
    msg = {}
    f1 = open("./res/catbus_map.txt", 'r')
    f2 = open("./res/catbus_time.txt", 'r')
    msg['message'] = {'text':f1.read().decode('cp949').encode('utf-8') + f2.read().decode('cp949').encode('utf-8')}
    msg['keyboard'] = {
        'type' : 'buttons',
        'buttons' : list(_menuInfo.menu.keys())
    }
    f1.close()
    f2.close()
    return msg
def ps4BusMap():
    msg = {}
    f = open("./res/catbus_map.txt", 'r')
    msg['message'] = {'text':f.read().decode('cp949').encode('utf-8')}
    msg['keyboard'] = {
        'type' : 'buttons',
        'buttons' : list(_menuInfo.menu.keys())
    }
    f.close()
    return msg
def ps4BusTime():
    msg = {}
    f = open("./res/catbus_time.txt", 'r')
    msg['message'] = {'text':f.read().decode('cp949').encode('utf-8')}
    msg['keyboard'] = {
        'type' : 'buttons',
        'buttons' : list(_menuInfo.menu.keys())
    }
    f.close()
    return msg

def ps4Univ1():
    msg = {}
    f = open("./res/univ1.txt", 'r')
    msg['message'] = {'text':f.read().decode('cp949').encode('utf-8')}
    msg['keyboard'] = {
        'type' : 'buttons',
        'buttons' : list(_menuInfo.menu.keys())
    }
    f.close()
    return msg
def ps4Univ2():
    msg = {}
    f = open("./res/univ2.txt", 'r')
    msg['message'] = {'text':f.read().decode('cp949').encode('utf-8')}
    msg['keyboard'] = {
        'type' : 'buttons',
        'buttons' : list(_menuInfo.menu.keys())
    }
    f.close()
    return msg
def ps4Univ3():
    msg = {}
    f = open("./res/univ3.txt", 'r')
    msg['message'] = {'text':f.read().decode('cp949').encode('utf-8')}
    msg['keyboard'] = {
        'type' : 'buttons',
        'buttons' : list(_menuInfo.menu.keys())
    }
    f.close()
    return msg
def ps4Univ4():
    msg = {}
    f = open("./res/univ4.txt", 'r')
    msg['message'] = {'text':f.read().decode('cp949').encode('utf-8')}
    msg['keyboard'] = {
        'type' : 'buttons',
        'buttons' : list(_menuInfo.menu.keys())
    }
    f.close()
    return msg
def ps4Univ5():
    msg = {}
    f = open("./res/univ5.txt", 'r')
    msg['message'] = {'text':f.read().decode('cp949').encode('utf-8')}
    msg['keyboard'] = {
        'type' : 'buttons',
        'buttons' : list(_menuInfo.menu.keys())
    }
    f.close()
    return msg
def ps4Univ6():
    msg = {}
    # f = open("./res/univ6.txt", 'r')
    msg['message'] = {'text':'관광문화대학'+MSG_PREPARE}
    msg['keyboard'] = {
        'type' : 'buttons',
        'buttons' : list(_menuInfo.menu.keys())
    }
    # f.close()
    return msg

def ps4Center1():
    msg = {}
    # f = open("./res/catbus_time.txt", 'r')
    msg['message'] = {'text':'대학본부'+MSG_PREPARE}
    msg['keyboard'] = {
        'type' : 'buttons',
        'buttons' : list(_menuInfo.menu.keys())
    }
    # f.close()
    return msg
def ps4Center2():
    msg = {}
    # f = open("./res/catbus_time.txt", 'r')
    msg['message'] = {'text':'부속기관'+MSG_PREPARE}
    msg['keyboard'] = {
        'type' : 'buttons',
        'buttons' : list(_menuInfo.menu.keys())
    }
    # f.close()
    return msg
def ps4Center3():
    msg = {}
    # f = open("./res/catbus_time.txt", 'r')
    msg['message'] = {'text':'부설교육기관'+MSG_PREPARE}
    msg['keyboard'] = {
        'type' : 'buttons',
        'buttons' : list(_menuInfo.menu.keys())
    }
    # f.close()
    return msg
def ps4Center4():
    msg = {}
    # f = open("./res/catbus_time.txt", 'r')
    msg['message'] = {'text':'기타기관'+MSG_PREPARE}
    msg['keyboard'] = {
        'type' : 'buttons',
        'buttons' : list(_menuInfo.menu.keys())
    }
    # f.close()
    return msg

