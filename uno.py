NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
COLORS = ["🔴","🟢","🟡","🔵" ]


class Card:
    def __init__(self, number, color):
        self.number = number
        self.color = color

    def ___str___(self):
        return f"{self.color} {self.number}"   


class Player:
    def __init__(self, name):
        self.name = name 
        self.hand = []

    def __str__(self):
        return f'{self.name}'


class Deck:
    def __init__(self, numbers, colors):
        self.cards = []
        for number in numbers:
            for color in colors:
                card = (color, number)
                self.cards.append(card)
        
    def shuffle(self):
        def shuffle(self):
         shuffle_deck:list = []    
         deck_to_shuffle = self.cards.copy()
        while len(deck_to_shuffle) > 0:
            # pull random card from unshuffled deck
            card_to_move = deck_to_shuffle [randint(0, len(deck_to_shuffle) -1)]
            # put it in random deck
            deck_to_shuffle.remove(card_to_move)
            # now remove it from original deck
            shuffle_deck.append(card_to_move)
        return shuffle_deck

class Game:
    def __init___(self):
        self.deck = Deck(NUMBERS, COLORS).shuffle()
        self.player1 = Player("Joe")
        self.player2 = Player("Mary")
        for card in self.deck:
            print(card)
        print(self.player1, self.player2)

    def deal_cards(self):
        for i in range(7):
          self.player1.hand.append(self.deck.pop())
          self.player2.hand.append(self.deck.pop())
        print(len(self.player1.hand), len(self.player2.hand))

game = Game()
deck = game.deck 
game.deal_cards()
