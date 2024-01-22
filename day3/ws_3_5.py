number_of_people = 0
number_of_book = 100

def increase_user():
    pass


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(name, age, address):
    user_info = {'name': '','age': 0,'address': ''}
    user_info['name'] = name
    user_info['age'] = age 
    user_info['address'] = address
    print(f'{name}님, 환영합니다!')

    return user_info

many_user = list(map(create_user,name,age,address))


def decrease_book(numbers):
    global number_of_book
    print (f'남은 책의 수: {number_of_book - numbers}')
    number_of_book = number_of_book - numbers

def rental_book(info):
    numbers = info['age'] // 10
    decrease_book(numbers)
    print (f"{info['name']}님이 {numbers}권의 책을 대여하였습니다.")

nameage = lambda x : {'name' : x['name'],'age': x['age']}
info = list(map(nameage,many_user))
list(map(rental_book,info))

