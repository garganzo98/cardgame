from card import card

class deck:
	def_init_(self):
	self.value = []
	self.validSuits = ["clubs","spades", "hearts", "diamonds"]
	self.validRanks = ["2","3","4","5","6","7","8","9","10","jack","queen","king","ace"]
	for suit in self.validSuits:
		for rank in self.validRanks:
			print(suit,rank)

startingDeck = Deck()