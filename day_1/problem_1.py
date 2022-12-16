# Read data from input file split by elf
with open(r'data\day_1.txt', 'r') as f:
    elves_calorie_list = f.read().split('\n\n')

# Sum the total number of calories held by each elf and update the list
for elf_num, elf_snack_calories in enumerate(elves_calorie_list):
    elves_calorie_list[elf_num] = sum([int(x) for x in elf_snack_calories.split('\n') if x != ''])

# Find the max value of the top three elves and sum their calorie results while reporting the elf calorie values
top_three_elves_total_calories = 0

for i in range(3):
    current_max_calorie = max(elves_calorie_list)
    print('Elf ', i+1, ' had ', current_max_calorie, ' calories.')
    top_three_elves_total_calories += current_max_calorie
    elves_calorie_list.remove(current_max_calorie)

print('Top three elves calorie sum: ', top_three_elves_total_calories)