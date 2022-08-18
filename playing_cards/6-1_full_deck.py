values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = [' of hearts', ' of spades', ' of clubs', ' of diamonds']

card_deck = [v+s for s in suits for v in values]
print(card_deck)

#Choose a suit and only print the cards with the suit.
spades = [c for c in card_deck if "spades" in c]
print(spades)