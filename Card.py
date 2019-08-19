class Card:
	def __init__(self, suit, rank, num_value):
		self.suit = suit
		self.rank = rank
		self.num_value = num_value

deck = []
suit = ["♥", "♦", "♣", "♠"] 
rank = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
num_value = [1,2,3,4,5,6,7,8,9,10]

for i in range(0,13):
	deck.append(Card("♥",rank[i], i+1 if i<10 else 10))
	deck.append(Card("♦",rank[i], i+1 if i<10 else 10))
	deck.append(Card("♣",rank[i], i+1 if i<10 else 10))
	deck.append(Card("♠",rank[i], i+1 if i<10 else 10))





	






