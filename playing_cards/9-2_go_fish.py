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


class Hand(Deck):
	def __init__(self, label=''):
		self.card_deck = []
		self.label = label


def check_pairs(hand, book):
	hand_sorted = sorted(hand, key=lambda v: v.value)
	pairs = []
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
				book.append(pairs)
				pairs = []
		return hand_sorted, book

def player_pick(human):
	while True:
		print("your hand:")
		human.show()
		pick = input("Pick a card from your hand: ")
		if any(pick in card.get_value() for card in human.card_deck):
			print(f"Do you have any {pick}s ?")
			# test = [human.card_deck.index(pick) for card in human.card_deck if card.get_value() == pick]
			# value_list = [card.get_value() for card in human.card_deck if card.get_value() == pick]
			indices = (i for i, card in enumerate(human.card_deck) if card.get_value() == pick)
			# print(value_list)
			# print(human.card_deck)
			return human.card_deck[next(indices)]
		print("This card is not in your hand.")

def player_ask(player, opponent, player_book):
	opponent_sorted = sorted(opponent.card_deck, key=lambda v: v.value)
	index = 0
	pair = []
	len_opponent_hand = len(opponent.card_deck)-1
	while True:
		pick = player_pick(player)
		while index <= len_opponent_hand:
			player_card = pick.get_value()
			opponent_card = opponent.card_deck[index].get_value()
			print(player_card, opponent_card)
			index += 1
			if Card.same_value(pick, opponent.card_deck[index]):
				return pick


# Driver Code

deck = Deck()
deck.shuffle_deck()
# deck.show_deck_size()

human = Hand('player')
deck.deal_hand(human, 7)
human_book = []

computer = Hand('computer')
deck.deal_hand(computer, 7)
computer_book = []


"""human.show_deck_size()
human.show()
computer.show_deck_size()
computer.show()
deck.show_deck_size()"""

human.card_deck, human_book = check_pairs(human.card_deck, human_book)
human.show()
print(len(human_book))
computer.card_deck, computer_book = check_pairs(computer.card_deck, computer_book)
computer.show()
print(len(human_book))


test = player_ask(human, computer, human_book)
print(test)
