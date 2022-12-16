def get_overlap_char(compartment_0, compartment_1):
    for char in compartment_0:
        if char in compartment_1:
            return char

def get_char_priority(char):
    # Using ascii value manipulation to get priority values
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38

def get_overlap_priority(rucksack):
    # Split rucksack into compartment
    compartment_0 = rucksack[0:int(len(rucksack)/2)]
    compartment_1 = rucksack[int(len(rucksack)/2):-1]

    overlapping_char = get_overlap_char(compartment_0, compartment_1)
    
    if overlapping_char is None:
        return 0

    return get_char_priority(overlapping_char)

# Read data
with open(r'data\day_3.txt', 'r') as f:
    rucksacks = f.read().splitlines()

priority_sum = 0
for rucksack in rucksacks:
    overlap_priority = get_overlap_priority(rucksack)
    priority_sum += overlap_priority

print('The sum of priority items in rucksacks was: ', priority_sum)