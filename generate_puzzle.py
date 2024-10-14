# Project 1
# Spelling Bee Game
# Hiba Mirza
# CS 111, Fall 2022, Reckinger
# Creates a game in which users need to guess as many possible words with 7 letters

global letters

# prompt user to enter 7 letters
letters = input("Enter 7 puzzle letters: ")

# user input is (changed to) all uppercase letters
letters = letters.upper()

# outputs beehive
print("--------SPELLING BEE-------")
print("--------- / ¯¯¯ \ ---------")
print("---------    " + letters[2] + "    ---------")
print("----/ ¯¯¯ \ ___ / ¯¯¯ \----")
print("----   " + letters[3] + "           " + letters[1] + "   ----")
print("----\ ___ / ¯¯¯ \ ___ /----")
print("---------    " + letters[0] + "    ---------")
print("----/ ¯¯¯ \ ___ / ¯¯¯ \----")
print("----   " + letters[4] + "           " + letters[6] + "   ----")
print("----\ ___ / ¯¯¯ \ ___ /----")
print("---------    " + letters[5] + "    ---------")
print("--------- \ ___ / ---------")