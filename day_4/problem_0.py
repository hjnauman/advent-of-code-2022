# Read in data
with open(r'data\day_4.txt', 'r') as f:
    pairs = f.read().splitlines()

fully_contained_pairs = 0
for pair in pairs:
    # Split each elf by their upper and lower bounds
    elf_0 = [int(x) for x in pair.split(',')[0].split('-')]
    elf_1 = [int(x) for x in pair.split(',')[1].split('-')]

    # Perform bound checking 
    if (elf_0[0] >= elf_1[0] and elf_0[1] <= elf_1[1]) or (elf_0[0] <= elf_1[0] and elf_0[1] >= elf_1[1]):
        fully_contained_pairs += 1

print('The number of fully contained pairs was: ', fully_contained_pairs)