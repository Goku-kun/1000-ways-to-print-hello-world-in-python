def recursion(x):
    if x == 0:
        return 0
    else:
        print("Hello, World!")
        return recursion(x-1)

if __name__ == '__main__':
    x = 1
    recursion(x)
