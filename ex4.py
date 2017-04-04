# -*- coding: utf-8 -*-
# n*nの行列を入れ替える関数を作ってください。
# before [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# after [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

#arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
arr2 = []
for i in range(len(arr)):
    arr2.append([])
    for j in range(len(arr[i])):
        arr2[i].append(arr[j][i])
print(arr)
print(arr2)
