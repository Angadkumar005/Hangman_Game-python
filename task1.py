import random

# Word categories
categories = {
    "fruits": ["apple", "banana", "grape", "orange", "mango"],
    "animals": ["tiger", "elephant", "giraffe", "rabbit", "lion"],
    "tech": ["python", "laptop", "keyboard", "server", "router"]
}

def choose_category():
    print("\n📂 Choose a category:")
    for idx, cat in enumerate(categories, start=1):
        print(f"{idx}. {cat.title()}")
    while True:
        try:
            choice = int(input("Enter number (1-3): "))
            if 1 <= choice <= len(categories):
                selected = list(categories.keys())[choice - 1]
                print(f"\n✅ You selected: {selected.title()}")
                return selected
            else:
                print("❌ Invalid choice.")
        except ValueError:
            print("❌ Please enter a number.")

def display_current_state(display_word, guessed_letters, tries, score):
    print("\n" + "-"*40)
    print("Word: ", " ".join(display_word))
    print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    print(f"Tries left: {tries}")
    print(f"⭐ Score: {score}")
    print("-"*40)

def play_game(score):
    category = choose_category()
    chosen_word = random.choice(categories[category])
    display_word = ["_" for _ in chosen_word]
    guessed_letters = []
    tries = 6

    print("\n🎯 Let's play Hangman!")
    print(f"🔤 Guess the word from category: {category.upper()}")

    while tries > 0 and "_" in display_word:
        display_current_state(display_word, guessed_letters, tries, score)
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ Already guessed.")
            continue

        guessed_letters.append(guess)

        if guess in chosen_word:
            print("✅ Nice!")
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    display_word[i] = guess
        else:
            tries -= 1
            print("❌ Nope.")

    # Game result
    if "_" not in display_word:
        print("\n🎉 You guessed it! The word was:", chosen_word)
        score += 1
    else:
        print("\n💀 You failed! The word was:", chosen_word)

    return score

def hangman():
    score = 0
    while True:
        score = play_game(score)
        again = input("\n🔁 Play again? (y/n): ").lower()
        if again != 'y':
            print(f"\n🏁 Final Score: {score}")
            print("👋 Thanks for playing Hangman!")
            break
            

# Run the game
hangman()
