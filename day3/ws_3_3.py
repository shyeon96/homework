number_of_book = 100

def rental_book(name, numbers):
    decrease_book(numbers)
    return f'{name}님이 {numbers}권의 책을 대여하였습니다.'

# number_of_book = 100

def decrease_book(numbers):
    global number_of_book
    print (f'남은 책의 수: {number_of_book - numbers}')
    return number_of_book - numbers

result = rental_book('홍길동',3)
print (result)