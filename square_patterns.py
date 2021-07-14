def square(n):
    for i in range(0, n):
        for j in range(0, n):
            print("*", end=" ")
        print()


def squareBorder(n):
    for rows in range(0, n):
        for cols in range(0, n):
            if cols == 0 or cols == n-1 or rows == 0 or rows == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def squareBorderUsingOnlyOneLoop(n):
    for rows in range(0, n):
        print("* ", end="")
        if rows == 0 or rows == n-1:
            print("* "*(n-2), end="")
        else:
            print("  "*(n-2), end="")
        print("* ")


if __name__ == "__main__":
    square(5)
    print()
    squareBorder(5)
    print()
    print()
    squareBorderUsingOnlyOneLoop(5)