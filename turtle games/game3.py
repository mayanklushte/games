import random

turn = True
a = ["rock", "paper", "scissors"]

p_name = input("Enter your name: ")

for i in range(3):
    if turn==True:
        player = input("enter your choice: ")
        turn = False

    if turn==False:
        computer = random.choice(a)
        print("computers choice: ", computer)
        turn = True


def win():
    if player == "rock" and computer == "scissors":
        print(p_name, " win, Rock blunts scissors")
    elif player == "paper" and computer == "rock":
        print(p_name, " win Paper covers rock")
    elif player == "scissors" and computer == "paper":
        print(p_name, " win Scissors cut paper")
    elif computer == "rock" and player == "scissors":
        print("computer win, Rock blunts scissors")
    elif computer == "paper" and player == "rock":
        print("computer win Paper covers rock")
    elif computer == "scissors" and player == "paper":
        print("computer win Scissors cut paper")
    elif player == "rock" and computer == "rock" or\
            player == "scissors" and computer == "scissors" or\
            player == "paper" and computer == "paper":
        print("its a tie")


win()
