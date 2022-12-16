# Read data from input file split by elf
with open(r'data\day_1_problem_0.txt', 'r') as f:
    elves_calorie_list = f.read().split('\n\n')

# Sum the total number of calories held by each elf and update the list
for elf_num, elf_snack_calories in enumerate(elves_calorie_list):
    elves_calorie_list[elf_num] = sum([int(x) for x in elf_snack_calories.split('\n') if x != ''])

print('The most calories held by a single elf was: ', max(elves_calorie_list))
