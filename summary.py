global name, words_list, scores_list

# creates name variable
name = str(name)

# output
print("************************")
print("GAME OVER")
print("************************")
print("Congrats, " + name + '!')

# outputs sum of all scores
print("Final Score:", sum(scores_list))

# output 6 words along with scores for each word
print("Words played: ")
print(words_list[0] + '(' + str(scores_list[0]) + ')')
print(words_list[1] + '(' + str(scores_list[1]) + ')')
print(words_list[2] + '(' + str(scores_list[2]) + ')')
print(words_list[3] + '(' + str(scores_list[3]) + ')')
print(words_list[4] + '(' + str(scores_list[4]) + ')')
print(words_list[5] + '(' + str(scores_list[5]) + ')')