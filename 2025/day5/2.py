"""
--- Part Two ---
The Elves start bringing their spoiled inventory to the trash chute at the back of the kitchen.

So that they can stop bugging you when they get new inventory, the Elves would like to know all of the IDs that the fresh ingredient ID ranges consider to be fresh. An ingredient ID is still considered fresh if it is in any range.

Now, the second section of the database (the available ingredient IDs) is irrelevant. Here are the fresh ingredient ID ranges from the above example:

3-5
10-14
16-20
12-18
The ingredient IDs that these ranges consider to be fresh are 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, and 20. So, in this example, the fresh ingredient ID ranges consider a total of 14 ingredient IDs to be fresh.

Process the database file again. How many ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges?

Your puzzle answer was 344423158480189.


"""
from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:i[0])
        res = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = res[-1][1]
            if start <= lastEnd:
                res[-1][1] = max(lastEnd, end)
            else:
                res.append([start,end])
        return res

with open('input.txt', 'r') as f:
    fresh = 0
    ranges = []
    seen = set()
    empty_line = False
    for line in f.readlines():
        line = line.strip()
        if line == '':
            empty_line = True
            ranges = merge(ranges)
            continue
        if not empty_line:
            a, b = map(int, line.split('-'))
            ranges.append([a, b])
        else:
            break
    
    result = 0
    for a, b in ranges:
        result += b - a + 1
    print(result)