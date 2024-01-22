import ws_3_1


number_of_people = 0

#
# def increase_user():


user_info = {'name': '','age': 0,'address': ''}

def create_user(name, age, address):
    # ws_3_1.increase_user()
    user_info['name'] = name
    user_info['age'] = age 
    user_info['address'] = address

    print(f'{name}님, 환영합니다!')
    return user_info

result = create_user('홍길동',30,'서울')
print(result)
ws_3_1.increase_user()