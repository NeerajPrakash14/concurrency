
from time import sleep, time
from threading import Thread
from threading import Condition
import queue

print("hello")


# load a file of words
def load_words(path):
    # open the file
    with open(path, encoding='utf-8') as file:
        # read all data as lines
        return file.readlines()

 
# target function to prepare some work
def task(condition, result_queue):
    # with condition:
    # load a file of words
    path = '1m_words.txt'
    words = load_words(path)
    print(f'Loaded {len(words)} words from {path}')

    #sleep(2)
    matched_words = []
    for word in words:
        if(word.startswith('ab')):
            matched_words.append(word)

    work_list = matched_words
    result_queue.put(work_list)
    # notify a waiting thread that the work is done
    print('Thread sending notification...', len(work_list))

    # condition.notify()
 




# entry point
def main():

    start_time = time()

    result_queue = queue.Queue()
    condition = Condition()

    print('Main thread waiting for data...')

    threads = []
    # with condition:
    for i in range(5):
        worker = Thread(target=task, args=(condition, result_queue))
        worker.start()

        threads.append(worker)

            #worker.join()
        
        # condition.wait()

    for thread in threads:
        thread.join()
    
    end_time = time()
    elapsed_time = end_time - start_time
    print("Elapsed time -> ", elapsed_time)
    print(f'Got data: {len(result_queue.get())}')












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

    
