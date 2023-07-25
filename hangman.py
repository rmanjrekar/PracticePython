'''In the real hangman game, each time we lose a life, the drawing of the hangman is completed
limb by limb. But in our case, we will simply tell the user that they have six lives, and we will deduct them one by one for each time the player chooses an incorrect letter.
If the player runs out of lives before guessing the word, the player loses. But if they guessed
the whole word before losing all their lives, the player wins.'''

from random import choice
import string
import sys


word_list = ['Hello','Change','World','Letter']
total_lives = 6
def get_a_word(list1):

    """
        Selects the word from the input list and returns the word and 
        list in the form of '_' as per alphabet count 
    """
    selected_word = choice(list1) # will randomly select the word for word_list
    length = len(selected_word)
    str1 = ""
    i = 0
    while i < length:
        str1 = str1 + " _ "    # to show number of alphabets
        i += 1
    print(str1)
    string_list = str1.split()
    return selected_word, string_list

def ask_user_to_enter(selected_word, string_list):
    """
        Takes input from user and prints the result as per the input
    """
    alphabet_list = list(selected_word)
    i = 1
    user_entered_list=[]
    wrong_letter_list=[]
    while(i<=6):
        letter = input('Guess the alphabet ')
        valid_letter = list(string.ascii_letters)
        if letter not in user_entered_list:
            if letter not in valid_letter:
                print("Incorrect letter, Renter!")
            elif letter in alphabet_list:
                print("Correct Letter")
                user_entered_list.append(letter)
                display_letter(letter, alphabet_list, string_list)
            else:
                print("You have entered wrong letter")
                wrong_letter_list.append(letter)
                lives = total_lives - i
                print("Wrong alphabets list guessed so far: ", wrong_letter_list)
                print(f"You have {lives} lives")
                i += 1
    print("You Lost!!!")
    sys.exit()

def display_letter(letter, alphabet_list, string_list):

    num = 0
    for l in alphabet_list:
        if letter == l:
            string_list[num] = letter
        num += 1
    print("Alphabet Guessed so far " , string_list)
    if "_" not in string_list:
        print("You Won!!!")
        sys.exit()

selected_word, string_list = get_a_word(word_list)
ask_user_to_enter(selected_word, string_list)
