import random
ranks = ["", "A", "2", "3", "4", "5", "6",
         "7", "8", "9", "10", "J", "Q", "K"]
suits = ["♥", "♣", "♠", "♦"]

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{ranks[self.rank]}{suits[self.suit]}"
    def __repr__(self):
         return f"{ranks[self.rank]}{suits[self.suit]}"

