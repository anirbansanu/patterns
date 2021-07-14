def pattern(n):
    print("\nPrint 90° triangle")
    for i in range(0, n):
        for j in range(0, i + 1):
            print("*", end=" ")
        print()


def trianglePattern(n):
    print("\nPrint 90° triangle using one loop")
    for i in range(1, n+1):
        print("* "*i)


def rev_pattern(n):
    print("\nPrint reverse 90° triangle")
    for i in range(n, 0, -1):
        for j in range(0, i):
            print("*", end=" ")
        print()


def revTrianglePattern(n):
    print("\nPrint reverse 90° triangle using only one loop")
    for i in range(n, 0, -1):
        print("* " * i)


if __name__ == "__main__":
    pattern(5)
    trianglePattern(5)
    rev_pattern(5)
    revTrianglePattern(5)
