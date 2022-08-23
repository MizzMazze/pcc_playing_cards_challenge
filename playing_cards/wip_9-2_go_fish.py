from random import choice, shuffle, randint
import operator

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

	def deal_hand(self, hand, num):
		for n in range(0, num):
			hand.add_card(self.get_first_card())

	def show_deck_size(self):
		print("Current size of Deck: {}".format(len(self.card_deck)))

class Player:
	def __init__(self, name, hand_size, book):
		self.name = name
		self.hand_size = hand_size
		self.hand = Hand(hand_size)
		self.book = book

class Hand(Deck):
	def __init__(self, hand_size):
		self.card_deck = []
		# self.label = label






def check_pairs(hand, table):
	hand_sorted = sorted(hand, key=lambda v: v.value)
	pairs = []
	print(len(hand_sorted))
	if len(hand_sorted) > 1:
		index = 0
		while index < len(hand_sorted)-1:
			if hand_sorted[index].get_value() == hand_sorted[index+1].get_value():
				pairs.append(hand_sorted[index])
				pairs.append(hand_sorted[index+1])
			index += 1
			if len(pairs) > 0:
				for p in pairs:
					hand_sorted.remove(p)
				index = 0
				table.append(pairs)
				pairs = []
		return hand_sorted, table


# Driver Code

deck = Deck()
deck.shuffle_deck()
deck.show_deck_size()

# hand.card_deck.show()
# test_book = []
test = Player('test', 7, [])
deck.deal_hand(test.hand, 7)

print(test.name, test.book)
test.hand.show()
print(dir(test.hand))


# player = deck.deal_hand()
# player_table = []

# computer = deck.deal_hand()

# player, player_table = check_pairs(player, player_table)

"""for p in player:
	p.show_card()"""

"""random_pick = choice(computer)
random_pick.show_card()
random_pick.get_suit()
random_pick.get_value()
print(f"{random_pick.get_value()}, {random_pick.get_suit()}")"""
