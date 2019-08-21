import random

class Deck:
	def __init__(self, num_of_decks):
		self.deck = []
		self.discarded_deck = []
		self.num_of_decks = num_of_decks
		self.init_deck()

	def init_deck(self):
		suit = ("♥", "♦", "♣", "♠")
		rank = ("A","2","3","4","5","6","7","8","9","10","J","Q","K")
		num_value = (1,2,3,4,5,6,7,8,9,10)

		for num in range(self.num_of_decks):
			for su in range(4):
				for ra in range(13):
					self.deck.append(Card(suit[su], rank[ra], ra+1 if ra<10 else 10))

	def shuffle(self):
		random.shuffle(self.deck)

	def take_card(self):
		card = self.deck.pop()
		self.discarded_deck.append(card)
		return card

	def take_hand(self):
		hand = Hand(self.take_card(), self.take_card())
		return hand

class Card:
	def __init__(self, suit, rank, num_value):
		self.suit = suit
		self.rank = rank
		self.num_value = num_value

class Hand:
	def __init__(self, card1, card2):
		self.hand = []
		self.hand.append(card1)
		self.hand.append(card2)
		self.total = card1.num_value + card2.num_value

	def hit(self, card):
		self.hand.append(card)
		self.total += card.num_value

for card in Deck(2).deck:
	print(card.rank, card.suit, card.num_value)






	






