from random import choice

def player_win(player_sign, bot_sign):
    if player_sign == "r" and bot_sign == "s":
        return True
    elif player_sign == "p" and bot_sign == "r":
        return True
    elif player_sign == "s" and bot_sign == "p":
        return True
    return False

def bot_win(player_sign, bot_sign):
    if bot_sign == "r" and player_sign == "s":
        return True
    elif bot_sign == "p" and player_sign == "r":
        return True
    elif bot_sign == "s" and player_sign == "p":
        return True
    return False

def draw(player_sign, bot_sign):
    if player_sign == "r" and bot_sign == "r":
        return True
    elif player_sign == "p" and bot_sign == "p":
        return True
    elif player_sign == "s" and bot_sign == "s":
        return True
    return False

kill_game, end_game = False, False
player_score, bot_score, game_round = 0, 0, 1
signs = ["r", "p", "s"]
sign = {"r" : "Rock", "p" : "Paper", "s" : "Scissors"}

print("\tWelcome to Rock-Paper-Scissors!")

while not kill_game:
    player_sign = input("\nEnter rock/paper/scissors(r/p/s): ").lower()
    
    if player_sign != "p" and player_sign != "r" and player_sign != "s":
        print("Invalid input! Enter 'r' or 'p' or 's': ")
        continue
    
    bot_sign = choice(signs)
    print(f"\n\tRound {game_round}\n")
    print(f"Your Move: {sign[player_sign]}\nVS\ncomputer Move: {sign[bot_sign]}\n")
    
    if player_win(player_sign, bot_sign):
        player_score += 1
        print("You won this round!")
    elif bot_win(player_sign, bot_sign):
        bot_score += 1
        print("You lose this round!")
    elif draw(player_sign, bot_sign):
        player_score += 1
        bot_score += 1
        print("This round is draw!")

    
    print(f"\nYour Score: {player_score}\nVS\ncomputer Score: {bot_score}")

    game_round += 1

    if player_score == 3 and bot_score == 3:
        print("It's Draw!")
        end_game = True
    elif player_score == 3 and bot_score != 3: 
        print("You Win!")
        end_game = True
    elif bot_score == 3 and player_score != 3:
        print("You Lose!")
        end_game = True
    
    if end_game:
        while True:
            play_again_char = input("Do you want to play again?[Y/N]: ").upper()
            if play_again_char == "Y":
                player_score, bot_score,game_round = 0, 0, 0
                print("Game Restarted")
                break
            elif play_again_char == "N":
                print("Game Finished !")
                kill_game = True
                break
            else:
                print("Invalid Character! please Enter Y or N: ")
