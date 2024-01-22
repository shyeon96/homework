number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1
    print(f'현재 가입 된 유저 수 : {number_of_people}')

# user_info = {'name': '','age': 0,'address': ''}

def create_user(name, age, address):
    user_info = {'name': '','age': 0,'address': ''}
    user_info['name'] = name
    user_info['age'] = age 
    user_info['address'] = address

    print(f'{name}님, 환영합니다!')
    return user_info

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

result = list(map(create_user,name,age,address))
print (result)