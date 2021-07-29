print("*" * 10, " TIC TAC TOE ", "*" * 10)

board = list(range(1,10))

# Create the board
def draw_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

# Accepts user input. Checks the correctness of the input.
# Checks if the box is not occupied already
def take_input(player_token):
   valid = False
   while not valid:
      player_answer = input("Where would you like to input " + player_token+" ?")
      try:
         player_answer = int(player_answer)
      except:
         print("Incorrect input. Try again")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token
            valid = True
         else:
            print("It is occupied already!")
      else:
        print("Incorrect input. Input the number from 1 to 9,please")

# Create a tuple with winning coordinates and loop through it in a for loop.
def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

# Main function to start the game
# Evaluates whether there is a winner or a tie
def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp, "Winner !")
              win = True
              break
        if counter == 9:
            print("Tie !")
            break
    draw_board(board)
main(board)

input("Input Enter for escape!")