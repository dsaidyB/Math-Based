import math

def vec_mat(v, A):
    new = []
    for m in range(0, len(v)):
        temp = 0
        for n in range(0, len(v)):
            print(v[n])
            print(A[m][n])
            temp += v[n] * A[m][n]
        new.append(temp)
    return new

theta = math.pi/4
v1 = [0, 0, 1]
A1 = [[math.cos(theta), -math.sin(theta), 0], [math.sin(theta), math.cos(theta), 0], [0, 0, 1]]

print(vec_mat(v1, A1))