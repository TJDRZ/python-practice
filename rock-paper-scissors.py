from random import randint

options = ["rock", "paper", "scissors"]

computerSelection = options[randint(0,2)]
userSelection = ""

while userSelection not in options:
    userSelection = input("Make your selection (Rock, Paper, Scissors): ").lower()

print(f"Computer chose {computerSelection} and you chose {userSelection}")

results = ""
match results:
    case results if computerSelection == userSelection:
        print("Tie")
    case results if (computerSelection == "rock" and userSelection == "scissors") or (computerSelection == "paper" and userSelection == "rock") or (computerSelection == "scissors" and userSelection == "paper"):
        print("You lose")
    case results if (userSelection == "rock" and computerSelection == "scissors") or (userSelection == "paper" and computerSelection == "rock") or (userSelection == "scissors" and computerSelection == "paper"):
        print("You Win")