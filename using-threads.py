#Printing Hello world after 2 secs
from threading import Timer

def hello():
    print("Hello, world!")

# create thread
t = Timer(2.0, hello)

# start thread after 2 seconds
t.start()