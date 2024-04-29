from random import choice
from os import system
print("ROCK - PAPER - SCISSORS")

#         Pedra Papel Tesoura
choices = ("R", "P", "S")
game = 1
scorePlayer = 0
scoreBot = 0
rules = {
    "WinB" : "RS",
    "WinB" : "PR",
    "WinB" : "SP",
    "WinP" : "RP",
    "WinP" : "PS",
    "WinP" : "SR"
}


#Se ambas as mãos forem iguais: empate; Se forem diferentes, por regras conhecidas, é decidido o vencedor. RS = Pedra-Papel, SR = Tesoura-Pedra... 
def getResult(choice1, choice2):
    comb = botChoice + playerChoice
    if choice1 == choice2:
        return "Draw"
    elif comb == "RS" or comb == "PR" or comb == "SP":
        return "You lost!"
    elif comb == "RP" or comb == "PS" or comb == "SR":
        return "You won!"
        

#Mostra em que jogo está, como está a pontuação, é escolhido a escolha do bot, então você escolhe. É mostrado as escolhas, então é calculado a pontuação, então se avança no jogo.
while True:
    print(f"\nGAME: {game}")
    print(f"SCORE: BOT-{scoreBot} X YOU-{scorePlayer}")
    botChoice = choice(choices)
    playerChoice = ""

    while playerChoice not in choices:
        playerChoice = str(input(f"\nInsert your choice [R, P, S]: ")).upper()

    print(f"Player: {playerChoice}\nBot: {botChoice}")
    print(getResult(botChoice, playerChoice))

    if getResult(botChoice, playerChoice) == "You won!":
        scorePlayer+=1
    elif getResult(botChoice, playerChoice) == "You lost!":
        scoreBot+=1
    
    game+=1
    ans = str(input("Continue? [Y/N]: ")).upper()[0]
    if ans == "N":
        exit()
    system("cls")
    