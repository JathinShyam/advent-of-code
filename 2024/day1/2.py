import collections
first_group, second_group = [], []

with open('input.txt', 'r') as f:
    for line in f.readlines():
        first, second = line.split()
        first_group.append(int(first))
        second_group.append(int(second))
    
    counter = collections.Counter(second_group)
    total_score = 0
    for num in first_group:
        total_score += num * counter[num]
    print(total_score) # 23384288