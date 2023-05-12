# https://leetcode.com/problems/rotate-image

def rotate(matrix):
    n = len(matrix) - 1
    midr = n // 2 + 1
    midc = midr if n % 2 else midr - 1
    print(n)
    for a in range(midr):
        c = n - a
        for b in range(midc):
            d = n - b
            temp = matrix[a][b]
            matrix[a][b] = matrix[d][a]
            matrix[d][a] = matrix[c][d]
            matrix[c][d] = matrix[b][c]
            matrix[b][c] = temp


rotate([[1,2,3,4,5],[6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]])
