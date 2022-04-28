def factorial(n):
    if (n < 0):
        print("number is not positive")

    # if isinstance(n,int):
    if (type(n) != int):
        print("number is not an integer")

    else:
        result = 1

        for x in range(0, n):
            result = result * (n - x)

        print(result)


factorial(8)


# recursion

def factorial_recursion(n):
    if n == 0:
        return 1
    return n * factorial_recursion(n - 1)


print(factorial_recursion(4))

# DP
factorial = [1]
m = int(input())
for f in range(1, m+1):
    factorial.append(f*factorial[f-1])
print(factorial[m])
