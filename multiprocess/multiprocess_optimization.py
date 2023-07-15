
# example of testing chunksize when hashing a word list in parallel with the process pool
from math import ceil
from time import time
from hashlib import sha512
from multiprocessing import Pool, cpu_count
 
# hash one word using the SHA algorithm
def hash_word(word):
    # create the hash object
    hash_object = sha512()
    # convert the string to bytes
    byte_data = word.encode('utf-8')
    # hash the word
    hash_object.update(byte_data)
    # get the hex hash of the word
    return hash_object.hexdigest()
 
# load a file of words
def load_words(path):
    # open the file
    with open(path, encoding='utf-8') as file:
        # read all data as lines
        return file.readlines()
 
# test a chunksize
def test_chunksize(words, size):
    time1 = time()
    # create the process pool
    with Pool(4) as pool:
        # create a set of word hashes
        _ = set(pool.map(hash_word, words, chunksize=size))
    time2 = time()
    total = time2 - time1
    print(f'{size}: {total:.3f} seconds')



def run_and_optimize(tasks):
    tasks_list = tasks
    cores_available = cpu_count()
    print(f'Number of cores - {cores_available}')

    # test chunk sizes
    base = ceil(len(tasks_list) / cores_available)
    sizes = [None, base, 100000, 50000, 10000, 5000, 1000, 500]
    for size in sizes:
        test_chunksize(tasks_list, size)

 

# entry point
def main():
    # load a file of words
    path = '1m_words.txt'
    words = load_words(path)
    print(f'Loaded {len(words)} words from {path}')
    run_and_optimize(words)









 
if __name__ == '__main__':
    main()
    run_and_optimize

