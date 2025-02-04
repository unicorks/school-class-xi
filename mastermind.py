import random
# picks out a code
code = [str(random.randrange(1, 7)) for i in range(4)]
hint = []
turn = 1

print("""Hello and welcome to Mastermind on the command line against the computer! 
- The computer picks out a 4 digit code (rep allowed) with digits 1-6, your task is to guess the code using the hints given after each guess
- Please enter your guess in the form '1234' where each digit of the guess is a number from 1-6
- There can be any duplicate digits in the code
- For the hints, 'p' will be shown for a perfect guess, 'e' will be shown for a guess which exists in the code
- There are 12 maximum turns to guess the code\n\n
LET THE GAME BEGIN!""")


while ''.join(hint) != 'pppp' and turn <= 12:
    # initialises hint variable, asks for user's guess
    hint = []
    guess = list(input(f'Enter your guess no {turn}: '))

    # sanitises the input
    if len(guess) != 4:
        print('Your guess was invalid, try again.')
        continue
    try:
        e = int(''.join(guess))
    except:
        print('Your guess was invalid, try again.')
        continue
    
    # hint mechanism
    # creates copy of the guess and code variables
    # first checks for perfect guesses, replaces their places with placeholder A
    # then checks if any other numbers in the guess exist in the code, also replaces them with placeholder
    # appends p to hints for perfect guess, e for exists
    guess_2 = guess.copy()
    code_2 = code.copy()
    for i in range(0, len(guess)):
        if guess[i] == code[i]:
            guess_2[i]= 'A'
            code_2[i] = 'A'
            hint.append('p')
    for i in range(len(guess)):
        if guess_2[i] != 'A':
            if (guess_2[i] in code_2):
                code_2[code_2.index(guess_2[i])] = 'A'
                guess_2[i]='A'
                hint.append('e')

    turn += 1
    random.shuffle(hint)
    print(f'Hint: {''.join(hint)}')

# win/lose
if ''.join(hint) == 'pppp':
    print("CONGRATS YOU WON!")
else:
    print("YOU LOST")
    print(f'The code was {''.join(code)}')