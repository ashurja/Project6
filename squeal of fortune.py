# Jamshed Ashurov
# 10/06/2017
# nym.py
# This program creates a game of Squeal of Fortune

import random


def wordchoice():
    """
    This function imports the list of words that I downloaded from the Internet and selects the word from that list.
    :return:
    """
    mylist = open("squeal of fortune.txt", "r")
    wordfile = mylist.readlines()
    word = random.choice(wordfile)
    mylist.close()
    return word[:-1]


def main():
    play = input("Would you like to play a game of Squeal of Fortune? (y/n)")
    while play != "n":
        word = wordchoice()
        emptylist = []
        for x in word:
            emptylist.append("_")
        progress = " ".join(emptylist)
        print(progress)
        num_of_guess = 6
        while True:
            guess = input("Please guess a letter")
            if guess not in word:
                num_of_guess = num_of_guess - 1
            for x in range(len(word)):
                if guess == word[x]:
                    emptylist[x] = word[x]
            print("You have", num_of_guess, "guess(es) left")
            progress = " ".join(emptylist)
            print(progress)
            if "_" not in emptylist:
                print("Congratulations, you guessed the word.")
                break
            elif num_of_guess == 0:
                print("Ohh, I am so sorry, but you ran out of your guesses. The actual word is", word)
                break
        play = input("Would you like to play a game of Squeal of Fortune? (y/n)")
    print("Oh well, next time then")

main()
