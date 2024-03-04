import random

from graphics import logo, stages
from words import word_list

print(logo)
lives: int = 6
chosenWord: str = random.choice(word_list)
chosenWordList: list[str] = ["_"] * len(chosenWord)
print(f"{' '.join(chosenWordList)}")
hasGameEnded: bool = False
while not hasGameEnded:
    guessLetter: str = input("Guess a letter: ").lower()
    if guessLetter in chosenWordList:
        print(f"You already guessed {guessLetter}")
    for index in range(len(chosenWord)):
        letter: str = chosenWord[index]
        if letter == guessLetter:
            chosenWordList[index] = letter
    if guessLetter not in chosenWord:
        lives -= 1
        print(f"The letter is not in the word. Remaining lives {lives}")
        if lives == 0:
            hasGameEnded = True
            print("The word was: " + chosenWord)
            print("Game Ended")
    print(f"{' '.join(chosenWordList)}")
    if chosenWordList.count("_") == 0:
        hasGameEnded = True
        print("You win")
    print(stages[lives])
