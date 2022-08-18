from random import choice, shuffle, randint

def build_deck():
	values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
	suits = [' of hearts', ' of spades', ' of clubs', ' of diamonds']
	return [v+s for s in suits for v in values]

def get_suit(card):
	suit = card.split(' ')
	return suit[-1]

def get_value(card):
	card_value = card[:2].strip()
	if card_value == 'J':
		return 'Jack'
	elif card_value == 'Q':
		return 'Queen'
	elif card_value == 'K':
		return 'King'
	elif card_value == 'A':
		return 'Ace'
	else:
		return card_value

def same_value(*cards):
	value_list = [c[:2].strip() for c in cards]
	return all(c == value_list[0] for c in value_list)

def same_suit(*cards):
	suit_list = [s[5:].strip() for s in cards]
	return all(s == suit_list[0] for s in suit_list)

def deal_top_card(card_deck):
	return card_deck.pop(0)

def get_random_card(card_deck):
	random_card = choice(card_deck)
	card_deck.remove(random_card)
	return random_card


def shuffle_deck(card_deck):
	shuffle(card_deck)
	return card_deck

def deal_hand(card_deck, hand_size):
	hand = []
	for i in range(0, hand_size):
		hand.append(card_deck.pop(randint(0,len(card_deck)-1)))
	return hand

def deal_hands(card_deck, hand_size, n_hands=2):
	hands = []
	for i in range(0, n_hands):
		hands.append(deal_hand(card_deck, hand_size))
	return hands

#Driver Codes

players = 2
hand_size = 7
table = []

hands_deal = shuffle_deck(build_deck())
hands = deal_hands(hands_deal, hand_size, players)


player_1 = hands[0]
player_2 = hands[1]
print(player_1)
print(player_2)