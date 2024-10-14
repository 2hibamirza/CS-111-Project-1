# Project 1
# Spelling Bee Game
# Hiba Mirza
# CS 111, Fall 2022, Reckinger
# Creates a game in which users need to guess as many possible words with 7 letters

global dictionary, word, score, words_list, scores_list

# prompts user for word that solves the puzzle
word = str(input("Word: "))

# assign the score associated with the word
score = dictionary[word]

# output score
print("Score for " + word + ":", int(score))

# add new score
scores_list.append(score)

# add new word
words_list.append(word)
