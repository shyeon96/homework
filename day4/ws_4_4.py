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



black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

def create_user(users_list):
    censored_user_list = {}
    for users in users_list:
        if censorship(users):
            censored_user_list[users['company']] = [users['name']]
    return censored_user_list



def censorship(users_list):
    if users_list['company'] in black_list:
        print(f"{users_list['company']}소속의 {users_list['name']}은/는 등록할 수 없습니다.")
        return False
    else:
        print('이상 없습니다.')
        return True
        
result = create_user(dummy_data)
print(result)
