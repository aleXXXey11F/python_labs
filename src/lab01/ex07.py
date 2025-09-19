s = input().strip()

start = next(i for i, c in enumerate(s) if c.isupper())
second = next(i+1 for i, c in enumerate(s) if c.isdigit())

step = second - start

result = "".join(s[i] for i in range(start, len(s), step))
print(result)
