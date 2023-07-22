
from time import sleep, time
from threading import Thread
from threading import Condition
import queue



# load a file of words
def load_words(path):
    # open the file
    with open(path, encoding='utf-8') as file:
        # read all data as lines
        return file.readlines()

 
# target function to prepare some work
def task(result_queue):
    path = '1m_words.txt'
    words = load_words(path)
    print(f'Loaded {len(words)} words from {path}')

    matched_words = []
    for word in words:
        if(word.startswith('ab')):
            matched_words.append(word)

    work_list = matched_words
    result_queue.put(work_list)
    print('Thread sending notification...', len(work_list))





# entry point
def main():


    start_time = time()

    result_queue = queue.Queue()

    print('Main thread waiting for data...')


    for i in range(5):
        task(result_queue)

    
    end_time = time()
    elapsed_time = end_time - start_time
    print("Elapsed time -> ", elapsed_time)

    print(f'Got data: {len(result_queue.get())}')
    while not result_queue.empty():
        result = result_queue.get()
        print("Result from the queue:", len(result))










if __name__ == '__main__':
    main()
