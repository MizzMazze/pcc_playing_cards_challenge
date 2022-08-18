values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = [' of hearts', ' of spades', ' of clubs', ' of diamonds']

card_suit = []
cards = [[v+s for v in values] for s in suits]
print(cards)


for v in values:
	card_suit.append(v + suits[0])
print(card_suit)