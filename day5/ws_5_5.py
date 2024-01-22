# 아래 함수를 수정하시오.
def even_elements(my_list):
    a = []
    for i in my_list:
        if i % 2 == 0:
            item1 = my_list.pop(my_list.index(i))
            a.extend([item1])
            item1 = 0
    return a


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
