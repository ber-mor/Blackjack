class Deck:
	def __init__(self, num_of_decks):
		self.deck = []
		self.discarded_deck = []
		self.num_of_decks = num_of_decks

	# def init_deck(self):

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

deck = []
suit = ("♥", "♦", "♣", "♠")
rank = ("A","2","3","4","5","6","7","8","9","10","J","Q","K")
num_value = (1,2,3,4,5,6,7,8,9,10)

for s in range(4):
	for r in range(13):
		deck.append(Card(suit[s], rank[r], r+1 if r<10 else 10))

for card in deck:
	print(card.rank, card.suit, card.num_value)






	






