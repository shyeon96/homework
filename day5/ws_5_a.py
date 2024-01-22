N = 9
data_1 = '123456789'
arr_1 = []
for a in data_1:
    arr_1.append(a)
print(arr_1)


M = 15
data_2 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
arr_2 = list(map(int,data_2.split()))
for a in arr_2:
    if a % 2 == 1:
        print(a)
