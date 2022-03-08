def search(matrix, target):
    m = len(matrix)
    n = len(matrix[0])-1
    print(m, n)
    i = 0
    while(i < m and n >= 0):
        if matrix[i][n] == target:
            return True
        elif(matrix[i][n] > target):
            n -= 1
        else:
            i += 1
    return False


matrix=[[1,4,7,11,15], 
        [2,5,8,12,19],
        [3,6,9,16,22],
        [10,13,14,17,24],
        [18,21,23,28,30]]
target=16

result = search(matrix, target)
print(result)
