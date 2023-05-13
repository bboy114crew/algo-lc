# https://leetcode.com/problems/spiral-matrix-ii
import math

def generateMatrix(n):
    layers = math.floor(n + 1 / 2)
    result = [[0 for _ in range(n)] for _ in range(n)]

    count = 1
    for layer in range(layers):
        for i in range(layer, n - layer):
            result[layer][i] = count
            count += 1

        for i in range(layer + 1, n - layer):
            result[i][n - layer - 1] = count
            count += 1

        for i in range(n - layer - 2, layer - 1, -1):
            print(count)
            result[n - layer - 1][i] = count
            count += 1

        for i in range(n - layer - 2, layer, -1):
            result[i][layer] = count
            count += 1

    return result

generateMatrix(3)
