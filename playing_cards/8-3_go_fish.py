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

def check_pairs(hand, table):
	hand.sort()
	pairs = []
	if len(hand) > 1:
		index = 0
		while index < len(hand) -1:
			if hand[index][:2].strip() == hand[index+1][:2].strip():
				pairs.append(hand[index])
				pairs.append(hand[index+1])
			index += 1
			if len(pairs) > 0:
				for i in pairs:
					hand.remove(i)
				index = 0
				table.append(pairs)
				pairs = []
		return hand, table

def pick_card(player_hand):
	while True:
		print(f"your hand {player_hand}")
		pick = input("Pick a card from your hand: ")
		if any(pick in card for card in player_hand):
			pick_value = get_value(pick)
			print(f"Do you have a {pick_value}?")
			get_pick_index = int(''.join([str(player_hand.index(n)) for n in player_hand if pick_value in get_value(n)]))
			# variation: get pick index by using a generator -> from stackoverflow.
			# pick_generator = (i for i, c in enumerate(player_hand) if pick in c)
			# pick_index = next(pick_generator)
			return player_hand[get_pick_index]
		print("This card is not in your hand.")

def player_ask(player, opponent, player_table):
	opponent.sort()
	index = 0
	pair = []
	len_opponent_hand = len(opponent)-1
	while True:
		pick = pick_card(player)
		while index <= len_opponent_hand:
			if same_value(pick, opponent[index]):
				print(f"Found a pair {pick} and {opponent[index]}")
				print("Removing pair from decks")
				pair.append(pick)
				pair.append(opponent[index])
				player_table.append(pair)
				pair = []
				player.remove(pick)
				del opponent[index]
				if not player or not opponent:
					return player_table, pick
				index = 0
				len_opponent_hand = len(opponent)-1
				pick = pick_card(player)
				continue
			else:
				index += 1
		player_go_fish()
		player, player_table = check_pairs(player, player_table)
		player1_last_picks.append(get_value(pick))
		return player_table, player1_last_picks

def player_go_fish():
	print("Go Fish!")
	player1.append(deal_top_card(hands_deal))
	return player1


def computer_pick(computer_hand, opponent_last_picks):
	# print(f"the previous picks from player 1: {opponent_last_picks}")
	for c in computer_hand:
		if get_value(c) in opponent_last_picks:
			opponent_last_picks.remove(get_value(c))
			return c
	return choice(computer_hand)

def computer_ask(computer_hand, computer_table, opponent_hand, opponent_last_picks):
	opponent_hand.sort()
	index = 0
	pair = []
	len_opponent_hand = len(opponent_hand)-1
	while True:
		computer_card = computer_pick(computer_hand, opponent_last_picks)
		print(f"Do you have any {get_value(computer_card)}?")
		while index <= len_opponent_hand:
			if same_value(computer_card, opponent_hand[index]):
				print(f"Found a pair of {computer_card} and {opponent_hand[index]}")
				print("Adding pair to my table")
				pair.append(computer_card)
				pair.append(opponent_hand[index])
				computer_table.append(pair)
				pair = []
				computer_hand.remove(computer_card)
				del opponent_hand[index]
				if not computer_hand or not opponent_hand:
					return computer_table, computer_card
				index = 0
				len_opponent_hand = len(opponent_hand)-1
				computer_card = computer_pick(computer_hand, opponent_last_picks)
				print(f"Do you have any {get_value(computer_card)}?")
				continue
			else:
				index += 1
		computer_hand = computer_go_fish()
		computer_hand, computer_table = check_pairs(computer_hand, computer_table)
		player2_last_picks.append(computer_card)
		# return computer_table, computer_card
		return computer_table, player2_last_picks

def computer_go_fish():
	print("Go Fish!")
	player2.append(deal_top_card(hands_deal))
	return player2

# Game start
players = 2
hand_size = 7

hands_deal = shuffle_deck(build_deck())
hands = deal_hands(hands_deal, hand_size, players)


player1 = hands[0]
# player1 = ['A of spades', 'K of clubs', 'Q of hearts', 'J of diamonds']
player1_table = []
player1_last_picks = []

player2 = hands[1]
# player2 = ['A of diamonds', 'K of spades', 'Q of clubs', 'J of hearts', '10 of spades']
player2_table = []
player2_last_picks = []



player1, player1_table = check_pairs(player1, player1_table)
player2, player2_table = check_pairs(player2, player2_table)

# Game running
while len(player1) > 0 and len(player2) > 0:

	if not player1 or not player2:
		break
	print("player 1 turn")
	# Cheat print for testing purposes
	# print(f"Hand of player 2: {player2}")
	# print(f"last requests from computer {player2_last_picks}")
	player1_table, player1_last_picks = player_ask(player1, player2, player1_table)

	if not player2 or not player1:
		break
	print("player 2 turn")
	# Cheat print for testing purposes
	# print(f"Hand of player 1: {player1}")
	print("computers turn")
	player2_table, player2_last_picks = computer_ask(player2, player2_table, player1, player1_last_picks)
	

# Winning conditions:
if len(player1_table) > len(player2_table):
	print(f"No. of Pairs of Player 1: {len(player1_table)}")
	print(f"No. of Pairs of Player 2: {len(player2_table)}")
	print(f"Player 1 has won this game with {len(player1_table)} pairs")
elif len(player2_table) > len(player1_table):
	print(f"No. of Pairs of Player 2: {len(player2_table)}")
	print(f"No. of Pairs of Player 1: {len(player1_table)}")
	print(f"Player 2 has won this game with {len(player2_table)} pairs")
else:
	print(f"No. of Pairs of Player 1: {len(player1_table)}")
	print(f"No. of Pairs of Player 2: {len(player2_table)}")
	print("The game ended in a draw")
print("game finished")




