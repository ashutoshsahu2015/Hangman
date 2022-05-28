# Hangman Game

## Description
A classic word guessing game where a player attempt to build a missing word by guessing one letter at a time.The word to guess is represented by a row of dashes.If the player guess a letter which exists in the word, the script writes it in all its correct positions.The player has incorrect guess equal to length of word + 1.

## How to run the program
 **You can start the game by running the following command :**
 ```
 python hangman.py
 ```
## Functionality

The script will get the random word from the text file name words.txt and ask the player to enter the characters.If the player guess a character which exists in the word, the script writes it in all its correct positions. When the user enters the wrong guess more than the limit then the script displayed the output message as "You Lost !!" and also print out the correct word.

Also the input validation such as entering two alphabet at a time and entering no alphabet is handled in the program.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
