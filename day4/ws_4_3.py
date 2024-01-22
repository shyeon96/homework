import requests
from pprint import pprint as print

dummy_data =[]
for i in range(1,11):
# 무작위 유저 정보 요청 경로
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
 # API 요청

    response = requests.get(API_URL)
# JSON -> dict 데이터 변환

    parsed_data = response.json()
# print (parsed_data)


    # 응답 데이터 출력
    # print(response)

    # # 변환 데이터 출력
    # print(parsed_data)
    # # 변환 데이터의 타입
    # print(type(parsed_data))
    if (float(parsed_data['address']['geo']['lat']) < 80) and (float(parsed_data['address']['geo']['lat']) > -80):
        if (float(parsed_data['address']['geo']['lng']) > -80) and (float(parsed_data['address']['geo']['lng'])) < 80:
            dummy_data.append({'company': parsed_data['company']['name'],'lat': parsed_data['address']['geo']['lat'],'lng': parsed_data['address']['geo']['lng'],'name': parsed_data['name']})

print(dummy_data)