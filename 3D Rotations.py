import numpy as np
import math

for n in range(0, int(input())):
    vals = list(map(float, input().split(" ")))
    a, b, c, x, y, z = vals[0], vals[1], vals[2], vals[3], vals[4], vals[5]
    if (a == b == c == 0):
        print("0.000000 0.000000 0.000000")
    else:
        point = np.array([a, b, c])
        axis = np.array([x, y, z])
        r = vals[6]

        theta = np.arctan(y / x)
        phi = math.pi / 2 - np.arcsin(z/math.sqrt(x**2 + y**2 + z**2))

        xy = np.array([[np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0], [0, 0, 1]])
        inv_xy = np.array([[np.cos(theta), np.sin(theta), 0], [-np.sin(theta), np.cos(theta), 0], [0, 0, 1]])

        zx = np.array([[np.cos(phi), 0, np.sin(phi)], [0, 1, 0], [-np.sin(phi), 0, np.cos(phi)]])
        inv_zx = np.array([[np.cos(phi), 0, -np.sin(phi)], [0, 1, 0], [np.sin(phi), 0, np.cos(phi)]])

        rotate = np.array([[np.cos(r), -np.sin(r), 0], [np.sin(r), np.cos(r), 0], [0, 0, 1]])

        new_basis = point@inv_xy@inv_zx
        # print(new_basis)

        rotate_new_basis = new_basis@rotate
        # print(rotate_new_basis)

        undo_basis_change = rotate_new_basis@zx@xy
        # print(undo_basis_change)

        ans = np.round(undo_basis_change, 6)
        print(ans[0], ans[1], ans[2])

    # print(xy)
    # print(zx)
    # print(rotate)

    # print(theta)
    # print(phi)
    # print(point)
    # print(axis)
    # print(r)
