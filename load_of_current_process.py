# load_of_current_process.py

# import psutil
# import os

# process_id = os.getpid()
# print("Current Process ID:", process_id)


# def get_process_cpu_load(process_id, core_id):
#     process = psutil.Process(process_id)
#     cpu_times = process.cpu_times()
#     cpu_count = psutil.cpu_count(logical=False)
#     core_load = cpu_times[core_id] / (cpu_count * cpu_times.elapsed)
#     return core_load

# # Usage example
# process_id = process_id  # Replace with the actual process ID
# core_id = 0  # Replace with the core ID you want to monitor

# load = get_process_cpu_load(process_id, core_id)
# print(f"Load on Core {core_id}: {load:.2%}")


# import psutil

# # Get the process ID of the current process
# pid = psutil.Process().pid



# # Get CPU utilization percentage for the current process
# cpu_percent = psutil.Process(pid).cpu_percent()

# print("CPU Load of the current process:", cpu_percent)


# import psutil
# import random

# # Generate some random math calculations
# numbers = [random.randint(1, 100) for _ in range(1000000)]

# # Get the process ID of the current process
# pid = psutil.Process().pid

# # Get CPU utilization percentage for the current process
# cpu_percent = psutil.Process(pid).cpu_percent()
# result = sum(numbers)


# print("Result of calculations:", result)
# print("CPU Load of the current process:", cpu_percent)


import psutil
import random
import time

# Generate some random math calculations
numbers = [random.randint(1, 100) for _ in range(1000000)]
result = sum(numbers)

# Get the process ID of the current process
pid = psutil.Process().pid

# Delay to allow CPU utilization
time.sleep(0.5)

# Get CPU utilization percentage for the current process
cpu_percent = psutil.Process(pid).cpu_percent()

print("Result of calculations:", result)
print("CPU Load of the current process:", cpu_percent)
