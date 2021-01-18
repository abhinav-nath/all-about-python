from random import shuffle


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


def player_guess():
    guess = ''

    while guess not in ['0', '1', '2']:
        # recall input()
        guess = input('Pick a number 0, 1 or 2: ')

    return int(guess)


def check_guess(mylist, guess):
    if(mylist[guess] == 'O'):
        print('Correct guess!')
    else:
        print('Wrong! Better luck next time.')
        print(mylist)


# driver code
# O indicates the position of the ball
mylist = ['', 'O', '']

# shuffle it
shuffled_list = shuffle_list(mylist)

# get user's guess
guess = player_guess()

# check user's guess
check_guess(shuffled_list, guess)
