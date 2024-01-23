# 아래 함수를 수정하시오.
def remove_duplicates_to_set(rdts):
    my_set = set()
    list_rdts = list(rdts)
    for a in list_rdts:
        my_set.add(a)
    return my_set


result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)
