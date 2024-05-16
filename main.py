import numpy as np
import matplotlib.pyplot as plt


def diamond_square(side, N, arr, roughness):
    border = 1
    while side > 1:
        new_side = side // 2

        for curr_x in range(border):
            for curr_y in range(border):
                x_0, x_1 = curr_x * side, (curr_x + 1) * side
                y_0, y_1 = curr_y * side, (curr_y + 1) * side
                x_center, y_center = x_0 + new_side, y_0 + new_side
                arr[y_center, x_center] = (arr[y_0, x_0] + arr[y_0, x_1] + arr[y_1, x_0] + arr[
                    y_1, x_1]) / 4 + roughness * np.random.uniform(-1, 1)

        for curr_y in range(2 * border + 1):
            y_center = new_side * curr_y
            for curr_x in range(border + 1):
                x_center = side * curr_x + new_side * (1 - curr_y % 2)
                if not (0 <= x_center < N and 0 <= y_center < N):
                    continue
                tot: float = 0
                number_tot = 0
                for (dx, dy) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    xs, ys = x_center + dx * new_side, y_center + dy * new_side
                    if not (0 <= xs < N and 0 <= ys < N):
                        continue
                    else:
                        tot += arr[ys, xs]
                        number_tot += 1
                arr[y_center, x_center] += tot / number_tot + roughness * \
                                           np.random.uniform(-1, 1)
        side = new_side
        border *= 2
        roughness /= 2


def main():
    N = 2 ** 9 + 1
    arr = np.zeros((N, N))
    arr[0::N - 1, 0::N - 1] = np.random.uniform(-1, 1, (2, 2))
    side = N - 1
    print('Введите шероховатость: ')
    roughness = float(input())
    diamond_square(side, N, arr, roughness)
    plt.imshow(arr, cmap='Blues')
    plt.show()


main()