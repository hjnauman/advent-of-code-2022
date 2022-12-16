def determine_score(game_round):
    def determine_choice(elf_choice, strategy):
        choices = ['A', 'B', 'C']

        # Lose
        if strategy == 'X':
            return choices[choices.index(elf_choice) - 1]
        # Win
        elif strategy == 'Z':
            return choices[(choices.index(elf_choice) + 1) % 3]
        # Draw
        else:
            return elf_choice

    # CHOICES: A - ROCK, B - PAPER, C - SCISSORS
    # GAME STATES: X - LOSE, Y - DRAW, Z - WIN
    game_states_points = {
        'X' : 0,
        'Y' : 3,
        'Z' : 6
    }

    choice_point = {
        'A' : 1,
        'B' : 2,
        'C' : 3
    }

    elf_choice = game_round.split()[0]
    strategy_guide_choice = game_round.split()[1]

    return game_states_points[strategy_guide_choice] + choice_point[determine_choice(elf_choice, strategy_guide_choice)]

# Read data from input file and split by round
with open(r'data\day_2_problem_0.txt', 'r') as f:
    game_rounds = f.read().splitlines()

# Sum total points gained by following strategy
total_points = 0
for game_round in game_rounds:
    total_points += determine_score(game_round)

print('Total points earned by using elf strategy: ', total_points)