import re
with open('input.txt', 'r') as f:
    data = f.read()

answer = 0
enabled = True
for m in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)|(don\'t\(\))|(do\(\))', data):
    if m[2] == 'don\'t()':
        enabled = False
        continue
    elif m[3] == 'do()':
        enabled = True
        continue
    if enabled:
        a, b = m[:2]
        a = int(a)
        b = int(b)
        answer += a * b

print(answer) # 77055967
