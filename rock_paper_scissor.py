import random

print("\n\n\t\t\U0001F389 WELCOME TO \"ROCK PAPER SCISSOR\" GAME \U0001F389\n")
target = random.randint(50,100)

print("\nQUICKOR:\n\n\tType \"1\" if \"ROCK\"\n\tType \"2\" if \"PAPER\"\n\tType \"3\" if \"SCISSOR\"\n")
system_states = ['rock','paper','scissor']

player_score = 0
system_score = 0

print("\nTARGET : ",target)
print("\n\t\t\t\U0001F389 GAME STARTS \U0001F389\n")
while True:
    player = input("\nENTER CHOICE: ")
    system = random.choice(system_states)

    if not player.isnumeric():
        player = "5"

        
    if player in ["1","2","3"]:
        print("\nPlayer's Choice : ",system_states[int(player)-1].upper())
        print("System's Choice : ",system.upper())
    elif player == "-1":
        print("\nPlayer's Choice : EXIT")
    
    if player == "1":
        if system == 'paper':
            system_score += 5
        elif system == 'scissor':
            player_score += 5
    elif player == "2":
        if system == 'rock':
            player_score += 5
        elif system == 'scissor':
            system_score += 5
    elif player == "3":
        if system == 'rock':
            system_score += 5
        elif system == 'paper':
            player_score += 5
    elif player == "-1":
        print("\n\nYou Exited The Game.\n\nThank You For Playing.")
        break
    else:
        print("\nPlease Give Valid Choice.".upper())
    
    print("\nPlayer's Score : ",player_score)
    print("System's Score : ",system_score)
    
    if player_score >= target:
        print("\n\n\t\U0001F389 Congratulations.You Won The Game. \U0001F389\n\n")
        break
    elif system_score >= target:
        print("\n\n\t\U0001F389 Best Try.System Won The Game.\U0001F389\n\n")
        break
        
            
