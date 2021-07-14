
def pyramid(n):
    for i in range(1, n + 1):
        for j in range(0, n - i):
            print(" ", end=" ")
        for k in range(0, 2 * i + 1):
            print("*", end=" ")
        print()


# pyramid using one loop
def pyramidUsingOneLoop(n):
    for i in range(0, n):
        j = n - i - 1
        k = 2 * i + 1
        print("  " * j + "* " * k)


def revPyramid(n):
    for i in range(n, 0, -1):
        for j in range(0, n - i):
            print(" ", end=" ")
        for k in range(0, 2 * i - 1):
            print("*", end=" ")
        print()


if __name__ == "__main__":
    pyramidUsingOneLoop(5)
    print()
    revPyramid(5)
