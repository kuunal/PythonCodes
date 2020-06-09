
import random
import re

# initialize list of "-" indicating empty position
def reset():
    for dummy_positions in range(0,9):
        board.append("-")


# prints list in board format
def print_board():
    for position, value in enumerate(board):
        print(value ,end=' ') if position not in (2,5) else print(value)
    print()
    print()

# checks for toss winner using random
def check_toss():
    try:
        input_choice = int(input("Enter toss(0,1): "))
        if input_choice not in (0,1):
            raise Exception("Please enter valid choice between 1 and 0!")
    except Exception:
            check_toss()
    else:    
        random_number = round(random.random())
        compute_turn(random_number,input_choice)        

# computes who will play first and sets turn to that player
def compute_turn(random_number, input_choice):
    global player,computer,turn_flag,number_of_moves
    if random_number == input_choice:
        try:
            user_choice=input("Please enter X or O!").upper()
            if user_choice != "X" and user_choice != "O" :
                raise Exception("Please enter valid choice!")
        except Exception:
            compute_turn(random_number,input_choice)
        else:
            player = user_choice
            if player == "X":
                computer = "O"
                turn_flag = "player"
            else:
                computer = "X"
    else:
        print("You lost the Toss!")
        computer = random.choice(["X","O"])
        if computer == "X":
            turn_flag = "computer"
            player = "O"
        else:
            player = "X"


# puts X or O for player at given place and computer at random place which is not occupied 
def play():
    global player, computer, turn_flag, number_of_moves
    winner = check_win()
    if winner != "" :
        print(winner+ "won!" )
        return 
    if number_of_moves == 0 :
        print("Tie")
        return
    if turn_flag == "player":
        try:
            location = int(input("Enter position"))
            if location > 9 or location == 0:
                raise Exception("Invalid location!")
        except Exception:
            play()
        else:
            if board[location-1] == "-":
                board[location-1] = player
                turn_flag = "computer"
                number_of_moves-=1
            else:
                print("Please choose another location!") 
        print_board()
        play()
        
    else:
        location = random.randint(0,8)
        if board[location] == "-":
            board[location] = computer
            turn_flag = "player"
            print_board()
            number_of_moves-=1
        play()

#  returns winner or null indicating no winner yet
def check_win():
    if check_row()!="": 
        return check_row() 
    if check_column()!="":
        return check_column() 
    if check_diagnol()!="":
        return check_diagnol() 
    if check_alternate_diagnol() != "":
        return check_alternate_diagnol() 
    return ""

# checks every row and returns winner or null.
def check_row():
    matched_row = ""
    for rows in range(0,8,3):        
        matched_row =  check_pair_of_three(rows,rows+1,rows+2)
        if matched_row != "":
            return matched_row
    return matched_row

# checks every column and returns winner or null.
def check_column():
    matched_column = ""
    for columns in range(0,2):
        return check_pair_of_three(columns,columns+3,columns+6)
        if matched_column != "":
            return matched_column
    return matched_column

# checks diagonal and returns winner or null.
def check_diagnol():
    diagnols=0
    return check_pair_of_three(diagnols,diagnols+4,diagnols+8) 
    
# checks alternate diagonal and returns winner or null.
def check_alternate_diagnol():
    diagnols=2
    return check_pair_of_three(diagnols,diagnols+2,diagnols+4)

# returns winner or null based on positions matched or not.
def check_pair_of_three(position_one, position_two, position_three):
    if board[position_one] == board[position_two] == board[position_three] and board[position_one] != "-":
            return board[position_one]
    return ""

board = []
turn_flag=""
player=""
computer=""
winner=""
number_of_moves=9
reset()
print_board()
check_toss()
play()
