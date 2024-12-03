import re
with open('input.txt', 'r') as f:
    data = f.read()

answer = 0

for a, b in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', data):
	a = int(a)
	b = int(b)
	answer += a * b

print(answer) # 153469856
