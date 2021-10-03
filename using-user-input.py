# A program to print 'Hello World' by force typing it by the user himself

def hello_world():
    str = input("Enter 'Hello World' exactly: ")
    if str == 'Hello World':
        print(str)
    else:
        print('Try Again!')
        hello_world()

hello_world()