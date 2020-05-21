import random

def main():
    try:
        file_handle=open('words.txt')
        words=file_handle.readlines()
        word=words[random.randint(0,7780)][:-1]
    except:
        print("Not able to read word from words file.")
    
    print("Welcome to Hangman Game")
    print("I am thinking of letter of length ",len(word),"characters.")
    print("You have ",len(word)+1, "incorrect turns to guess the word.")
    for letter in word:
        print("_ ",end='')
    print("")
    

    turn= len(word)+1

    guessed_letter=list()

    while turn >0:
        guess_letter=input('\nGuess the letter :')
        if guess_letter not in word:
            turn=turn-1
        
        guessed_letter.append(guess_letter)
        result=check_word(word,guessed_letter)
        for letter in result:
            print(letter, end=' ')
        if result==word:
            print("\nYou Won !!!")
            exit()
        print("\nYou have ",turn, "left.")
    print("\nYou lost!")
    print("Word is :", word)

def check_word(word,guessed_letter):
    status=''
    for letter in word:
        if letter in guessed_letter:
            status+=letter
        else:
            status+='_'
    return status



if __name__=="__main__":
    main()