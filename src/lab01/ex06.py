N = int(input().strip())
ochno = 0
zaocho = 0
for _ in range(N):
    parts = input().strip().split()
    if parts[3] == "True":
        ochno += 1
    else:
        zaocho += 1
print(ochno, zaocho)