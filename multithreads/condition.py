# import threading

# print("Hello")

# # Shared resource (counter)
# counter = 0

# # Condition associated with the counter
# condition = threading.Condition()

# def increment_counter():
#     global counter
#     with condition:
#         counter += 1
#         condition.notify_all()

# def wait_until_threshold(threshold):
#     global counter
#     with condition:
#         while counter < threshold:
#             condition.wait()

# # Create two threads
# thread1 = threading.Thread(target=increment_counter)
# thread2 = threading.Thread(target=wait_until_threshold, args=(5,))

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

# print("Counter:", counter)  # Output will be 5


# code
 
# import modules
 
import time
from threading import *
import random
 
 
 
class appointment:
   
  def patient(self):
    condition_object.acquire()
    print('patient john waiting for appointment')
    condition_object.wait()   # Thread is in waiting state
    print('successfully got the appointment')
    condition_object.release()
 
  def doctor(self):
    condition_object.acquire()
    print('doctor jarry checking the time for appointment')
    time=0
    time=random.randint(1,13)
    print('time checked')
    print('appointed time is {} PM'.format(time))
    condition_object.notify()
    condition_object.release()
 
   
condition_object = Condition()
class_obj=appointment()
 
T1 = Thread(target=class_obj.patient)
 
T2 = Thread(target=class_obj.doctor)
 
T1.start()
 
T2.start()
