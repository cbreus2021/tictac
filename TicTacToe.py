import random

class tic_tac_toe:

  def __init__(self):
    self.game_is_playing = False
    self.board = [' '] * 9 

  def play(self):

    print("Welcome to Tic-Tac-Toe! Choose a player to be Player 1 and Player 2. Player 1 wil be x's, and player 2 will be o's.")
    print("Player 1 will go first.")
   
    self.game_is_playing = True
    player = 1
    while self.game_is_playing == True:
      self.print_board()
      print("It is player " + str(player) + "'s turn.")
      a = self.get_player_move()
      self.move(player, a-1)
      if self.is_winner(player) == True:
        self.print_board()
        print("Congrats player " + str(player) + "! You won!")
        self.game_is_playing = False
      elif self.board_is_full() == True:
        self.print_board()
        print("It's a tie.")
        self.game_is_playing = False
      player = self.switch_player(player)
  
  def print_board(self):
    print('   |   |')
    print(' ' + self.board[0] + ' | ' + self.board[1] + ' | ' +  self.board[2])

    print('-----------')
    print(' ' + self.board[3] + ' | ' + self.board[4] + ' | ' +  self.board[5])

    print('   |   |')
    print('-----------')

    print(' ' + self.board[6] + ' | ' + self.board[7] + ' | ' +  self.board[8])
    print('   |   |')

  def get_player_move(self):
    guess = int(input("Guess a number 1-9."))
    while type(guess) != int:
      guess = int(input("Please pick a different number 1-9."))
      print("not an int")
    while guess not in {1, 2, 3, 4, 5, 6, 7, 8, 9} or not self.space_is_free(guess):
      guess = int(input("Please pick a different number 1-9."))
      print("second while")
    return guess
  
  def move(self, player, move): 
    piece = ""
    if player == 1:
      piece = "x"
    if player == 2:
      piece = "o"
    self.board[move] = piece 
  
  def space_is_free(self, move): 
    if self.board[move-1] == ' ':
      return True
    else:
      return False
    
  def board_is_full(self): 
    for i in self.board:
      if i == ' ':
        return False   
    return True

  def is_winner(self, player):
    piece = ""
    if player == 1:
      piece = "x"
    if player == 2:
      piece = "o"
    return ((self.board[6] == piece and self.board[7] == piece and self.board[8] == piece) or 
            (self.board[0] == piece and self.board[1] == piece and self.board[2] == piece) or
            (self.board[3] == piece and self.board[4] == piece and self.board[5] == piece) or
            (self.board[0] == piece and self.board[3] == piece and self.board[6] == piece) or
            (self.board[1] == piece and self.board[4] == piece and self.board[7] == piece) or 
            (self.board[2] == piece and self.board[5] == piece and self.board[8] == piece) or
            (self.board[0] == piece and self.board[4] == piece and self.board[8] == piece) or
            (self.board[2] == piece and self.board[4] == piece and self.board[6] == piece))
    
  def switch_player(self, player):
    if player == 1:
      return 2
    else: 
      return 1

t = tic_tac_toe()
t.play() 


