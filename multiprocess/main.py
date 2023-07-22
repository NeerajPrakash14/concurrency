
from time import sleep, time
# from threading import Thread
# from threading import Condition
import queue
import multiprocessing


print("hello")



# load a file of words
def load_words(path):
    # open the file
    with open(path, encoding='utf-8') as file:
        # read all data as lines
        return file.readlines()

 
# target function to prepare some work
def task(result_queue):
    # load a file of words
    path = 'multiprocess/1m_words.txt'
    words = load_words(path)
    print(f'Loaded {len(words)} words from {path}')

    matched_words = []
    for word in words:
        if(word.startswith('ab')):
            matched_words.append(word)

    work_list = matched_words
    result_queue.put(len(work_list))
    print('Thread sending notification...', len(work_list))
 




# entry point
def main():

    start_time = time()

    result_queue = multiprocessing.Queue()

    print('Main thread waiting for data...')

    processes = []
    # with condition:
    for i in range(5):
        process = multiprocessing.Process(target=task, args=(result_queue,))
        process.start()

        processes.append(process)


    for process in processes:
        process.join()
    
    end_time = time()
    elapsed_time = end_time - start_time
    print("Elapsed time -> ", elapsed_time)
    print(f'Got data: {result_queue.get()}')




# # import multiprocessing

# def scan(queue):
#     # Perform some processing and append the result to the queue
#     result = 42
#     queue.put(result)

# if __name__ == "__main__":
#     # Create a queue to store the results
#     result_queue = multiprocessing.Queue()

#     # Create and start the 4 processes
#     processes = []
#     for _ in range(5):
#         process = multiprocessing.Process(target=task, args=(result_queue,))
#         process.start()
#         processes.append(process)

#     # Wait for all processes to finish appending to the queue
#     for process in processes:
#         process.join()

#     # Print the results from the queue
#     while not result_queue.empty():
#         result = result_queue.get()
#         print("Result from the queue:", result)







if __name__ == '__main__':
    test_run_count = 5
    average_time_elapsed = 0
    for i in range(0, test_run_count):
        start_time = time()
        main()
        end_time = time()
        elapsed_time = end_time - start_time
        average_time_elapsed  += elapsed_time
    
    average_time_elapsed = average_time_elapsed / test_run_count
    
    print("Using Function, Average Time Elapsed--- %s seconds ---" % (average_time_elapsed))

    
