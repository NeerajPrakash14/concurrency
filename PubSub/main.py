
 
import time 
from threading import *
import random
import queue


   
# def publish(condition_object, data_queue ):
#     condition_object.acquire()
#     print('publishing message')
#     time.sleep(3)
#     value=0
#     value=random.randint(1,13)
#     data_queue.put(value)
#     print('value published is {}'.format(value))
#     condition_object.notify()
#     condition_object.release()


# def subscribe(condition_object, data_queue):
#     condition_object.acquire()
#     print('Waiting for subscribed message')
#     condition_object.wait()
#     print('Found subscribed message -> ', data_queue.get())
#     condition_object.release()
 


# data_queue = queue.Queue()

# condition_object = Condition()

 
# T1 = Thread(target=publish, args=(condition_object, data_queue))
 
# T2 = Thread(target=subscribe, args=(condition_object, data_queue))
 
# # Order is important here
# T2.start()
# T1.start()
 


def publish(condition_object, data_queue ):
    global counter
    condition_object.acquire()
    print('publishing message')
    time.sleep(3)
    counter=random.randint(1,13)
    data_queue.put(counter)
    print('value published is {}'.format(counter))
    condition_object.notify()
    condition_object.release()


def subscribe(condition_object, data_queue):
    global counter
    condition_object.acquire()
    print('Waiting for subscribed message')
    if(counter != 4):
        condition_object.wait()
        print('Found subscribed message -> ', data_queue.get())
        condition_object.release()
 


data_queue = queue.Queue()
counter = 0

condition_object = Condition()

 
T1 = Thread(target=publish, args=(condition_object, data_queue))
 
T2 = Thread(target=subscribe, args=(condition_object, data_queue))
 
# Order is important here
T2.start()
T1.start()
