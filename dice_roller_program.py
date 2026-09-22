# Python Dice Roller Game
import random

# ● ┌ ─ ┐ │ └ ┘

# DICE ART
dice_faces = {
    1: [
        "┌─────────────┐",
        "│             │",
        "│             │",
        "│      ●      │",
        "│             │",
        "│             │",
        "└─────────────┘"
    ],
    2: [
        "┌─────────────┐",
        "│  ●          │",
        "│             │",
        "│             │",
        "│             │",
        "│           ● │",
        "└─────────────┘"
    ],
    3: [
        "┌─────────────┐",
        "│ ●           │",
        "│             │",
        "│      ●      │",
        "│             │",
        "│           ● │",
        "└─────────────┘"
    ],
    4: [
        "┌─────────────┐",
        "│  ●       ●  │",
        "│             │",
        "│             │",
        "│             │",
        "│  ●       ●  │",
        "└─────────────┘"
    ],
    5: [
        "┌─────────────┐",
        "│  ●       ●  │",
        "│             │",
        "│      ●      │",
        "│             │",
        "│  ●       ●  │",
        "└─────────────┘"
    ],
    6: [
        "┌─────────────┐",
        "│  ●       ●  │",
        "│             │",
        "│  ●       ●  │",
        "│             │",
        "│  ●       ●  │",
        "└─────────────┘"
    ]
}

# DISPLAY DICE
def display_dice(rolls):
    for row in range(7):
        for roll in rolls:
            print(dice_faces[roll][row], end="  ")

        print()

# GET NUMBER OF DICE
def get_number_of_dice():
    while True:
        try:
            number = int(input("How many dice do you want to roll? "))

            if number > 0:
                return number

            print("❌ Please enter a number greater than 0.")

        except ValueError:
            print("❌ Please enter a valid number.")

# SIMPLE DICE ROLLER
def simple_dice_roller():

    print("\n🎲 SIMPLE DICE ROLLER")
    print("-" * 30)

    number_of_dice = get_number_of_dice()

    rolls = []

    for _ in range(number_of_dice):
        roll = random.randint(1, 6)
        rolls.append(roll)

    print("\n🎲 Your dice:\n")

    display_dice(rolls)

    total = sum(rolls)

    print(f"\nTotal: {total}")

# DICE BATTLE
def dice_battle():
    print("\n⚔️ DICE BATTLE")
    print("-" * 30)

    number_of_dice = get_number_of_dice()

    player_rolls = []
    computer_rolls = []

    for _ in range(number_of_dice):

        player_roll = random.randint(1, 6);
        computer_roll = random.randint(1, 6);

        player_rolls.append(player_roll)
        computer_rolls.append(computer_roll)

    print("\n👤 PLAYER:\n")

    display_dice(player_rolls)

    player_total = sum(player_rolls)

    print(f"\nPlayer total: {player_total}")

    print("\n💻 COMPUTER:\n")

    display_dice(computer_rolls)

    computer_total = sum(computer_rolls)

    print(f"\nComputer total: {computer_total}")

    print("\n" + "-" * 30)

    if player_total > computer_total:
        print("🏆 YOU WIN!")

    elif player_total < computer_total:
        print("💻 COMPUTER WINS!")

    else:
        print("🤝 DRAW!")

# TARGET NUMBER
def target_number():

    print("\n🎯 TARGET NUMBER")
    print("-" * 30)

    number_of_dice = get_number_of_dice()

    maximum_target = number_of_dice * 6

    target = random.randint(number_of_dice, maximum_target)

    print(f"\n🎯 Your target is: {target}")

    input("\nPress ENTER to roll the dice...")

    rolls = []

    for _ in range(number_of_dice):
        roll = random.randint(1, 6)
        rolls.append(roll)

    print("\n🎲 Your dice:\n")

    display_dice(rolls)

    total = sum(rolls)

    difference = abs(target - total)

    print(f"\nYour total: {total}")
    print(f"Target: {target}")
    print(f"Difference: {difference}")

    if total == target:
        print("\n🎉 PERFECT! You hit the target!")
    elif difference <= 2:
        print("\n🔥 Very close!")
    else:
        print("\n❌ You missed the target.")

# MAIN MENU
def main():
    while True:

        print("\n")
        print("╔══════════════════════════════╗")
        print("║         🎲 DICE GAME         ║")
        print("╠══════════════════════════════╣")
        print("║                              ║")
        print("║  1. 🎲 Simple Dice Roller    ║")
        print("║  2. ⚔️ Dice Battle            ║")
        print("║  3. 🎯 Target Number         ║")
        print("║  4. 🚪 Exit                  ║")
        print("║                              ║")
        print("╚══════════════════════════════╝")

        choice = input("\nChoose an option: ")

        if choice == "1":
            simple_dice_roller()

        elif choice == "2":
            dice_battle()

        elif choice == "3":
            target_number()

        elif choice == "4":
            print("\n👋🏻 Thanks for playing!")
            break

        else:
            print("\n❌ Invalid choice. Please choose 1-4.")

# START PROGRAM
main()