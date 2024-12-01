first_group, second_group = [], []

with open('input.txt', 'r') as f:
    for line in f.readlines():
        first, second = line.split()
        first_group.append(int(first))
        second_group.append(int(second))
    result = 0
    first_group.sort()
    second_group.sort()
    for l,r in zip(first_group, second_group):
        result += abs(l - r)
    print(result) # 2176849