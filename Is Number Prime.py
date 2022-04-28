n = int(input())

factors = 0

for x in range(1,n):
    if (n % x == 0):
        factors = factors + 1
    if (factors > 1):
        break

if (factors == 1):
    print("yes")
else:
    print("no")
