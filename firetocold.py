
from words import words

print(
    "Welcome to the FireToCold Game! \n"
    "Rules: \n"
    "1. 2 Player Game \n"
    "2. Change One Letter at a Time \n"
    "3. Spell the Word 'COLD' \n"
    "Type 'quit' to stop the game. \n"
)

start = "FIRE"
end = "COLD"
player = 1

print(start)

while True:

    print("Player", player)
    print("What letter do you want to change:")

    fromletter = input("From: ").strip().upper()
    if fromletter == "QUIT":
        print("Game stopped. Nobody wins.")
        break

    toletter = input("To: ").strip().upper()
    if toletter == "QUIT":
        print("Game stopped. Nobody wins.")
        break

    if len(fromletter) != 1 or len(toletter) != 1:
        print("Enter only one letter")
        continue

    if fromletter not in start:
        print("Letter does not exist")
        continue

    # Find every spot where that letter shows up in the word
    positions = [i for i in range(len(start)) if start[i] == fromletter]

    # If the letter shows up more than once, ask which one to change
    if len(positions) == 1:
        position = positions[0]
    else:
        which = input(f"There are {len(positions)} {fromletter}'s. Which one? "
                      f"(1 = first, 2 = second...): ").strip()
        if which not in [str(n) for n in range(1, len(positions) + 1)]:
            print("Invalid choice")
            continue
        position = positions[int(which) - 1]

    # Change only the letter at that spot
    new_word = start[:position] + toletter + start[position + 1:]

    if new_word == start:
        print("Choose a different letter")
        continue

    if new_word not in words:
        print("Word does not exist")
        continue

    start = new_word

    print(start)

    if start == end:
        print("Player", player, "wins!")
        break

    if player == 1:
        player = 2
    else:
        player = 1
