import turtle
import time
import random

the_board = [ "_", "_", "_",
              "_", "_", "_",
              "_", "_", "_"]

def draw_board(board):
    """
    signature: list(str) -> NoneType
    Given the current state of the game, draws
    the board on the screen, including the
    lines and the X and O pieces at the position
    indicated by the parameter.
    """
    turtle.clear()
    draw_lines()
    pos_lst = [(-turtle.window_width()//3,turtle.window_height()//3),(0,turtle.window_height()//3),\
               (turtle.window_width()//3,turtle.window_height()//3),(-turtle.window_width()//3,0),\
               (0,0),(turtle.window_width()//3,0),(-turtle.window_width()//3,-turtle.window_height()//3),\
               (0,-turtle.window_height()//3),(turtle.window_width()//3,-turtle.window_height()//3)]#list of cordinates of all positions.
    
    for i in range(len(board)): #goes through the positions on the board, drawing Xs and Os where required.
        if board[i] == "X":
            draw_cross(pos_lst[i][0], pos_lst[i][1])
        elif board[i] == "O":
            draw_circle(pos_lst[i][0], pos_lst[i][1])
            
    turtle.setposition(0,0)
    turtle.update()

def draw_lines():
    #sig: None -> NoneType
    '''
    Draws the lines according to the size of the window.
    '''
    turtle.up()
    turtle.setposition(turtle.window_width()/6,turtle.window_height()/2)
    turtle.right(90)
    turtle.down()
    turtle.forward(turtle.window_height())
    turtle.up()
    turtle.setposition(turtle.window_width()/(-6),turtle.window_height()/2)
    turtle.down()
    turtle.forward(turtle.window_height())
    turtle.up()
    turtle.left(90)
    turtle.setposition(turtle.window_width()/-2, turtle.window_height()/6)
    turtle.down()
    turtle.forward(turtle.window_width())
    turtle.up()
    turtle.setposition(turtle.window_width()/-2, turtle.window_height()/(-6))
    turtle.down()
    turtle.forward(turtle.window_width())
    turtle.up()
    

def draw_circle(xcor, ycor):
    #sig: int,int -> NoneType
    '''
    Draws a circle centered at the input x and y cordinates. The radius is according to the size of the position on the board.
    '''
    turtle.setheading(0)
    turtle.up()
    turtle.color("green")
    turtle.setposition(xcor, (ycor - turtle.window_height()/6))#moves the turtle to the point where we need the lowest point of the circle.
    turtle.down()
    turtle.circle(turtle.window_height()/6)
    turtle.up()
    turtle.color("black")
    
    
def draw_cross(xcor, ycor):
    #sig: int,int -> NoneType
    '''
    Draws a cross centered at the input x and y cordinates. The size is according to the size of the position on the board.
    ''' 
    turtle.up()
    turtle.color("red")
    turtle.setposition((xcor-(turtle.window_width()/6)), (ycor+(turtle.window_height()/6)))
    turtle.down()
    turtle.setposition((xcor+(turtle.window_width()/6)), (ycor-(turtle.window_height()/6)))
    turtle.up()
    turtle.setposition((xcor+(turtle.window_width()/6)),(ycor+(turtle.window_height()/6)))
    turtle.down()
    turtle.setposition((xcor-(turtle.window_width()/6)),(ycor-(turtle.window_height()/6)))
    turtle.up()
    turtle.color("black")
    turtle.setheading(0)


def do_user_move(board, x, y):
    """
    signature: list(str), int, int -> bool
    Given a list representing the state of the board
    and an x,y screen coordinate pair indicating where
    the user clicked, updates the board
    with an O in the corresponding position. Your
    code will need to translate the screen coordinate
    (a pixel position where the user clicked) into the
    corresponding board position (a value between 0 and
    8 inclusive, identifying one of the 9 board positions).
    The function returns a bool indicated if
    the operation was successful: if the user
    clicks on a position that is already occupied
    or outside of the board area, the move is
    invalid, and the function should return False,
    otherise True.
    """
    print("user clicked at "+str(x)+","+str(y))
    pos = cor_to_pos(x,y)#converts input cordinates to a position
    if pos == -1 or board[pos] != "_":
        return False #when the cordinates are on the lines, or when the position is not empty
    else:
        board[pos] = "O"
        return True
        
        
def cor_to_pos(x,y):
    #sig: float, float -> int
    '''
    Takes cordinates and gives the corresponding position on the board. If cordinates are on the lines, returns -1.
    '''
    pos = -1
    
    if (-turtle.window_width()//2 < x < -turtle.window_width()//6):
        if (turtle.window_height()/6 < y < turtle.window_height()/2):
            pos = 0
        elif (-turtle.window_height()/6 < y < turtle.window_height()/6):
            pos = 3
        elif (-turtle.window_height()/2 < y < -turtle.window_height()/6):
            pos = 6
            
    elif (-turtle.window_width()//6 < x < turtle.window_width()//6):
        if (turtle.window_height()/6 < y < turtle.window_height()/2):
            pos = 1
        elif (-turtle.window_height()/6 < y < turtle.window_height()/6):
            pos = 4
        elif (-turtle.window_height()/2 < y < -turtle.window_height()/6):
            pos = 7
            
    elif (turtle.window_width()//6 < x < turtle.window_width()//2):
        if (turtle.window_height()/6 < y < turtle.window_height()/2):
            pos = 2
        elif (-turtle.window_height()/6 < y < turtle.window_height()/6):
            pos = 5
        elif (-turtle.window_height()/2 < y < -turtle.window_height()/6):
            pos = 8

    return pos


def check_game_over(board):
    """
    signature: list(str) -> bool
    Given the current state of the board, determine
    if the game is over, by checking for
    a three-in-a-row pattern in horizontal,
    vertical, or diagonal lines; and also if the
    game has reached a stalemate, achieved when
    the board is full and no further move is possible.
    If there is a winner or if there is a stalemate, display
    an appropriate message to the user and clear the board
    in preparation for the next round. If the game is over,
    return True, otherwise False.
    """

    condition_lst = [board[:3], board[3:6], board[6:],board[0:7:3], \
                     board[1:8:3], board[2:9:3], board[0:9:4], board[2:7:2]] #list of lines on the board

    for line in condition_lst:
        if line == ["X","X","X"]:
            end_game("You Lose !", board)
            return True
        
        elif line == ["O", "O", "O"]:
            end_game("You Win !", board)
            return True

    if not("_" in board):
        end_game("Draw !", board)
        return True
    
    else:
        return False

def end_game(message, board):
    #sig: str -> NoneType
    '''
    Writes on the turtle screen.
    '''
    turtle.write(message, False, align="center", font=("Times New Roman", 80, "normal"))
    time.sleep(3)
    clear_board(board)
    draw_board(the_board)

def clear_board(board):
    #sig: list -> NoneType
    '''
    Removes all crosses and circles from the board.
    '''
    for i in range(9):
        board[i] = "_"

def do_computer_move(board):
    """
    signature: list(str) -> NoneType
    Given a list representing the state of the board,
    select a position for the computer's move and
    update the board with an X in an appropriate
    position. The algorithm for selecting the
    computer's move shall be as follows: if it is
    possible for the computer to win in one move,
    it must do so. If the human player is able 
    to win in the next move, the computer must
    try to block it. Otherwise, the computer's
    next move may be any random, valid position
    (selected with the random.randint function).
    """
    position = -1 #position is undecided.
    
    lst_open_pos = [] #list of open positions is made.
    for j in range(len(board)):
        if board[j] == "_":
            lst_open_pos.append(j)
          
    test_board = board[:]#a copy of the original board is made where the computer can test placing its moves.
    
    for pos in lst_open_pos: #goes through each of the open positions, putting a hashtag and then testing the outcomes.
        test_board[pos] = "#" 
        
        res = test(test_board)
        
        if res == "win": #if the position is a winning position, it is chosen and no further positions are tested.
            position = pos
            break
        if res == "save": #if the position is a saving position, it is chosen but testing goes on, incase there is a winning position.
            position = pos
            
        test_board[pos] = "_" #test board is reset after the test for the position is complete.

    if position == -1: #if the computer is still undecided (i.e. no winning or saving positions have been found), it chooses randomly.
        position = lst_open_pos[random.randint(0, (len(lst_open_pos)-1))]

    board[position] = "X" #places its move at the chosen position.

def test(board):
    #sig: lst -> str
    '''
    Takes a test case of the board with a "#" at the position where the computer is thinking about placing its move.
    Returns the outcome of placing the move there. It can be a win, save, or neither.
    '''
    condition_lst = [board[:3], board[3:6], board[6:],board[0:7:3], \
                     board[1:8:3], board[2:9:3], board[0:9:4], board[2:7:2]] #list of lines
    res = ''
    
    for item in condition_lst:
        if "#" in item:
            if item.count("X") == 2:
                res = "win"
                break
            
            if  item.count("O") == 2:
                res = "save"

    return res


def clickhandler(x, y):
    """
    signature: int, int -> NoneType
    This function is called by turtle in response
    to a user click. The parameters are the screen
    coordinates indicating where the click happened.
    The function will call other functions. You do not
    need to modify this function, but you do need
    to understand it.
    """
    if do_user_move(the_board,x,y):
        draw_board(the_board)
        if not check_game_over(the_board):
            do_computer_move(the_board)
            draw_board(the_board)
            check_game_over(the_board)

def main():
    """
    signature: () -> NoneType
    Runs the tic-tac-toe game. You shouldn't
    need to modify this function.
    """
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.onscreenclick(clickhandler)
    draw_board(the_board)
    turtle.mainloop()


main()
    
        
        
    






