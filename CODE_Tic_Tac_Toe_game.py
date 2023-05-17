#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Board Representation

from IPython.display import clear_output

def display_board(board):
    clear_output()
    
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('--|---|--')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('--|---|--')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])


# In[ ]:


# Testing the Board Function

test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# In[ ]:


# Function to take the player input and assign their marker as 'X' or 'O'

def player_input():
    
    marker = ''

    while not (marker == "x" or marker == "o"):
        
        marker = input("player1: Please pick a marker 'X' or 'O' ").lower()
        
    if marker == 'x':
        return ('X','O')
    else:
        return ('O','X')


# In[ ]:


# Testing the input function

player_input()


# In[ ]:


# Function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.

def place_marker(board,marker,position):
    
    board[position] = marker


# In[ ]:


# Testing the marker function

place_marker(board= test_board, marker= '$', position= 4)
display_board(board= test_board)


# In[ ]:


# Function that takes in a board and a mark (X or O) and then checks to see if that mark has won.

def win_check(board,mark):
    return(
        (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
        (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
        (board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
        (board[1] == mark and board[4] == mark and board[7] == mark) or  # down the left
        (board[2] == mark and board[5] == mark and board[8] == mark) or  # down the middle
        (board[3] == mark and board[6] == mark and board[9] == mark) or  # down the right
        (board[1] == mark and board[5] == mark and board[9] == mark) or  # diagonal
        (board[3] == mark and board[5] == mark and board[7] == mark)     # diagonal
    )


# In[ ]:


# Testing the win function

win_check(board= test_board, mark= 'X')


# In[ ]:


# Function that uses the random module to randomly decide which player goes first.

from random import randint

def choose_first():
    first = randint(0,1)
    if first == 0:
        return ('Player 1')
    else:
        return ('Player 2')


# In[ ]:


# Function to check whether a board has free space available or not

def space_check(board,position):
    
    return board[position] == ' '


# In[ ]:


# Function to check if the board is full or not

def full_board_check(board):
    
    for i in range(1,10):
        
        if space_check(board,i):   # if space is available that means board is not full
            return False
        
    return True


# In[ ]:


# function that asks for a player's next position (as a number 1-9) and then uses the space_check function to check if it's a free position. If it is, then return the position for later use.

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input(f'{turn} Choose your next position: (1-9) '))
        
    return(position)


# In[ ]:


# Function that asks the player if they want to play again and returns a boolean True if they do want to play again.

def replay():
    re_play = ' '
    
    while not (re_play == 'y' or re_play == 'n'):
        re_play = input('you wanted to play again ? (Y/N)').lower()
    
    if re_play == 'y':
        return True
    else:
        False


# In[ ]:


# Function to start the game

def start_game():
    
    play_game = ' '
    while not (play_game == 'y' or play_game == 'n'):
        play_game = input('are you ready to play the game ? (Y/N)').lower()
    
    if play_game == 'y':
        return True
    else:
        False


# In[ ]:


# LET'S JOIN ALL THE FUNCTIONS TO RUN THE GAME

print('Welcome to Tic Tac Toe!')

while True:
    
    the_board = [' '] * 10
    p1_marker,p2_marker = player_input()
    turn = choose_first()
    
    game_on = start_game()
    
    while game_on:
        
        if turn == 'Player 1':
            
            display_board(board= the_board)
            position = player_choice(board= the_board)
            place_marker(board= the_board, marker= p1_marker, position=position)
            
            if win_check(board= the_board,mark= p1_marker):
                display_board(board= the_board)
                print(f'Congratulations ! {turn} you won the game !')
                game_on = False
                
            else:
                if full_board_check(board= the_board):
                    display_board(board= the_board)
                    print('The game is draw!')
                    break
                
                else:
                    turn = 'Player 2'
                    
        else:
            
            display_board(board= the_board)
            position = player_choice(board= the_board)
            place_marker(board= the_board, marker= p2_marker, position=position)
            
            if win_check(board= the_board,mark= p2_marker):
                display_board(board= the_board)
                print(f'{turn} you won the game !')
                game_on = False
                
            else:
                if full_board_check(board= the_board):
                    display_board(board= the_board)
                    print('The game is draw!')
                    break
                else:
                    turn = 'Player 1'
            
    if not replay():
        break


# In[ ]:

