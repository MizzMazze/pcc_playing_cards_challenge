values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = [' of hearts', ' of spades', ' of clubs', ' of diamonds']

card_deck = []

for s in suits:
	for c in (values):
		card_deck.append(c + s)
print(card_deck)

#Choose a suit and only print the cards with the suit.
spades = [c for c in card_deck if "spades" in c]
print(spades)