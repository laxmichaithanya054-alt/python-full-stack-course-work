import random

def dice():
    return random.randint(1, 6)

player1 = input("Enter Player 1 name: ")
player2 = input("Enter Player 2 name: ")

player1_score = 0
player2_score = 0

winning_point = 100
ladders = {6:25, 12:31, 25:90, 46:60, 51:74, 78:99, 82:96}
snakes = {24:5, 45:18, 66:33, 74:37, 88:77, 93:57, 98:21}

while True:

    # ---------- PLAYER 1 ----------
    status1 = input(f"{player1}: [P]lay or [Q]uit: ").lower()
    if status1 == "q":
        print(f"{player2} wins!")
        break

    dice_1 = dice()
    print(f"{player1} rolled: {dice_1}")

    if player1_score + dice_1 <= winning_point:
        player1_score += dice_1

    # Ladder
    if player1_score in ladders:
        print("🎉 Ladder!")
        player1_score = ladders[player1_score]

    # Snake
    elif player1_score in snakes:
        print("🐍 Snake!")
        player1_score = snakes[player1_score]

    print(f"{player1} position: {player1_score}")

    if player1_score == winning_point:
        print(f"🏆 {player1} wins!")
        break


    # ---------- PLAYER 2 ----------
    status2 = input(f"{player2}: [P]lay or [Q]uit: ").lower()
    if status2 == "q":
        print(f"{player1} wins!")
        break

    dice_2 = dice()
    print(f"{player2} rolled: {dice_2}") 

    if player2_score + dice_2 <= winning_point:
        player2_score += dice_2

    # Ladder
    if player2_score in ladders:
        print("🎉 Ladder!")
        player2_score = ladders[player2_score]

    # Snake
    elif player2_score in snakes:
        print("🐍 Snake!")
        player2_score = snakes[player2_score]

    print(f"{player2} position: {player2_score}")

    if player2_score == winning_point:
        print(f"🏆 {player2} wins!")
        break