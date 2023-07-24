
from PubSub.main import main


publisher_subscriber_map = {}
channel_pub_sub_map = {}





if __name__ == "__main__":

    operation = input("Enter a operation (or 'q' to quit): \n 1. Create new Channel\n 2. Create new Publisher\n 3. Add new subscriber\n 4. Open existing Channel")
    if operation.lower() == '1':
        channel_name = input("Enter new channel name")
        channel_pub_sub_map.setdefault(channel_name, {'pub': None, 'sub': 0})
    
    if operation.lower() == '2':
        channel_name = input("Enter existing channel name to publish to")
        publisher_name = input("Enter new publisher name")
        channel_pub_sub_map[channel_name]['pub'] = publisher_name
    
    if operation.lower() == '3':
        channel_name = input("Enter existing channel name to subscribe to")
        print('Adding new subscriber into the channel -> ', channel_name)
        channel_pub_sub_map[channel_name]['sub'] += 1


    if operation.lower() == '4':
        channel_name = input("Enter existing channel name to connect to")
        print('Connecting to channel -> ', channel_name)
        main(channel_name, channel_pub_sub_map[channel_name]['pub'], channel_pub_sub_map[channel_name]['sub'])
    




