"""
Exercise 26 (and Solution)
This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 3, and Part 4.

As you may have guessed, we are trying to build up to a full tic-tac-toe board. However, this is significantly more than half an hour of coding, so we’re doing it in pieces.

Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the moves were made.
"""
game = [[2, 2, 1], 
        [0, 2, 2],
        [1, 1, 2],]


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        print("   a  b  c")
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except IndexError as e:
        print("Error: make sure you input row/column as 0 1 or 2?")
    
    except Exception as e:
        print("Something went very wrong!", e)

# count() is an inbuilt function in Python that returns count of how many times a given object occurs in list.
def win_horizontally(current_game):
    for row in current_game:
        if row.count(1) == 3:
            print("-----------------------")
            print("Winner player number 1!")
            print("-----------------------")
            
        elif row.count(2) == 3:
            print("-----------------------")
            print("Winner player number 2!")
            print("-----------------------")
            
    
    return game_board(game)

def win_vertiacally(current_game):
    if current_game[0][0] == 1 and current_game[1][0] == 1 and current_game[2][0] == 1:
        print("-----------------------")
        print("Winner player number 1!")
        print("-----------------------")
    elif current_game[0][1] == 1 and current_game[1][1] == 1 and current_game[2][1] == 1:
        print("-----------------------")
        print("Winner player number 1!")
        print("-----------------------")
    elif current_game[0][2] == 1 and current_game[1][2] == 1 and current_game[2][2] == 1:
        print("-----------------------")
        print("Winner player number 1!")
        print("-----------------------")
    else:
        if current_game[0][0] == 2 and current_game[1][0] == 2 and current_game[2][0] == 2:
            print("-----------------------")
            print("Winner player number 2!")
            print("-----------------------")
        elif current_game[0][1] == 2 and current_game[1][1] == 2 and current_game[2][1] == 2:
            print("-----------------------")
            print("Winner player number 2!")
            print("-----------------------")
        elif current_game[0][2] == 2 and current_game[1][2] == 2 and current_game[2][2] == 2:
            print("-----------------------")
            print("Winner player number 2!")
            print("-----------------------")

def win_diagonally(current_game):
    if current_game[0][0] == 1 and current_game[1][1] == 1 and current_game[2][2] == 1:
        print("-----------------------")
        print("Winner player number 1!")
        print("-----------------------")
    elif current_game[2][0] == 1 and current_game[1][1] == 1 and current_game[0][2] == 1:
        print("-----------------------")
        print("Winner player number 1!")
        print("-----------------------")
    else:
        if current_game[0][0] == 2 and current_game[1][1] == 2 and current_game[2][2] == 2:
            print("-----------------------")
            print("Winner player number 2!")
            print("-----------------------")
        elif current_game[2][0] == 2 and current_game[1][1] == 2 and current_game[0][2] == 2:
            print("-----------------------")
            print("Winner player number 2!")
            print("-----------------------")

def get_user_input(current_game):
    #column = input("Please choose the collumn A B C and type 1 or 2")
    #row = input("Please choose the collumn row and type 1 or 2")
    #if column == 
while True:
    print("-----------------------")
    print("Hello two the new game!")
    print("-----------------------")
    
