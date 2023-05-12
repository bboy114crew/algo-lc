# https://leetcode.com/problems/pascals-triangle-ii

def getNum(row, col):
    if row == 0 or col == 0 or row == col:
        return 1

    return getNum(row - 1, col - 1) + getNum(row - 1, col)
def getRow(rowIndex):
    result = []

    for i in range(rowIndex + 1):
        print(i)
        result.append(getNum(rowIndex, i))

    return result

getRow(3)
