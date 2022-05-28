import random
import time
import os

def main():
    #Functionality to get the words from text file and initialize parameters
    try:
        file_handle=open('words.txt')
        words=file_handle.readlines()
        word=words[random.randint(0,7780)][:-1]   ##Removing the newline character from the end
    except:
        print("Not able to read word from words file.")
    
    ## Intial Welcome Message
    os.system('CLS')
    print("Welcome to Hangman")
    time.sleep(5)
    print("I am thinking of word of length ",len(word),"characters.")
    print("You have ",len(word)+1, "incorrect turns to guess the word.")
    for letter in word:
        print("_ ",end='')
    print("")
    

    turn= len(word)+1

    guessed_letter=list()

    while turn >0:
        guess_letter=input('\nGuess the letter :').lower()  ## Taking the input and converting it into lower case
        
        ## Clearing the Screen
        os.system('CLS')

        ## Validating the input
        if len(guess_letter) != 1 or guess_letter in guessed_letter:
            if len(guess_letter) !=1 :
                print("Please enter only one alphabet !!!")
            else:
                print("You already inputed ",guess_letter," alphabet.\n")
            result=check_word(word,guessed_letter)
            for letter in result:
                print(letter, end=' ')
            
            print("\n\n Words you already inputed are :",guessed_letter)

            continue

        ## Decreasing the no of guesses    
        if guess_letter not in word:
            turn=turn-1 

        ## Adding the input to the list of guessed alphabet
        guessed_letter.append(guess_letter)

        ## Checking the result
        result=check_word(word,guessed_letter)

        for letter in result:
            print(letter, end=' ')
        print("\n\n Words you already inputed are :",guessed_letter)
        if result==word:
            print("\nYou Won with ",str(turn)," turn left !!!\n")
            exit()
        print("\nYou have ",turn, "turn left.")
    print("\nYou lost!")
    print("Word is :", word)

def check_word(word,guessed_letter):
    """
        Function to check the entered letters in orginal word
        Input : Original word and the user input word
        Output : String with the matched or not matched words
    """
    status=''
    for letter in word:
        if letter in guessed_letter:
            status+=letter
        else:
            status+='_'
    return status

if __name__=="__main__":
    main()