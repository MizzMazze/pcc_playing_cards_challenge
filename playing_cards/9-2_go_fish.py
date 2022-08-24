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

def player_ask(player, player_book, opponent):
	# opponent = sorted(opponent.card_deck, key=lambda v: v.value)
	index = 0
	pair = []
	len_opponent_hand = len(opponent.card_deck)-1
	while True:
		pick = player_pick(player)
		while index <= len_opponent_hand:
			# print(pick)
			# comment row below out when finished with debugging
			# opponent_card = opponent.card_deck[index].show_card()
			if Card.same_value(pick, opponent.card_deck[index]):
				print(f"found a pair of {pick.get_value()} and {opponent.card_deck[index].get_value()}")
				print("Removing pair from both Decks")
				pair.append(pick)
				pair.append(opponent.card_deck[index])
				player_book.append(pair)
				pair = []
				player.card_deck.remove(pick)
				del opponent.card_deck[index]
				if not player.card_deck or not opponent.card_deck:
					return player_book
				index = 0
				len_opponent_hand = len(opponent.card_deck)-1
				pick = player_pick(player)
				continue
			else:
				index += 1
		player_go_fish()
		player.card_deck, player_book = check_pairs(player.card_deck, player_book)
		return player_book

def player_go_fish():
	print("Go Fish!")
	deck.deal_hand(human, 1)

def computer_pick(computer_hand):
	return computer_hand.get_random_card()

def computer_ask(computer_hand, computer_book, opponent_hand):
	index = 0
	pair = []
	len_opponent_hand = len(opponent_hand.card_deck)-1
	while True:
		computer_card = computer_pick(computer_hand)
		print(f"Do you have any {computer_card.get_value()}s ?")
		while index <= len_opponent_hand:
			if Card.same_value(computer_card, opponent_hand.card_deck[index]):
				print(f"found a pair of {computer_card.get_value()} and {opponent_hand.card_deck[index].get_value()}")
				print("Adding pair to my book")
				pair.append(computer_card)
				pair.append(opponent_hand.card_deck[index])
				computer_book.append(pair)
				pair = []
				del opponent_hand.card_deck[index]
				if not computer_hand.card_deck or not opponent_hand.card_deck:
					return computer_book
				index = 0
				len_opponent_hand = len(opponent_hand.card_deck)-1
				computer_card = computer_pick(computer_hand)
				print(f"Do you have any {computer_card.get_value()}s ?")
				continue
			else:
				index += 1
		computer_hand.add_card(computer_card)
		# computer_hand.show()
		computer_go_fish()
		# print("---")
		computer_hand.card_deck, computer_book = check_pairs(computer_hand.card_deck, computer_book)
		# computer.show()
		return computer_book

def computer_go_fish():
	print("Computer goes fishing!")
	deck.deal_hand(computer, 1)
	

# Driver Code

# Build Deck
deck = Deck()
deck.shuffle_deck()


# Initialize Players and books
human = Hand('player')
human_book = []
computer = Hand('computer')
computer_book = []

# Deal hands to players
deck.deal_hand(human, 7)
deck.deal_hand(computer, 7)

# Check for pairs after initial deal
human.card_deck, human_book = check_pairs(human.card_deck, human_book)
computer.card_deck, computer_book = check_pairs(computer.card_deck, computer_book)


# Game running
while len(human.card_deck) > 0 and len(computer.card_deck) > 0:

	if not human.card_deck or not computer.card_deck:
		break
	print("Human player turn")
	# show opponent hand for debugging
	# computer.show()
	human_book = player_ask(human, human_book, computer)

	if not computer.card_deck or not human.card_deck:
		break
	print("Computer player turn")
	# Show opponent hand for debugging
	# human.show()
	computer_book = computer_ask(computer, computer_book, human)

# Winning conditions
if len(human_book) > len(computer_book):
	print(f"No. of Pairs of Human Player: {len(human_book)}")
	print(f"No. of Pairs of Computer Player: {len(computer_book)}")
	print(f"Human player has won this game with {len(human_book)} pairs")
elif len(human_book) < len(computer_book):
	print(f"No. of Pairs of Computer Player: {len(computer_book)}")
	print(f"No. of Pairs of Human Player: {len(human_book)}")
	print(f"Computer player has won this game with {len(computer_book)} pairs")
else:
	print(f"No. of Pairs of Human Player: {len(human_book)}")
	print(f"No. of Pairs of Computer Player: {len(computer_book)}")
	print("The game ended in a draw")

print("Game over")