# test json

# JSON 라이브러리를 사용하면, Python 타입의 Object를 JSON 문자열로 변경할 수 있으며(JSON 인코딩),
# 또한 JSON 문자열을 다시 Python 타입으로 변환할 수 있다 (JSON 디코딩)

# JSON 인코딩: Python Object (Dictionary, List, Tuple 등) 를 JSON 문자열로 변경하는 것
# JSON 디코딩: JSON 문자열을 Python 타입 (Dictionary, List, Tuple 등) 으로 변경하는 것




import sys
from urllib.request import Request, urlopen
from datetime import *
import json

try:
    url = 'http://kickscar.cafe24.com:8080/myapp-api/api/user/list'
    request = Request(url)
    resp = urlopen(request)
    resp_body = resp.read().decode("utf-8")
    print(type(resp_body), ":", resp_body)

    json_result = json.loads(resp_body)
    print(type(json_result), ":", json_result )

    data = json_result['data']
    print(type(data), ":", data)
except Exception as e:
    print('%s %s' % (e, datetime.now()), file=sys.stderr)