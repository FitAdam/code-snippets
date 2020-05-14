while True:
    ask_user = str(input("Hello do you want to play a game? yes or no "))
    if ask_user == "yes":
        usr_input = str(input("Please type rock, scissors or paper: "))
        usr_input2 = str(input("Please type rock, scissors or paper: "))

        if usr_input == "scissors" and usr_input2 == "scissors":
            print("it's a draw!")
        if usr_input == "scissors" and usr_input2 == "rock":
            print("user2 has won")
        if usr_input == "scissors" and usr_input2 == "paper":
            print("user1 has won")
        if usr_input == "rock" and usr_input2 == "rock":
            print("it's a draw!")
        if usr_input == "rock" and usr_input2 == "paper":
            print("user2 has won!")
        if usr_input == "rock" and usr_input2 == "scissors":
            print("user1 has won")
        if usr_input == "paper" and usr_input2 == "paper":
            print("it's a draw!")
        if usr_input == "paper" and usr_input2 == "scissors":
            print("user2 has won")
        if usr_input == "paper" and usr_input2 == "rock":
            print("user1 has won")
    else:
        ask_user2 = str(input("Are you sure? "))
        if ask_user2 == "yes":
            break





