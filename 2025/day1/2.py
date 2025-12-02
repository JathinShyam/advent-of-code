
with open('input.txt', 'r') as f:
    result = 0
    current = 50
    for line in f.readlines():
        d = line[0]
        x = int(line[1:])
        delta = +1 if d == "R" else -1
        for _ in range(x):
            current += delta
            current %= 100
            if current == 0:
                result += 1
    print(result)