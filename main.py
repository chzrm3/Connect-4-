x = 10

def name_players():
    print(
        "Welcome, one and all, to the epic arena of Connect 4 - Destruction Derby!!! Our two challengers today are some of the finest in the land!")

    player_1 = input("Player 1, what is your name?")
    print("Beautiful! Player 1 will henceforth be known as the valiant {}".format(player_1))
    player_2 = input("And Player 2, what shall we call you, m'lord?")
    print(
        "Phemonenal. The phrase 'player 2' will cease to exist, and in its stead, we call you the mighty {}!!!".format(player_2))
    return player_1, player_2

def modify_x():
    global x
    x += 100
def print_board(board):
    for row in board:
        output = "|"
        for cell in row:
            output += " " + cell + " |"
        print(output)

def create_board():
    board = []
    for _ in range(6):
        row = [" "] * 7
        board.append(row)
    return board

def get_player_input(player_name):
    while True:
        player_input = input("{}, it's your turn! Enter a column number (1-7): ".format(player_name))
        if player_input.isdigit() and 1 <= int(player_input) <= 7:
            return int(player_input)
        else:
            print("Invalid input. Please enter a valid column number from 1 to 7.")

def take_turn(board, player_1, player_2, turn_counter):
    print_board(board)
    column = 6
    player_piece = " "
    if turn_counter % 2 == 0:
        player_name = player_2
        player_piece = "O"
    else:
        player_name = player_1
        player_piece = "X"

    player_turn = get_player_input(player_name)

    for row in range(5, -1, -1):
        if board[row][player_turn - 1] == " ":
            print("We're currently at row {} and column {}!".format(row, player_turn - 1))
            board[row][player_turn - 1] = player_piece
            break
        else:
            print("We're currently at row {} and column {}!".format(row, player_turn - 1))

def check_winner():
    # Check horizontally
    for row in range(6):
        for col in range(4):
            # Check if there are four consecutive matching pieces
            if (
                board[row][col] != " "
                and board[row][col] == board[row][col + 1]
                == board[row][col + 2]
                == board[row][col + 3]
            ):
                return True  # We have a winner!

    # Check vertically
    for row in range(3):
        for col in range(7):
            # Check if there are four consecutive matching pieces
            if (
                board[row][col] != " "
                and board[row][col] == board[row + 1][col]
                == board[row + 2][col]
                == board[row + 3][col]
            ):
                return True  # We have a winner!

    # Check diagonally (from top-left to bottom-right)
    for row in range(3):
        for col in range(4):
            # Check if there are four consecutive matching pieces
            if (
                board[row][col] != " "
                and board[row][col] == board[row + 1][col + 1]
                == board[row + 2][col + 2]
                == board[row + 3][col + 3]
            ):
                return True  # We have a winner!

    # Check diagonally (from bottom-left to top-right)
    for row in range(3, 6):
        for col in range(4):
            # Check if there are four consecutive matching pieces
            if (
                board[row][col] != " "
                and board[row][col] == board[row - 1][col + 1]
                == board[row - 2][col + 2]
                == board[row - 3][col + 3]
            ):
                return True  # We have a winner!

    return False  # No winner found



    #for x in range(6):
      #  if (board[int(player_turn)-1][column] == " "):
       #     board[int(player_turn)-1][column] = player_piece
     #   if board[column][x] == " ":
      #    board[column][x] = player_piece
       #   break
        #else:
         #   column -= 1
          #  if (column < 0):
           #     break



print(x)
modify_x()
print(x)

board = create_board()
print_board(board)
player_1, player_2 = name_players()
print(player_1)
print(player_2)

winner = False
winners_name = " "
turn_counter = 1
while not winner:
    take_turn(board, player_1, player_2, turn_counter)
    winner = check_winner()
    turn_counter += 1
    print("Moving on to turn {}".format(turn_counter))

print("We have a winner, ladies and gentlemen!!!! I CAN'T BELIEVE THIS!!! AHHH!!!!")

if (turn_counter % 2 == 0):
    print("{} is the winner! His family will eat well tonight, while {}'s starves in the street! HAHAHHAHA (no I'm just kidding, it's just a game "
          "of connect 4, let's take it easy here fellas)".format(player_1, player_2))
else:
    print(
        "{} is the winner! The streets will run red with the blood of {}!!!!! (no no guys it's just a joke, this was a friendly and lighthearted game!"
        "Nobody has anything to worry about...right {}!!?!?!?".format(player_2, player_1, player_2))
print_board(board)


# statement = input("Say whatever you want, and I'll repeat it blindly!")
# print(statement)
# print("The user said {}. What a wild and unpredictable thing to say!".format(statement))