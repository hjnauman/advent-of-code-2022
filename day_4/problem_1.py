# Read in data
with open(r'data\day_4.txt', 'r') as f:
    pairs = f.read().splitlines()

overlapping_pairs = 0
for pair in pairs:
    # Create set of values for range of lower and upper bounds
    elf_0 = {x for x in range(int(pair.split(',')[0].split('-')[0]), int(pair.split(',')[0].split('-')[1]) + 1)}
    elf_1 = {x for x in range(int(pair.split(',')[1].split('-')[0]), int(pair.split(',')[1].split('-')[1]) + 1)}

    # Perform bound checking by using set intersection
    if len(elf_0.intersection(elf_1)) > 0:
        overlapping_pairs += 1 


print('The number of overlapping pairs was: ', overlapping_pairs)