# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 15:26:00 2021

@author: Ceyhun
"""

from random import choice

class Player:
    
    
    def __init__(self, marker=None):
        self.marker = marker
    
    @staticmethod
    def marker_choice():
        marker = " "
        while marker not in ["X", "O"]:
            marker = str(input("Player 1 Choose your Marker X or O : \n")).upper()
        if marker == "X":
            return ("X", "O")
        return("O", "X")
    
    @staticmethod
    def marker_setter(player1, player2):
        player1.marker, player2.marker = Player.marker_choice()
        
        
class Game:
    
    
    def __init__(self):
        self.board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    
    
    def display(self):
        print(
            f"| {self.board[7]} | {self.board[8]} | {self.board[9]} |",
            "—————————————",
            f"| {self.board[4]} | {self.board[5]} | {self.board[6]} |",
            "—————————————",        
            f"| {self.board[1]} | {self.board[2]} | {self.board[3]} |",
sep=("\n"))
        
    
    def space_checker(self, pos):
        return self.board[pos] == " "
    
    
    def tie_checker(self):
        for i in range(1, 10):
            if self.space_checker(i):
                return False
        else:
            return True

    
    def place_marker(self, player):
        position = 0
        while not self.space_checker(position) or position not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            position = int(input("Select Position : \n"))
            
        self.board[position] = player.marker
        
    
    
    def first_player(self, player1, player2):
        return choice([player1.marker, player2.marker])
    
    
    
    def win_check(self, player):
        return((self.board[1] == self.board[2] == self.board[3] == player.marker)
            or (self.board[4] == self.board[5] == self.board[6] == player.marker)
            or (self.board[7] == self.board[8] == self.board[9] == player.marker)
            or (self.board[7] == self.board[4] == self.board[1] == player.marker)
            or (self.board[8] == self.board[5] == self.board[2] == player.marker)
            or (self.board[9] == self.board[6] == self.board[3] == player.marker)
            or (self.board[1] == self.board[5] == self.board[9] == player.marker)
            or (self.board[3] == self.board[5] == self.board[7] == player.marker))
    
    
    def replay(self):
        choice = " "
        while choice not in ["Y", "N"]:
            choice = str(input("Play : Y or N: \n")).upper()
        if choice == "Y":
            return True
        return False
    
    
    def play(self, player1, player2):
        
        
        while True:
            player1 = Player()
            player2 = Player()
            Player.marker_setter(player1, player2)
            turn = self.first_player(player1, player2)
            game_on = True
            print("Welcome To Tic-Tac-Toe")
            print(f"{turn} goes First!")
            while game_on:

                if turn == player1.marker:
                    
                    self.place_marker(player1)
                    self.display()
                    
                    if self.tie_checker():
                        game_on = False
                        
                    elif self.win_check(player1):
                        game_on = False
                        
                    else:
                        turn = player2.marker
                
                if turn == player2.marker:
                    
                    self.place_marker(player2)
                    self.display()
                    
                    if self.tie_checker():
                        game_on = False
                    
                    elif self.win_check(player2):
                        game_on = False
                    
                    else:
                        turn = player1.marker
            
            if not self.replay():
                break
            
            else:
                self.board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
            
game = Game()
game.play("player1", "player2")