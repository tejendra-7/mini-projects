import random

def play_game():
    number = random.randint(1, 100)
    chances = 10
    # you can edit the number of chances in the above line
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while chances > 0:
        guess = int(input("Take a guess: "))

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number!")
            break   

        chances -= 1
        print(f"You have {chances} chances left.")

    if chances == 0:
        print(f"Game over! The number was {number}.")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_game()
    else:
        print("Thank you for playing!")

play_game()