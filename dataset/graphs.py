import matplotlib.pyplot as plt
import numpy as np


def insert_plot() -> None:
    fig, ax = plt.subplots()

    x = [100, 500, 900, 1300, 1700, 2100, 2500, 2900]
    y = [9.49, 167.11, 385.48, 829.21, 22600.04, 1631.36, 2838.84, 2603.60]

    x1 = [100, 2900]
    y1 = [9.49, 2603.60]

    ax.plot(x1, y1, label='предполагалось')
    ax.plot(x, y, label='получилось')

    ax.plot()

    ax.legend(loc='upper left')

    ax.set_title('INSERT')
    ax.set_ylabel('Время работы(мс)')
    ax.set_xlabel('Кол-во элементов')

    plt.show()


def extr_min_plt() -> None:
    fig, ax = plt.subplots()

    x = [100, 500, 900, 1300, 1700, 2100, 2500, 2900]
    y = [1.60, 7.52, 8.26, 17.53, 12.91, 16.40, 28.90, 24.70]

    one = 9.49 / 1000

    z = x[:]
    z.append(1)
    z.sort()

    ax.plot(x, y, label='получилось')
    ax.plot(z, (np.log2(z)+z)*one, label='предполагалось')

    ax.plot()

    ax.legend(loc='upper left')

    ax.set_title('Extract min')
    ax.set_ylabel('Время работы(мс)')
    ax.set_xlabel('Кол-во элементов')

    plt.show()


def union_plt() -> None:
    fig, ax = plt.subplots()

    x = [100, 500, 900, 1300, 1700, 2100, 2500, 2900]
    y = [0.00, 0.00, 0.00, 0.00, 0.16, 0.00, 0.00, 0.00]

    one = 9.49 / 100

    ax.plot(x, y, label='получилось')
    ax.plot(x, [0]*len(x), label='предполагалось')

    ax.plot()

    ax.legend(loc='upper left')

    ax.set_title('Union')
    ax.set_ylabel('Время работы(мс)')
    ax.set_xlabel('Кол-во элементов')

    plt.show()


if __name__ == '__main__':
    insert_plot()
    extr_min_plt()
    union_plt()
