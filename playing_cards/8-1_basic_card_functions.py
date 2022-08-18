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


#Driver Codes
deck = build_deck()
print(deck)

suit = '2 of hearts'
print(get_suit(suit))

card = '10 of spades'
print(get_value(card))


first = '3 of hearts'
second = '3 of clubs'
third = '3 of diamonds'
fourth = '3 of spades'
fifth = '5 of hearts'
print(same_value(first, second, third, fourth))

print(same_suit(first, suit, fifth))