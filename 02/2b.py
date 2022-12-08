actions = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
}

results = {
    'lose': 0,
    'draw': 3,
    'win': 6,
}

opponent_actions = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
}

my_actions = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win',
}

score = 0
chosen_action = ''
for line in open('input.txt'):
    opponent = line[0]
    me = line[2]
    if my_actions[me] == 'draw':
        chosen_action = opponent_actions[opponent]
    elif my_actions[me] == 'win':
        if opponent_actions[opponent] == 'scissors': chosen_action = 'rock'
        if opponent_actions[opponent] == 'paper': chosen_action = 'scissors'
        if opponent_actions[opponent] == 'rock': chosen_action = 'paper'
    else:
        if opponent_actions[opponent] == 'scissors': chosen_action = 'paper'
        if opponent_actions[opponent] == 'paper': chosen_action = 'rock'
        if opponent_actions[opponent] == 'rock': chosen_action = 'scissors'
    score += results[my_actions[me]] + actions[chosen_action]

print(f"score: {score}")