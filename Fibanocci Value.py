def fibanocci_val (n):
    if (n == 0):
        return (0)

    if (n == 1):
        return (1)

    else:
        return fibanocci_val(n-1) + fibanocci_val(n-2)

print(fibanocci_val(6))

num = 10

for x in range(0, num):
    print(fibanocci_val(x))