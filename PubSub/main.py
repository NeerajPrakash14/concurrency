
 
import time 
from threading import *
import random
import queue



message_queue = queue.Queue()
counter = 0
channel_to_condition_object_map = {}

# List to keep track of subscribed threads
subscribers = []


def handle_client_message(client_message):
    # Process the client message (You can add your custom logic here)
    print(f"Received message from client: {client_message}")

def get_new_condition_object(channelName):
    condition_object = Condition()
    channel_to_condition_object_map.setdefault(channelName, condition_object)
    return condition_object
 
def get_existing_condition_object(channelName):
    if channelName in channel_to_condition_object_map.keys():
        return channel_to_condition_object_map[channelName]
    else:
        return None
    

def publish(condition, message_queue ):
    # Simulate clients sending messages
    while True:
        time.sleep(0.1)
        client_message = input("Enter a message from the client (or 'q' to quit): ")
        if client_message.lower() == 'q':
            break
        with condition:
            print('Sending message to subscribers')
            message_queue.put(client_message)
            condition.notify_all()


def subscribe(condition, message_queue):
    while True:
        with condition:
            # print('Waiting for subscribed message')
            while message_queue.empty():
                condition.wait()
            message = message_queue.get()
            handle_client_message(message)
 

def create_publisher_thread(channelName):
    condition_object = get_new_condition_object(channelName)
    thread_pub = Thread(target=publish, args=(condition_object, message_queue))
    return thread_pub

def create_subscriber_thread(channelName):
    condition_object = get_existing_condition_object(channelName)
    if condition_object == None:
        return None

    thread_sub = Thread(target=subscribe, args=(condition_object, message_queue))
    return thread_sub

def create_publisher(channelName):
    thread = create_publisher_thread(channelName)
    thread.start()

def create_subscriber(channelName):
    thread = create_subscriber_thread(channelName)
    thread.start()
    subscribers.append(thread)

   
def main(channel_name, publisher_name, subscriber_count):
    create_publisher(channel_name)

    for i in range(subscriber_count):
        create_subscriber(channel_name)


# publisher_subscriber_map = {}
channel_pub_sub_map = {'prod': {'pub': 'prod','sub': 2}}





if __name__ == "__main__":

    operation = input("Enter a operation to continue (or 'q' to quit): \n 1. Create new Channel\n 2. Create new Publisher\n 3. Add new subscriber\n 4. Open existing Channel\n")
    if operation.lower() == '1':
        channel_name = input("Enter new channel name: ")
        channel_pub_sub_map.setdefault(channel_name, {'pub': None, 'sub': 0})
    
    if operation.lower() == '2':
        channel_name = input("Enter existing channel name to publish to: ")
        publisher_name = input("Enter new publisher name: ")
        channel_pub_sub_map[channel_name]['pub'] = publisher_name
    
    if operation.lower() == '3':
        channel_name = input("Enter existing channel name to subscribe to: ")
        print('Adding new subscriber into the channel -> ', channel_name)
        channel_pub_sub_map[channel_name]['sub'] += 1


    if operation.lower() == '4':
        channel_name = input("Enter existing channel name to connect to: ")
        print('Connecting to channel -> ', channel_name)
        main(channel_name, channel_pub_sub_map[channel_name]['pub'], channel_pub_sub_map[channel_name]['sub'])


# if __name__ == "__main__":

#     create_publisher('prod')


#     for i in range(2):
#         create_subscriber('prod')


#     # # Wait for the client listener thread to finish (you can use KeyboardInterrupt to stop the program)
#     #     try:
#     #         client_listener_thread.join()
#     #     except KeyboardInterrupt:
#     #         print("Program terminated.")
