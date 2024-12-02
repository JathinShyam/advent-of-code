safe_levels = 0

with open('input.txt', 'r') as f:
    for line in f.readlines():
        levels = list(map(int, line.split()))
        sorted_levels = sorted(levels)

        for i in range(len(levels)):
            good = True
            nums = levels[:i] + levels[i+1:]
            if nums != sorted(nums) and nums != sorted(nums)[::-1]:
                continue
            for i in range(len(nums) - 1):
                if not (1 <= abs(nums[i+1] - nums[i]) <= 3):
                    good = False
                    break
            if good:
                safe_levels += 1
                break

    print(safe_levels) # 577