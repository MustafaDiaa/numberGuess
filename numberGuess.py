high = int(raw_input('Put any highest guess for your number: '))


def numberGuess(high):		#function definition, given highest guess as input
    low = 0					#lowest guess = 0
    ans = (low + high) / 2	#answer is the average of both low & high guess
    guessNO = 0

    print 'Please think of a number between 0 and ' + str(high) + '!'
    print 'Is your secret number ' + str(ans) + '?'
    responce = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

##########################################################################################
    while responce != 'c':
##############################
        if responce == 'h':		#if the answer is high, let it the highest guess
            high = ans

        elif responce == 'l':
            low = ans			#if the answer is low, let it the lowest guess
        
        else:
            print 'Sorry, I did not understand your input.'		#if input is not (l or h) print statement
        guessNO += 1
##############################
        ans = (high+low) / 2		#take the average of (low & high) and assign it to answer
        print 'Is your secret number ' + str(int(ans)) + '?'
        responce = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
##########################################################################################
    if responce == 'c':		#if user responce equal 'c', end program
        print 'Game over. Your secret number was: ' + str(int(ans))
    print('number of guesses is: ') + str(guessNO)
    return ans
numberGuess(high)		#highest guess is given as input, put whatever you like!
