# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 11:02:03 2021

@author: msi
"""
import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")

ranks = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
          "Eight", "Nine", "Ten", "Jack", "Queen", "King")

values = {"Ace" : 11, "Two" : 2, "Three" : 3,
          "Four" : 4, "Five" : 5,"Six" : 6, "Seven": 7,
          "Eight" : 8, "Nine" : 9, "Ten" : 10, "Jack" : 10,
          "Queen" : 10, "King" : 10}


class Card():
    

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck():
    

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    

    def __len__(self):
        return len(self.deck)
    

    def shuffle(self):
        random.shuffle(self.deck)
    

    def deal_one(self):
        return self.deck.pop(0)


class Hand():
    

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    

    def add_cards(self,new_card):
        self.cards.append(new_card)
        self.value += new_card.value
        if new_card.rank == "Ace":
            self.aces += 1
    

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chip():
    

    def __init__(self, chips = 0):
        self.chips = chips
    

    def __str__(self):
        return f"Player has {self.chips} $ \n"
    

    def deposit(self, money):
        self.chips += money
    

    def bet(self):
        while True:
            try:
                print(player_balance)
                money = int(input("Place your bet : Min Bet is 1 $ \n"))
                if self.chips > money and money != 0:
                    print("\n"*100)
                    print(f"Player bet is {money} $ \n")
                    self.chips -= money
                    return money
                elif self.chips == money and money != 0:
                    print("\n"*100)
                    print(f"Player goes All-In! {money} $ \n")
                    self.chips -= money
                    return money
                else:
                    if money == 0:
                        print("\n"*100)
                        print("You can't bet 0 $ \n")
                    else:
                        print("\n"*100)
                        print("Not enough money to bet! \n")
            except:
                print("Please enter an Integer! \n")


def player_win():
    player.cards.clear()
    dealer.cards.clear()
    player_balance.deposit(new_bet * 2)
    player.value = 0
    dealer.value = 0
    dealer.aces = 0
    player.aces = 0
    print(f"Player has won {new_bet * 2} $ \n")


def dealer_win():
    player.cards.clear()
    dealer.cards.clear()
    player.value = 0
    dealer.value = 0
    dealer.aces = 0
    player.aces = 0
    print("Dealer has won! \n")


def player_bust():
    player.cards.clear()
    dealer.cards.clear()
    player.value = 0
    dealer.value = 0
    dealer.aces = 0
    player.aces = 0
    print("Player Bust!! Dealer has won! \n")


def dealer_bust():
    player.cards.clear()
    dealer.cards.clear()
    player_balance.deposit(new_bet * 2)
    player.value = 0
    dealer.value = 0
    dealer.aces = 0
    player.aces = 0
    print(f"Dealer Bust!! Player has won {new_bet * 2} $ \n")


def push():
    player.cards.clear()
    dealer.cards.clear()
    player.value = 0
    dealer.value = 0
    dealer.aces = 0
    player.aces = 0
    player_balance.deposit(new_bet / 2)
    print("It is a Push! Nobody has won! \n")


def hit_or_stand():
    global playing
    choice = []
    while choice not in ("HIT", "STAND"):
        choice = input("Stand or Hit ? : \n").upper()
        print("\n"*100)
        if choice == "HIT":
            hit(new_deck, player)
            playing = True
        else:
            player.aces = 0
            playing = False


def display(player, dealer):
    print("Player hand : ",*player.cards,sep = "\n")
    print(f"Player SUM : {player.value}")
    print("\n")
    if len(dealer.cards) == 2 and player.value < 21 and dealer.value < 21:
        print("Dealer hand : ")
        print("|[CLOSED CARD]|")
        for card in range(1, len(dealer.cards)):
            print(dealer.cards[card])
        print("\n")
    elif (player.value == 22 or dealer.value == 22) and len(player.cards) == 21:
        print("Dealer hand : ")
        print("|[CLOSED CARD]|")
        for card in range(1, len(dealer.cards)):
            print(dealer.cards[card])
        print("\n")

    else:
        print("Dealer hand : ",*dealer.cards,sep = "\n")
        print(f"Dealer SUM : {dealer.value}")
        print("\n")


def replay():
    global game_on
    choice = []
    if player_balance.chips == 0:
        print("Player out of credits. Please deposit!")
        game_on = False
    else:
        while choice not in ("Y", "N"):
            choice = input("Do you want to play again? Y/N : \n").capitalize()
            if choice == "Y":
                print("\n"*100)
                game_on = True
            else:
                game_on = False


def hit(new_deck, player):
    player.add_cards(new_deck.deal_one())
    player.adjust_for_ace()


new_deck = Deck()
new_deck.shuffle()
player = Hand()
dealer = Hand()
player_balance = Chip(100)
game_on = True

print("\n"*100)
print("Welcome to Blackjack")

while game_on:
    print(f"There are {len(new_deck)} Cards in the deck!")
    if len(new_deck) < 10:
        print("Changing the Deck!")
        new_deck = Deck()
        new_deck.shuffle()
    new_bet = player_balance.bet()
    for deal in range(2):
        player.add_cards(new_deck.deal_one())
        dealer.add_cards(new_deck.deal_one())
    display(player, dealer)
    if player.value == 21 and dealer.value != 21:
        player_win()
        player.aces = 0
    elif dealer.value == 21 and player.value != 21:
        dealer_win()
        player.aces = 0
    elif dealer.value == 21 and player.value == 21:
        push()
        player.aces = 0
    else:
        playing = True
        while playing:
            hit_or_stand()
            display(player, dealer)
            if player.value == 21:
                player_win()
                player.aces = 0
                playing = False
            elif player.value > 21:
                player_bust()
                playing = False
        if player.value != 0:
            while dealer.value < 17:
                dealer.add_cards(new_deck.deal_one())
                dealer.adjust_for_ace()
                print("\n"*100)
                display(player, dealer)
            if dealer.value == 21:
                dealer_win()
            elif dealer.value > 21:
                dealer_bust()
            elif dealer.value < player.value:
                print("\n"*100)
                print("Player hand : ",*player.cards,sep = "\n")
                print(f"Player SUM : {player.value}")
                print("\n")
                print("Dealer hand : ",*dealer.cards,sep = "\n")
                print(f"Dealer SUM : {dealer.value}")
                print("\n")
                player_win()
            elif dealer.value > player.value:
                print("\n"*100)
                print("Player hand : ",*player.cards,sep = "\n")
                print(f"Player SUM : {player.value}")
                print("\n")
                print("Dealer hand : ",*dealer.cards,sep = "\n")
                print(f"Dealer SUM : {dealer.value}")
                print("\n")
                dealer_win()
            else:
                print("\n"*100)
                print("Player hand : ",*player.cards,sep = "\n")
                print(f"Player SUM : {player.value}")
                print("\n")
                print("Dealer hand : ",*dealer.cards,sep = "\n")
                print(f"Dealer SUM : {dealer.value}")
                print("\n")
                push()
    print(player_balance)
    replay()
