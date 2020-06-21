#You can also change 'choosen' list for more words in this game
import random
def menu():
    print('H A N G M A N')
    action = input('Type "play" to play the game, "exit" to quit:')
    if action == 'play':
        game()
    elif action == 'exit':
        pass


def game():
    print()
    choosen = list(random.choice(['python', 'java', 'kotlin', 'javascript']))
    hidden = list(len(choosen) * '-')
    count = 0
    tried_letters_list = []
    while count < 8:
        print()
        print(''.join(hidden))
        guess = input('Input a letter:')
        if len(guess) != 1:
            print('You should input a single letter')
        elif guess.islower() == False:
            print('It is not an ASCII lowercase letter')
        elif guess in hidden or guess in tried_letters_list:
            print('You already typed this letter')
        elif guess in choosen:
            for i in range(len(choosen)):
                if choosen[i] == guess:
                    hidden[i] = guess
        else:
            print('No such letter in the word')
            tried_letters_list.append(guess)
            count += 1
        if hidden == choosen:
            print(f'You guessed the word {"".join(choosen)}!')
            print('You survived!')
            break
    if count == 8:
        print('You are hanged!')


menu()