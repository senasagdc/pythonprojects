import hangman_words
import hangman_art
import random

print("welcome to hangman game! ")
game_word = random.choice(hangman_words.word_list)
game_lives = 6
game_over = False

blank = ""
for i in range(0, len(game_word)):
    blank += "_"
print("your word is:" + blank)
#to check the word: print(game_word)

re_word = list("_" * len(game_word))
guessed_letters = []

while not game_over:
    user_guess = input("Please guess a letter: ").lower()
    if len(user_guess) != 1 or not user_guess.isalpha():
        print("Please enter a single letter.")
        continue

    if user_guess in guessed_letters:
        print(f"You already guessed '{user_guess}'. Try a different letter.")
        continue
    guessed_letters.append(user_guess)

    if user_guess in game_word:
        for i in range(0, len(game_word)):
            if game_word[i] == user_guess:
                re_word[i] = user_guess
        print("".join(re_word))

        if "_" not in re_word:
            print("You win! The word was:", game_word)
            game_over = True
    else:
        game_lives -= 1
        print("it's wrong!! remaining life: " + str(game_lives))
        print(hangman_art.stages[game_lives])
        if game_lives < 1:
            game_over = True
            print("game 
