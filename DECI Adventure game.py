import time
import random

def print_pause(message, delay=1):
    """
    Prints a message with a delay.

    Args:
        message (str): The message to be printed.
        delay (float, optional): The delay in seconds before printing the message.
                                 Defaults to 1.
    """
    print(message)
    time.sleep(delay)

def introduction():
    """
    Introduces the player to the game.
    """
    print_pause("Welcome to the Text-Based Adventure Game!")
    print_pause("You find yourself in a dark forest, unsure of how you got here.")
    print_pause("You must make choices to navigate through the forest and reach safety.")

def choice1():
    """
    Presents the first choice to the player.
    """
    global total_score
    print_pause("You come across a fork in the path. Which way do you go?")
    print_pause("1. Take the left path.")
    print_pause("2. Take the right path.")

    while True:
        choice = input("Enter 1 or 2: ")
        if choice == "1":
            print_pause("You follow the left path and come across a friendly bear.")
            print_pause("The bear helps you find your way out of the forest.")
            total_score += 50
            print_pause(f"Your total score: {total_score}")
            print_pause("Congratulations, you have completed the game!")
            break
        elif choice == "2":
            print_pause("You follow the right path and stumble upon a dangerous mountain lion.")
            print_pause("The mountain lion attacks you, and you are unable to escape.")
            total_score -= 20
            print_pause(f"Your total score: {total_score}")
            print_pause("Game over.")
            break
        else:
            print_pause("Invalid input. Please enter 1 or 2.")

def choice2():
    """
    Presents the second choice to the player.
    """
    global total_score
    print_pause("You continue on the path and come across a lake.")
    print_pause("What do you do?")
    print_pause("1. Try to swim across the lake.")
    print_pause("2. Look for a way around the lake.")

    while True:
        choice = input("Enter 1 or 2: ")
        if choice == "1":
            print_pause("You dive into the lake, but the current is too strong.")
            print_pause("You are swept away and drown.")
            total_score -= 30
            print_pause(f"Your total score: {total_score}")
            print_pause("Game over.")
            break
        elif choice == "2":
            print_pause("You find a narrow bridge crossing the lake.")
            print_pause("You safely cross the bridge and continue on your path.")
            total_score += 20
            print_pause(f"Your total score: {total_score}")
            random_event()
            break
        else:
            print_pause("Invalid input. Please enter 1 or 2.")

def random_event():
    """
    Implements a random event during the game.
    """
    global total_score
    events = ["storm", "clear skies", "fog"]
    random_event = random.choice(events)

    if random_event == "storm":
        print_pause("As you walk further, a sudden storm hits the forest.")
        print_pause("You take shelter under a large tree until the storm passes.")
        total_score -= 10

    elif random_event == "clear skies":
        print_pause("The weather is clear and the sun shines brightly.")
        print_pause("You make good progress through the forest.")
        total_score += 10

    elif random_event == "fog":
        print_pause("Thick fog engulfs the forest, making it difficult to see.")
        print_pause("You navigate cautiously, trying to stay on the right path.")
        total_score -= 5

    choice3()

def choice3():
    """
    Presents the third choice to the player.
    """
    global total_score
    print_pause("You come across a cabin in the forest.")
    print_pause("What do you do?")
    print_pause("1. Knock on the door and see if anyone is home.")
    print_pause("2. Continue on the path and leave the cabin alone.")

    while True:
        choice = input("Enter 1 or 2: ")
        if choice == "1":
            print_pause("You knock on the door, and an old man opens it.")
            print_pause("The old man offers you shelter and a warm meal.")
            print_pause("You accept his offer and rest before continuing your journey.")
            total_score += 30
            print_pause(f"Your total score: {total_score}")
            print_pause("Congratulations, you have completed the game!")
            break
        elif choice == "2":
            print_pause("You decide to leave the cabin alone and continue on the path.")
            print_pause("You eventually find your way out of the forest.")
            total_score += 15
            print_pause(f"Your total score: {total_score}")
            print_pause("Congratulations, you have completed the game!")
            break
        else:
            print_pause("Invalid input. Please enter 1 or 2.")

def play_game():
    """
    Starts the game and guides the player through the choices.
    """
    global total_score
    total_score = 0
    introduction()
    choice1()
    choice2()

def main():
    """
    Allows the player to restart or exit the game.
    """
    while True:
        play_game()
        print_pause("Would you like to play again?")
        restart = input("Enter 'y' to play again or 'n' to exit: ")
        if restart.lower() != 'y':
            print_pause(f"Your final score: {total_score}")
            print_pause("Thank you for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()