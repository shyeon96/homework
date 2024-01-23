# 아래 함수를 수정하시오.
def union_sets(set1, set2):
    set3 = set1.union(set2)
    return set3


result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)
