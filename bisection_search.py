highNumber = 100
lowNumber = 0
guessNumber = int((highNumber + lowNumber) / 2.0)
anwser = 'y'
print('Please think of a number between 0 and 100!')
while anwser != 'c':
    print('Is your secret number ' + str(guessNumber) + '?')
    anwser = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if anwser == 'h':
        highNumber = guessNumber
        guessNumber = int((highNumber + lowNumber) / 2.0)
    elif anwser == 'l':
        lowNumber = guessNumber
        guessNumber = int((highNumber + lowNumber) / 2.0)
    elif anwser == 'c':
        print("Game over. Your secret number was: " + str(guessNumber))
    else:
        print('Sorry, I did not understand your input.')
