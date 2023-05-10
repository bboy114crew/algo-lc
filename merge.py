# https://leetcode.com/problems/merge-intervals

def takeOne(elem):
    return elem[0]

def merge(intervals):
    intervals.sort(key=takeOne)
    if len(intervals) == 1:
        return intervals
    i = 0
    j = i + 1
    result = []
    current_interval = [intervals[i][0], intervals[i][1]]
    while i < len(intervals):
        end_i = current_interval[1]
        start_j = intervals[j][0]

        if end_i >= start_j and (intervals[j][1] >= end_i or intervals[j][1] >= current_interval[0]):
            current_interval = [min(start_j, current_interval[0]), max(end_i, intervals[j][1])]
            if j == len(intervals) - 1:
                result.append(current_interval)
                break
            j += 1
        else:
            result.append(current_interval)
            i = j
            j += 1
            current_interval = [intervals[i][0], intervals[i][1]]
            if i == len(intervals) - 1:
                result.append(current_interval)
                break
    return result

print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[0,4]]))
print(merge([[1,4],[0,0]]))
print(merge([[1,4],[0,1]]))
print(merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
