#  Write a Python program to guess a number between 1 to 9.
# Note : User is prompted to enter a guess.
# If the user guesses wrong then the prompt appears again until the guess is correct,
#  on successful guess, user will get a "Well guessed!" message, and the program will exit.

number = 1
user_guess = int(input('Input a Number(1-9): '))

while user_guess != number:
    user_guess = int(input('Input a Number(1-9): '))
    continue
else:
    print('Well guessed!')
