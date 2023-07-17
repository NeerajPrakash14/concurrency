# example of daemon threads being terminated abruptly
from time import sleep
from threading import current_thread
from threading import Thread
 
# function to be executed in a new thread
def task():
    # get the current thread
    thread = current_thread()
    # report if daemon thread
    print(f'Daemon thread: {thread.daemon}')
    # loop for a while
    for i in range(1000):
        print(i)
        # block for a moment
        sleep(0.1)
 
# create a new daemon thread
thread = Thread(target=task, daemon=True)
# start the new thread
thread.start()
# block for a moment to let the daemon thread run
sleep(3)
# prepare the user
print('Main thread exiting...')
