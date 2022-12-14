from random import choice, shuffle, randint

class Card:
	""" A class to model cards."""

	def __init__(self, val, suit):
		self.value = val
		self.suit = suit
		

	def show_card(self):
		print("{} of {}".format(self.value, self.suit))

	def get_suit(self):
		return self.suit

	def get_value(self):
		return self.value

	# def same_value(self, other):
	# 	return self.value == other.value
	def same_value(*cards):
		values = [v.value for v in cards]
		return len(set(values)) < 2

	# def same_suit(self, other):
	#	return self.suit == other.suit
	def same_suit(*cards):
		suits = [s.suit for s in cards]
		return len(set(suits)) < 2


class Deck:
	""" A class to model Card Decks."""

	def __init__(self):
		self.card_deck = []
		self.build_deck()

	def build_deck(self):
		for s in ['hearts', 'spades', 'clubs', 'diamonds']:
			for v in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
				self.card_deck.append(Card(v, s))

	def show(self):
		for c in self.card_deck:
			c.show_card()

	def get_first_card(self):
		return self.card_deck.pop(0)

	def get_random_card(self):
		random_card = choice(self.card_deck)
		self.card_deck.remove(random_card)
		return random_card

	def shuffle_deck(self):
		return shuffle(self.card_deck)

	def add_card(self, card):
		self.card_deck.append(card)

	def deal_hand(self, hand, num=7):
		for n in range(0, num):
			hand.add_card(self.get_first_card())

	def show_deck_size(self):
		print("Current size of Deck: {}".format(len(self.card_deck)))


class Hand(Deck):
	def __init__(self, label=''):
		self.card_deck = []
		self.label = label


# Driver Code

deck = Deck()
deck.shuffle_deck()
deck.show_deck_size()

human = Hand('human player')
computer = Hand('Computer')

deck.deal_hand(human, 7)
deck.deal_hand(computer, 7)
human.show_deck_size()
human.show()
computer.show_deck_size()
computer.show()
deck.show_deck_size()

random_computer = computer.get_random_card()
random_computer.show_card()
print(f"{random_computer.get_value()}, {random_computer.get_suit()}")
