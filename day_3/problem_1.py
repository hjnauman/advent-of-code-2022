def get_overlap_char(rucksack_0, rucksack_1, rucksack_2):
    for char in rucksack_0:
        if char in rucksack_1 and char in rucksack_2:
            return char

def get_char_priority(char):
    # Using ascii value manipulation to get priority values
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38

def get_overlap_priority(group_rucksacks):
    # Send each rucksack from a given group into the overlap char function
    overlapping_char = get_overlap_char(group_rucksacks[0], group_rucksacks[1], group_rucksacks[2])
    
    if overlapping_char is None:
        return 0

    return get_char_priority(overlapping_char)

# Read data
with open(r'data\day_3.txt', 'r') as f:
    rucksacks = f.read().splitlines()

priority_sum = 0
for i in range(0, len(rucksacks) + 1, 3):
    if i == 0:
        continue
    else:
        overlap_priority = get_overlap_priority(rucksacks[i-3:i])
        priority_sum += overlap_priority

print('The sum of priority items in rucksacks was: ', priority_sum)