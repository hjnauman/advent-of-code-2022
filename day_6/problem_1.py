# Read in data
with open(r'data\day_6.txt', 'r') as f:
    data_stream = f.readline().split('\n')[0]

# Find number of characters need to be processed before the first start-of-message marker is detected
start_of_message_marker = 0
for i in range(13, len(data_stream)):
    if len(set([char for char in data_stream[i-13:i+1]])) == 14:
        start_of_message_marker = i + 1
        break

print('Start of message marker is: ', start_of_message_marker)