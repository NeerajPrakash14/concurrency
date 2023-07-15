import multiprocessing as mp
import time, math

global results_a,results_b,results_c
results_a = 0
results_b = 0
results_c = 0 

def make_calc_1(numbers):
   global results_a
   for number in numbers:
        results_a += (number * 2)

def make_calc_2(numbers):
   global results_b
   for number in numbers:
        results_b += (number * 2)

def make_calc_3(numbers):
   global results_c
   for number in numbers:
        results_c += (number * 2)

def main():
    global results_a,results_b,results_c
    numbers = list(range(2))  # up to 1 : Result = (1 * 2) = 2
    numbers2 = list(range(3)) # up to 2 : Result = (1 * 2) + (2 * 2) = 6
    numbers3 = list(range(4)) # up to 3 : Result = (1 * 2) + (2 * 2) + (3 * 2) = 12

    tini = time.time()
    make_calc_1(numbers)
    make_calc_2(numbers2)
    make_calc_3(numbers3)
    tfin = time.time()
    print (" Sequential time : ", (tfin - tini))
    print(" A : ", results_a, "\n B : ", results_b,"\n C : ",results_c)
    tini = tfin

    # Reset results values to zero (0)
    results_a = 0
    results_b = 0
    results_c = 0
    
    p1 = mp.Process(target="make_calc_1",args=(numbers),)
    p2 = mp.Process(target="make_calc_2",args=(numbers2),)
    p3 = mp.Process(target="make_calc_3",args=(numbers3),)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()


    # Whatever you chose ("terminate()" or "kill()") produce same results
    p1.terminate()
    p2.terminate()
    p3.terminate()
    
    tfin = time.time()
    print ("\n Multiprocess time : ", (tfin - tini))
    print(" A : ", results_a, "\n B : ", results_b,"\n C : ",results_c)


if __name__ == '__main__':
    main()
