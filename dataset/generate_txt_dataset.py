import os
from random import randint


def make_dirs():
    if not (os.path.isdir('insert') and os.path.isdir('extractmin') and os.path.isdir('union')):
        os.mkdir('insert')
        os.mkdir('extractmin')
        os.mkdir('union')

        for i in range(1, 6):
            os.makedirs('insert/0' + str(i))
            os.makedirs('extractmin/0' + str(i))
            os.makedirs('union/0' + str(i))


def make_txt_for_insert(i, j, some_arr):
    for k in some_arr:
        with open(i + '/' + j + '/' + str(k) + '.txt', 'w') as f:
            for m in range(k-1):
                some_number = randint(1, 1_000_000)
                f.write(str(some_number) + '\n')

            else:
                some_number = randint(1, 1_000_000)
                f.write(str(some_number))


def make_txt_for_union(i, j, some_arr):
    for k in some_arr:
        with open(i + '/' + j + '/' + str(k) + '.txt', 'w') as f:
            for m in range(1, 2*k - 1):
                some_number = randint(1, 1_000_000)
                f.write(str(some_number) + '\n')

                if m == k-1:
                    some_number = randint(1, 1_000_000)
                    f.write(str(some_number) + '\n' + '\n')

            else:
                some_number = randint(1, 1_000_000)
                f.write(str(some_number))


def make_txt_for_extract_min(i, j, some_arr):
    for k in some_arr:
        some_set = set()

        with open(i + '/' + j + '/' + str(k) + '.txt', 'w') as f:
            for m in range(k):
                some_number = randint(1, 1_000_000)
                some_set.add(some_number)
                f.write(str(some_number) + '\n')

            else:
                f.write(str(min(some_set)) + '\n')
                f.write(str(min2(some_set)))


def make_txt_files(some_arr):
    for i in os.listdir():
        if i[-3:] == '.py':
            continue

        for j in os.listdir(i):
            if i == 'insert':
                make_txt_for_insert(i, j, some_arr)

            if i == 'union':
                make_txt_for_union(i, j, some_arr)

            if i == 'extractmin':
                make_txt_for_extract_min(i, j, some_arr)


def min2(some_arr):
    m1, m2 = float('inf'), float('inf')

    for x in some_arr:
        if x <= m1:
            m1, m2 = x, m1

        elif x < m2:
            m2 = x

    return m2


arr_for_elements = [100, 5_000, 100_000, 5_000_000]
make_dirs()
make_txt_files(arr_for_elements)
