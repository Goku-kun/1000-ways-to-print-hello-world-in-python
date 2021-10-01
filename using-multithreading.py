import threading

def print_helloworld(thread):
    print("Hello World from thread {}".format(thread))

if __name__ == "__main__":
    # creating threads
    number_of_threads = 10
    t = []
    for index in range(0,number_of_threads):
        t.append(threading.Thread(target=print_helloworld, args=(index,)))

    for index in range(0,number_of_threads):
        # starting threads
        t[index].start()

    for index in range(0,number_of_threads):
        # wait until each thread is completely executed
        t[index].join()

    # All threads completely executed
    print("Done!")
