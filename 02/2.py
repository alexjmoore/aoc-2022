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
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors',
}

score = 0
for line in open('input.txt'):
    opponent = line[0]
    me = line[2]
    if my_actions[me] == opponent_actions[opponent]:
        outcome = 'draw'
    elif \
        (my_actions[me] == 'rock' and opponent_actions[opponent] == 'scissors') or \
        (my_actions[me] == 'paper' and opponent_actions[opponent] == 'rock') or \
        (my_actions[me] == 'scissors' and opponent_actions[opponent] == 'paper'):
        outcome = 'win'
    else:
        outcome = 'lose'
    score += results[outcome] + actions[my_actions[me]]

print(f"score: {score}")