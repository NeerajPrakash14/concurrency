
##############################################

###############################################

# example of checking if a new thread is a daemon thread
from threading import current_thread
from threading import Thread
 
# function to be executed in a new thread
def task():
    # get the current thread
    thread = current_thread()
    # report if daemon thread
    print(f'Daemon thread: {thread.daemon}')
 
# create a new thread with a default value for "daemon"
thread = Thread(target=task)
# start the new thread
thread.start()


##############################################

###############################################
# example of creating a new daemon thread
from time import sleep
from threading import current_thread
from threading import Thread
 
# function to be executed in a new thread
def task():
    # get the current thread
    thread = current_thread()
    # report if daemon thread
    print(f'Daemon thread: {thread.daemon}')
 
# create a new daemon thread
thread = Thread(target=task, daemon=True)
# start the new thread
thread.start()
# block for a moment to let the daemon thread run
sleep(0.5)




##############################################

###############################################

# example of configuring a thread to be a daemon thread
from time import sleep
from threading import current_thread
from threading import Thread
 
# function to be executed in a new thread
def task():
    # get the current thread
    thread = current_thread()
    # report if daemon thread
    print(f'Daemon thread: {thread.daemon}')
 
# create a new thread
thread = Thread(target=task)
# configure the thread to be a daemon thread
thread.daemon = True
# start the new thread
thread.start()
# block for a moment to let the daemon thread run
sleep(0.5)



##############################################

###############################################

# SuperFastPython.com
# example of creating a daemon thread from a daemon thread
from time import sleep
from threading import current_thread
from threading import Thread
 
# function to be executed by second daemon thread
def task2():
    # get the current thread
    thread = current_thread()
    # report if daemon thread
    print(f'Daemon thread 2: {thread.daemon}')
 
# function to be executed in a new thread
def task():
    # get the current thread
    thread = current_thread()
    # report if daemon thread
    print(f'Daemon thread 1: {thread.daemon}')
    # create a new thread
    new_thread = Thread(target=task2)
    # start the new thread
    new_thread.start()
 
# create a new daemon thread
thread = Thread(target=task, daemon=True)
# start the new thread
thread.start()
# block for a moment to let the daemon threads run
sleep(0.5)


##############################################

###############################################
# example of changing the current thread to be a daemon thread
from threading import current_thread
# get the current thread
thread = current_thread()
# report if daemon thread
print(f'Daemon thread: {thread.daemon}')
# try and change the current thread to be a daemon
thread.daemon = True



##############################################

###############################################
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

