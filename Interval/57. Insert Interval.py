class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        lower_fit = -1
        intervalsClone = []
        append = False

        if not intervals:
            return [newInterval]

        for i in range(len(intervals)):
            if append is True:
                intervalsClone.append(intervals[i])
                continue

            if newInterval[0] < intervals[i][0]:
                if newInterval[1] < intervals[i][0]:
                    if lower_fit == -1:
                        intervalsClone.append(newInterval)
                        intervalsClone.append(intervals[i])
                        append = True
                    else:
                        intervalsClone.append([lower_fit, newInterval[1]])
                        intervalsClone.append(intervals[i])
                        append = True
                else:
                    if lower_fit == -1:
                        lower_fit = newInterval[0]
                    if newInterval[1] <= intervals[i][1]:
                        intervalsClone.append([lower_fit, intervals[i][1]])
                        append = True
                    else:
                        continue
            else:
                if newInterval[0] <= intervals[i][1]:
                    lower_fit = intervals[i][0]
                    if newInterval[1] <= intervals[i][1]:
                        intervalsClone.append(intervals[i])
                        append = True
                    else:
                        continue
                else:
                    intervalsClone.append(intervals[i])
            
        if not intervalsClone and lower_fit != -1:
            return [[lower_fit, newInterval[1]]]

        if lower_fit == -1 and append is False:
            intervalsClone.append(newInterval)

        if lower_fit != -1 and append is False:
            intervalsClone.append([lower_fit, newInterval[1]])

        return intervalsClone
