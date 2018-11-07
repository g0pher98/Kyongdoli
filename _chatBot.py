# -*- coding: utf-8 -*-

def bot(content):
    msg = {}
    answer = answer(mean(content))
    msg['message'] = {'text': answer }
    return msg

def mean(content):
    return {'type a':1, 'type b':2}

def answer(meaning):
    return "챗봇 서비스 준비중입니다."