import random
from words import words
i = 1
fr = [0]*26
word = random.choice(words)
length = chances = len(word)
hidden = length*'_'
list(hidden)
# print(hidden)
chances += 3
changes = 0
print(word, chances, hidden)
while chances > 0:
    letter = input("Guess a letter : ")
    if fr[ord(letter)-97] > 0:
        print("You have already guessed it !")
    else:
        fr[ord(letter)-97] = 1
    for i in range(length):
        if word[i] == letter and hidden[i] != letter:
            hidden = hidden[0:i]+letter+hidden[i+1:length]
            changes += 1
    print(hidden)
    if changes == length:
        print("You won !")
        chances = 0
    chances -= 1
if chances > -1:
    print("You lost !")
    print(f"Hidden word was : {word}")
