safe_levels = 0


with open('input.txt', 'r') as f:
    for line in f.readlines():
        levels = list(map(int, line.split()))
        sorted_levels = sorted(levels)
        if levels != sorted_levels and levels != sorted_levels[::-1]:
            continue
        good = True
        for x, y in zip(levels, levels[1:]):
            if not (1 <= abs(y - x) <= 3):
                good = False
                break
        if good:
            safe_levels += 1
    print(safe_levels) # 534