import random

RANKS = ["Spades", "Clubs", "Hearts", "Diamonds"]
VALUES = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
          "Nine", "Ten", "Jack", "Queen", "King", "Ace"]

class Card:
    def __init__(self, rank, value):
        self.rank = rank
        self.value = value
        self.worth = self.get_worth(self.value)

    @staticmethod
    def get_worth(value):
        if value == "Two":
            return 2
        if value == "Three":
            return 3
        if value == "Four":
            return 4
        if value == "Five":
            return 5
        if value == "Six":
            return 6
        if value == "Seven":
            return 7
        if value == "Eight":
            return 8
        if value == "Nine":
            return 9
        if value == "Ten":
            return 10
        if value == "Jack":
            return 11
        if value == "Queen":
            return 12
        if value == "King":
            return 13
        if value == "Ace":
            return 14

    def __repr__(self):
        return f"{self.value} of {self.rank}"
    
class Deck:
    def __init__(self):
        self.deck = []
        self.get_cards()
    
    def get_cards(self):
        for rank in RANKS:
            for value in VALUES:
                card = Card(rank, value)
                self.deck.append(card)

        del self.deck[35:39]

        del self.deck[44:48]

        random.shuffle(self.deck)