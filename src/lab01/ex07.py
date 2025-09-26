s = input().strip()
start = -1
for i in range(len(s)):
    if s[i].isupper():
        start = i
        break  
second = -1
for i in range(len(s)):
    if s[i].isdigit():
        second = i + 1  
        break
if start == -1 or second == -1:
    print("Не найдена заглавная буква или цифра!")
else:
    step = second - start
    result = ""
    for i in range(start, len(s), step):
        result += s[i]
    print(result)
