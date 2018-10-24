

def bot(content):
    msg = {}
    answer = mean(content)
    msg['message'] = {'text': answer }
    return msg

def mean(content):
    return "챗봇 서비스 준비중입니다."