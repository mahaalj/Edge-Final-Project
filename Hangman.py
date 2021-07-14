# Edge-Final-Project
# My idea of my project is to create a game of Hangman. Where the user will have 6 tries to guess a word that is chosen randomly. The word to guess is represented by a row of dashes. If the player guess a letter which exists in the word, the it will appear in the correct position where it exists.  An image of the actual hangman will be printed whenever the user gets an answer wrong to show the have many tries are left


import random
from words import words

hangman_image = ['_',
                    '__',
                    '__\n |',
                    '__\n |\n O',
                    '__\n |\n O\n |',
                    '__\n |\n O\n/|',
                    '__\n |\n O\n/|\ ',
                    '__\n |\n O\n/|\ \n/',
                    '__\n |\n O\n/|\ \n/ \ '
                    ]

number_mistake = 0
letters_guessed = []
trials = len(hangman_image)
word = random.choice(words)
word_letters = list(word)
wrong_letters = []

print ()
print ('Welcome to Hangman! your word has {} letters'.format(len(word_letters)))

while number_mistake < trials:
    print()
    print('Wrong letters: ', end='')
    for letter in wrong_letters:
        print('{}, '.format(letter), end='')
    print()
    print('You have {} guesses left'.format(trials - number_mistake))
    player_letter = input ('Please enter a letter: ')


    while player_letter in letters_guessed or player_letter in wrong_letters:
        print()
        print('This letter has already been guessed, Try another letter')
        player_letter = input('Please enter a letter: ')

    if player_letter not in word_letters:
        number_mistake += 1
        wrong_letters.append(player_letter)

    print()
    print('Word: ', end='')

    for letter in word_letters:
        if player_letter == letter:
            letters_guessed.append(player_letter)

    for letter in word_letters:
        if letter in letters_guessed:
            print(letter + ' ', end='')
        else:
            print('_ ', end='')

    print()
    if number_mistake:
        print(hangman_image[number_mistake -1])
        print()


    if len(letters_guessed) == len(word_letters):
        print()
        print('Congratulations, You won !')
        break

if number_mistake == trials:
    print()
    print('Unfortunately, You Have Lost, Try Again!')



