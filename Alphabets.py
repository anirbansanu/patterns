def A():
    n = 6
    for rows in range(0, n):
        if rows == 0 or rows == n//2:
            print("* "*(n-1)+"*", end="")
        else:
            print("* "+"  "*(n-2)+"*", end="")
        print()


if __name__ == "__main__":
    A()
