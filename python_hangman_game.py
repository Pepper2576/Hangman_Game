import random

word = ["apple", "banana", "orange", "grape", "pear", "house", "chair", "table", "book", "pen", "lamp", "phone", "watch", "radio", "music", "movie", "game", "show", "sport", "food"]
chosen_word = random.choice(word)
word_list = list(chosen_word)
correct_guess = []
incorrect_guess_list = []
user_guess_list = []
lives = 11


for i in range(len(word_list)):
    correct_guess.append('_')

while(True):
    
    print(f"Your word is {correct_guess}")

    user_guess = input("Guess a letter\n").lower()

    if user_guess_list.count(user_guess) == 0:

        user_guess_list.append(user_guess)

        if user_guess in word_list:
            print("Correct")
            for i in range(len(word_list)):
                if user_guess == word_list[i]:
                    correct_guess[i] = user_guess
            if correct_guess.count('_') == 0:
                print(f"You win\nyour word was '{chosen_word.upper()}'")
                break
        else:
            lives = lives - 1
            incorrect_guess_list.append(user_guess)
            if lives == 0:
                print(f"game over\nyour word was '{chosen_word.upper()}'")
                break
            else:
                print(f"nope, {lives} left\nIncorrect guesses {incorrect_guess_list}")
    else:
        print(f'You\'ve already guessed that letter:\n{user_guess_list}')