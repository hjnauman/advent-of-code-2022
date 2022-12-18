# Read in data
with open(r'data\day_6.txt', 'r') as f:
    data_stream = f.readline().split('\n')[0]

# Find number of characters needed to be processed before the first start-of-packet marker is detected
start_of_packet_marker = 0
for i in range(3, len(data_stream)):
    if len(set([char for char in data_stream[i-3:i+1]])) == 4:
        start_of_packet_marker = i + 1
        break

print('Start of packet marker is: ', start_of_packet_marker)