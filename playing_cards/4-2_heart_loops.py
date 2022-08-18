card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suit_name = ' of hearts'

card_deck = []

for c in range(len(card_values)):
	card_deck.append(card_values[c] + suit_name)

for c in range(len(card_deck)):
	print(card_deck[c])
print("\n")

for number_card in card_deck[:9]:
	print(number_card)

print("\n")
for face_card in card_deck[9:13]:
	print(face_card)