import time

CONCURRENT_USERS = 100000000

# Increment through a function
def increment_using_function():
    
    count = 0

    def increment_count_operation(count):
        count += 1
        return count

    for i in range(0, CONCURRENT_USERS):
        count = increment_count_operation(count)
        count = increment_count_operation(count)
    
    print('count-> ', count)


    


# Increment without a function
def increment_without_function():
    count = 0

    for i in range(0, CONCURRENT_USERS):
        count = count + 1

    print('count-> ', count)
    



def main():
    test_run_count = 10

    average_time_elapsed = 0
    for i in range(0, test_run_count):
        start_time = time.time()
        increment_using_function()
        end_time = time.time()
        elapsed_time = end_time - start_time
        average_time_elapsed  += elapsed_time
        print("Time Elapsed--- %s seconds ---" % (elapsed_time))


    average_time_elapsed = average_time_elapsed / test_run_count
    print("Using Function, Average Time Elapsed--- %s seconds ---" % (average_time_elapsed))
    

    average_time_elapsed = 0
    for i in range(0, test_run_count):
        start_time = time.time()
        increment_without_function()
        end_time = time.time()
        elapsed_time = end_time - start_time
        average_time_elapsed  += elapsed_time
        print("Time Elapsed--- %s seconds ---" % (elapsed_time))

    average_time_elapsed = average_time_elapsed / test_run_count
    print("Using Function, Average Time Elapsed--- %s seconds ---" % (average_time_elapsed))








if __name__ == "__main__":
    main()

