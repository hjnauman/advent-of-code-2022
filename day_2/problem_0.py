def determine_score(game_round):
    # CHOICES: A/X - ROCK, B/Y - PAPER, C/Z - SCISSORS
    # Loss states are insignificant as the key won't exist and we can just assign zero
    game_states_points = {
        # Draws
        'A X' : 3,
        'B Y' : 3,
        'C Z' : 3,

        # Wins
        'A Y' : 6,
        'B Z' : 6,
        'C X' : 6
    }

    choice_point = {
        'X' : 1,
        'Y' : 2,
        'Z' : 3
    }

    strategy_guide_choice = game_round.split()[1]

    if game_round in game_states_points.keys():
        return game_states_points[game_round] + choice_point[strategy_guide_choice]
    return choice_point[strategy_guide_choice]


# Read data from input file and split by round
with open(r'data\day_2_data.txt', 'r') as f:
    game_rounds = f.read().splitlines()

# Sum total points gained by following strategy
total_points = 0
for game_round in game_rounds:
    total_points += determine_score(game_round)

print('Total points earned by using elf strategy: ', total_points)