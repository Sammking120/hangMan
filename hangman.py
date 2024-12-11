from random import choice


def run_game():
    word: str = choice(['apple','secret','banana'])

    username:str =input("What is your Name? >>>> ")

    print(f'Welcome to the Hangman,{username}!')

    #Setup

    guessed:str = ''
    tries:int = 3

    while tries> 0:
        blanks: int =0


        print('Word: ', end='')

        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('_', end ='')
                blanks+=1

        print() #Adds a blank  line

        if blanks == 0:
            print('You got it right!')
            break  
        
        
        try:
            guess:str = input('Enter a letter: ')
            assert len(guess) <= 3, print("You Entered More Than 5 characters")
            assert all('a' <= i <= 'z' for i in guess), print('Characters other than a-z are found')
        except Exception as e:
            pass
        

        if guess in guessed:
            print(f'You have already used: "{guess}". Please try with another letter!')
            continue

        guessed+= guess
        

        if guess not in word:
            tries -=1
            print(f'Sorry, that was wrong...{tries} tries remaining')

            if tries == 0:
                print('No more tries reamining... You Lost the game')
                break


if __name__ == '__main__':
    run_game()