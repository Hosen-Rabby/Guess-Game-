from random import randint
# generate a number from 1~10
answer = randint(1, 10)
while True:
    try:
        # input from user
        guess = int(input('Guess a number 1~10: '))
        # check that input is a number
        if 0 < guess < 11:
            # check if input is a right guess
            if guess == answer:
                print('Correct, you are a genius!')
                break
        else:
            print('Hey, are you insane! I said 1~10')
    except ValueError:
        print('Please enter number')
