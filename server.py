# -*- coding: utf-8 -*-

import os
from main import *
from flask import Flask, request, jsonify, render_template

''' 식별 변수
app_key
플러스 친구에서 자옹등답을 위한 앱 등록시 프로필별로 발급되는 고유 키값
app_secret
인증을 위해 app_key와 조합하여 사용되는 키 값
user_key
이용자를 구분하기 위한 key
'''

''' 오브젝트
keyboard
	type :
		buttons -> 객관식 응답
		text -> 주관식 응답
	buttons : Array[String] -> 객관식 응답의 목록

message
	text : -> 사용자에게 발송될 메시지 텍스트(100자이내)
	photo : -> 말풍선에 들어갈 이미지 1장(jpeg/png)
		url : 이미지
		width : 너비
		height : 높이
	message_button : -> 말풍선에 붙는 링크버튼 정보
		label : 링크버튼 타이틀
		url : 링크버튼 연결 주소
	
'''

app = Flask(__name__)

#사용자가 채팅방에 들어올 때
#return { 'type' : type, 'buttons' : [menu1,menu2,...] }
@app.route('/keyboard', methods=['GET'])
def mainMenu():
	msg = {}
	msg['type'] = 'buttons'
	msg['buttons'] = list(menuInfo.menu.keys())
	return jsonify(msg)

#사용자가 메시지를 보냈을 때
#return { 'message' : {}, 'keyboard' : {}}
@app.route('/message', methods=['POST'])
def userMsg():
	data = request.get_json()
	user_key = data['user_key'].encode('utf-8')
	c_type = data['type'].encode('utf-8')
	content = data['content'].encode('utf-8')
	return jsonify(main(user_key, c_type, content))

#사용자가 친구 추가를 했을 때
@app.route('/friend', methods=['POST'])
def addFriend():
	data = request.get_json()
	user_key = data['user_key']
	return 0
#사용자가 친구 삭제를 했을 때
@app.route('/friend', methods=['DELETE'])
def delFriend():
	data = request.get_json()
	user_key = data['user']
	return 1

#사용자가 채팅방을 삭제했을 때
@app.route('/chat_room', methods=['DELETE'])
def delChatroom():
	data = request.get_json()
	user_key = data['user']
	return 2

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)

