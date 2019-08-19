class Card:
	def __init__(self, suit, rank, num_value):
		self.suit = suit
		self.rank = rank
		self.num_value = num_value

deck = []
suit = ["♥", "♦", "♣", "♠"] 
rank = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
num_value = [1,2,3,4,5,6,7,8,9,10]

for s in range(4):
	for r in range(13):
		deck.append(Card(suit[s], rank[r], r+1 if r<10 else 10))

for card in deck:
	print(card.rank, card.suit, card.num_value)





	






