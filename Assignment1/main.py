import random

def play():
    possible_options = ['R', 'P', 'S']
    computer = random.choice(possible_options)
    player = input('''Pick an option: 'R' for rock, 'P' for paper, 'S' for scissors ''').capitalize()
    
    while player not in possible_options:
        player = input('''Invalid Input Try again: Pick a weapon: 'R' for rock, 'P' for paper, 'S' for scissors ''').capitalize()
    
    if player == computer:
        print(f'player ((player)) : CPU ((computer))')
        print('Its a tie')
        return play()
    # r>s, s>p, p>r
    elif player == 'R':
       if computer == 'P':
        print(f'player ((player)) : CPU ((computer))')
        print('You lose!')
       if computer == 'S':
        print(f'player ((player)) : CPU ((computer))')
        print('You win!')
       
    elif player == 'S':
       if computer == 'R':
        print(f'player ((player)) : CPU ((computer))')
        print('You lose!')
       if computer == 'P':
        print(f'player ((player)) : CPU ((computer))')
        print('You win!')
    
    elif player == 'P':
       if computer == 'S':
        print(f'player((player)) : CPU ((computer))')
        print('You lose!')
       if computer == 'R':
        print(f'player ((player)) : CPU ((computer))')
        print('You win!')
        
play()    