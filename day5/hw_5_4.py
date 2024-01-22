# 아래 함수를 수정하시오.
def find_min_max(test_list):
    test_list.sort()
    return (test_list[0], test_list[-1])
    
    
# sort 안쓰고 하기
    # compare = [1,1]
    # for i in test_list:
    #     if i >= compare[0]:
    #         if i >= compare[1]:
    #             compare[1] = i
    #     elif i <= compare[0]:
    #         compare[0] = i
    #     else:
    #         compare[0] = i
    #         compare[1] = i
    # return tuple(compare)



result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
