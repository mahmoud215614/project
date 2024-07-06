def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest.")
    print("What do you do?")
    print("1. Go north")
    print("2. Go south")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        go_north()
    elif choice == "2":
        go_south()
    else:
        print("Invalid choice. Please try again.")
        start_game()

def go_north():
    print("You head north and discover a hidden cave.")
    print("Do you enter the cave?")
    print("1. Yes")
    print("2. No")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        enter_cave()
    elif choice == "2":
        print("You decide not to enter the cave and continue your journey.")
        start_game()
    else:
        print("Invalid choice. Please try again.")
        go_north()

def go_south():
    print("You go south and stumble upon a river.")
    print("What do you do?")
    print("1. Swim across")
    print("2. Look for a bridge")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("You attempt to swim across the river but get swept away by the current.")
        game_over()
    elif choice == "2":
        print("You find a sturdy bridge and safely cross the river.")
        start_game()
    else:
        print("Invalid choice. Please try again.")
        go_south()

def enter_cave():
    print("Inside the cave, you discover a treasure chest!")
    print("What do you do?")
    print("1. Open the chest")
    print("2. Leave the cave")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("You open the chest and find a valuable gem. Congratulations, you win!")
        play_again()
    elif choice == "2":
        print("You leave the cave and continue your journey.")
        start_game()
    else:
        print("Invalid choice. Please try again.")
        enter_cave()

def game_over():
    print("Game over. Would you like to play again?")
    print("1. Yes")
    print("2. No")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        play_again()
    elif choice == "2":
        print("Thank you for playing!")
    else:
        print("Invalid choice. Please try again.")
        game_over()

def play_again():
    print("Starting a new game...")
    start_game()

# Start the game
start_game()