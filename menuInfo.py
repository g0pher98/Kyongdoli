# -*- coding: utf-8 -*-

from collections import OrderedDict

#side3
catbus = OrderedDict()
catbus['노선 & 시간표'] = {}
catbus['버스 노선도'] = {}
catbus['버스 시간표'] = {}

univ = OrderedDict()
univ['융합교양대학'] = {}
univ['휴먼인재융합대학'] = {}
univ['지식정보서비스대학'] = {}
univ['융합과학대학'] = {}
univ['창의공과대학'] = {}
univ['관광문화대학'] = {}

center = OrderedDict()
center['대학본부'] = {}
center['부속기관'] = {}
center['부설교육기관'] = {}
center['기타기관'] = {}

#deep2
weather = OrderedDict()
weather['전체 날씨'] = {}
weather['오늘 날씨'] = {}
weather['내일 날씨'] = {}

food = OrderedDict()
food['전체 학식'] = {}
food['이스퀘어'] = {}
food['감성코어'] = {}
food['교직원식당'] = {}
food['기숙사'] = {}

facilities = OrderedDict()
facilities['고양이 버스'] = catbus
facilities['증명서 발급기 위치'] = {}
facilities['프린터기 위치'] = {}
facilities['ATM기 위치'] = {}

contact = OrderedDict()
contact['대학 연락처'] = univ
contact['기관 연락처'] = center


#deep1
menu = OrderedDict()
menu['날씨'] = weather
menu['학식'] = food
menu['편의시설'] = facilities
menu['연락처'] = contact
menu['챗봇'] = {}
menu['문의'] = {}

def findMenuPath(input, dics):
    for i in dics:
        if dics[i] != {}:
            res = findMenuPath(input, dics[i])
            if res != []:
                return [i] + res
            else:
                if i == input:
                    return [i]
    if input in dics:
        return [input]
    else:
        return []
