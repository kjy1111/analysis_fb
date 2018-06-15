# http test

# urllib 라이브러리는 Python에서 웹과 관련된 데이터를 쉽게 이용하게 도와주는 라이브러리입니다.
# Request() 웹을 열어서 데이터를 읽어오는 역할
# urlopen () 해당 URL을 열고 데이터를 얻을 수 있는 함수와 클래스 제공하며, HTTP 를 통해 웹 서버에 데이터를 얻는 데 많이 사용된다.​
# urlopen().read([nbytes]) : nbyte의 데이터를 바이트 문자열로 읽음

import sys
from urllib.request import Request, urlopen
from datetime import *

try:
    url = 'http://www.naver.com'
    request = Request(url)  # 현재 요청의 URL에 대한 정보를 가져옵니다.
    resp = urlopen(request)
    resp_body = resp.read().decode("utf-8")
    print(resp_body)
except Exception as e:
    print('%s %s' % (e, datetime.now()), file=sys.stdout)   # file=sys.stdout -> 작성 안해도 디폴트로 자동으로 작성


'''

System.out.println('Hello World')
write(0, "Hello World")


'''