import math


def vec_mat(v, A):
    new = []
    for m in range(0, len(v)):
        temp = 0
        for n in range(0, len(v)):
            temp += v[n] * A[m][n]
        new.append(temp)
    return new


for n in range(0, int(input())):
    vals = list(map(float, input().split(" ")))
    a, b, c, x, y, z = vals[0], vals[1], vals[2], vals[3], vals[4], vals[5]
    if (a == b == c == 0):
        print("0.000000 0.000000 0.000000")
    else:
        point = [a, b, c]
        axis = [x, y, z]
        r = vals[6]

        theta = 0
        xy = []
        inv_xy = []

        if (x == 0 and y > 0):
            theta = math.pi/2
            xy = [[math.cos(theta), -math.sin(theta), 0], [math.sin(theta), math.cos(theta), 0], [0, 0, 1]]
            inv_xy = [[math.cos(theta), math.sin(theta), 0], [-math.sin(theta), math.cos(theta), 0], [0, 0, 1]]
        elif (x == 0 and y < 0):
            theta = 3*math.pi/2
            xy = [[math.cos(theta), -math.sin(theta), 0], [math.sin(theta), math.cos(theta), 0], [0, 0, 1]]
            inv_xy = [[math.cos(theta), math.sin(theta), 0], [-math.sin(theta), math.cos(theta), 0], [0, 0, 1]]
        elif (x == y == 0):
            xy = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
            inv_xy = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        else:
            theta = math.atan(y / x)
            xy = [[math.cos(theta), -math.sin(theta), 0], [math.sin(theta), math.cos(theta), 0], [0, 0, 1]]
            inv_xy = [[math.cos(theta), math.sin(theta), 0], [-math.sin(theta), math.cos(theta), 0], [0, 0, 1]]

        phi = math.pi / 2 - math.asin(z / math.sqrt(x ** 2 + y ** 2 + z ** 2))

        zx = [[math.cos(phi), 0, math.sin(phi)], [0, 1, 0], [-math.sin(phi), 0, math.cos(phi)]]
        inv_zx = [[math.cos(phi), 0, -math.sin(phi)], [0, 1, 0], [math.sin(phi), 0, math.cos(phi)]]

        rotate = [[math.cos(r), -math.sin(r), 0], [math.sin(r), math.cos(r), 0], [0, 0, 1]]

        new_basis = vec_mat(vec_mat(point, inv_xy), inv_zx)
        # print(new_basis)

        rotate_new_basis = vec_mat(new_basis, rotate)
        # print(rotate_new_basis)

        undo_basis_change = vec_mat(vec_mat(rotate_new_basis, zx), xy)
        # print(undo_basis_change)

        print('{:.6f}'.format(round(undo_basis_change[0], 6)), '{:.6f}'.format(round(undo_basis_change[1], 6)),
              '{:.6f}'.format(round(undo_basis_change[2], 6)))

    # print(xy)
    # print(zx)
    # print(rotate)

    # print(theta)
    # print(phi)
    # print(point)
    # print(axis)
    # print(r)
