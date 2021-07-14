def square(n):
    for i in range(0, n):
        for j in range(0, n):
            print("*", end=" ")
        print()


if __name__ == "__main__":
    square(4)