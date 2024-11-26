import numpy as np


def search_vector_k(z: list[list[float]], y: list[float]) -> list:
    dt = np.dtype(np.float64)
    mz = np.array(z, dtype=dt).T
    my = np.array(y, dtype=dt)
    b = mz.T.dot(mz)
    b = np.linalg.inv(b)
    b = b.dot(mz.T)
    b = b.dot(my)
    return b.tolist()


def test():
    x = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [10, 15, 20, 25, 40, 37, 43, 35, 38, 55],
    [12, 10, 9, 9, 8, 8, 6, 4, 4, 5]
]

    y = [20, 35, 30, 45, 60, 69, 75, 90, 105, 110]
    k = search_vector_k(x, y)
    print(k)


def main():
    test()


if __name__ == '__main__':
    main()