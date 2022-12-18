def get_stacks(input_txt):
    stacks = []

    for line_num, line in enumerate(input_txt):
        # Indicates the bottom of all stacks
        if line.startswith(' 1'):
            num_stacks = len(line.split())

            # Create empty stacks
            for i in range(num_stacks):
                stacks.append([])

            # Reverse through lines and append to each stack
            for i in range(line_num - 1, -1, -1):
                # The first element of each stack starts on index 1 of the string and increments by 4 for each stack
                element_index = 1

                # Check each stack for a possible value and add it if it exists
                for j in range(num_stacks):
                    if input_txt[i][element_index] != ' ':
                        stacks[j].append(input_txt[i][element_index])

                    element_index += 4

    return stacks

def get_instructions(input_txt):
    # Creates instructions list of list where each instruction is formatted as given in the below example
    # move 1 from 5 to 1 -> [1,5,1]
    instructions = []

    for line in input_txt:
        if line.startswith('move'):
            line_elements = line.split()
            instruction = []

            for element in line_elements:
                if element.isnumeric():
                    instruction.append(int(element))

            instructions.append(instruction)

    return instructions

# Read and parse data
with open(r'data\day_5.txt', 'r') as f:
    lines = f.readlines()

# Get initial data structure and instructions
stacks = get_stacks(lines)
instructions = get_instructions(lines)

# Perform move operations
for instruction in instructions:
    elements_to_move = instruction[0]
    source_stack = instruction[1] - 1
    destination_stack = instruction[2] - 1

    for i in range(elements_to_move):
        stacks[destination_stack].append(stacks[source_stack].pop())

output = ''
for stack in stacks:
    output += stack[-1]

print('The final message is: ', output)