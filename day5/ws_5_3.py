# 아래 함수를 수정하시오.
def sort_tuple(input_tuple):
    new_tuple = ()
    tuple_list = list(input_tuple)
    tuple_list.sort()
    new_tuple = tuple(tuple_list)
    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)
