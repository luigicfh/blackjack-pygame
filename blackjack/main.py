import deck
import pygame
from pygame import mixer

pygame.init()

new_deck = deck.Deck()
player = deck.Player()
dealer = deck.Player()
chips = deck.Chips()

background = pygame.image.load("table_cloth.png")
d_hidden_c = pygame.image.load("dealer_card.png")
hit_button = pygame.image.load("hit_button.png")
stand_button = pygame.image.load("stand_button.png")
bj_logo = pygame.image.load("black_jack_logo.png")
spade = pygame.image.load("poker.png")
screen = pygame.display.set_mode((800,600))
chip_img = pygame.image.load('chips.png')
hit_button_bright = pygame.image.load('hit_button_bright.png')
stand_button_bright = pygame.image.load("stand_button_bright.png")
play_button = pygame.image.load('play_again.png')

pygame.display.set_caption("Black Jack")
pygame.display.set_icon(spade)

mixer.music.load("music.mp3")
mixer.music.play(-1)


#3.9844416982096
#font: trajan color

chips_font = pygame.font.Font('Trajan Pro.ttf',20)

def player_text(player_chips,x,y):
	text = chips_font.render("Player",True,(255,255,255))
	screen.blit(text,(x,y))
	text2 = chips_font.render("Bet: ${}".format(default_bet),True,(255,255,255))
	screen.blit(text2,(x,y+25))
	text3 = chips_font.render("Chips: ${}".format(player_chips-default_bet),True,(255,255,255))
	screen.blit(text3,(x,y+50))

def dealer_text(dealer_chips,x,y):
	text = chips_font.render("Dealer",True,(255,255,255))
	screen.blit(text,(x,y+15))
	text2 = chips_font.render("Chips: ${}".format(dealer_chips),True,(255,255,255))
	screen.blit(text2,(x,y+40))


#dealer card positions:
dcs_x = 392
dcs_y = 150

#dealer chips positions:
dc_x = 125
dc_y = 150

#dealer text position:
dt_x = 235
dt_y = 150

#player cards positions:
pcs_x = 392
pcs_y = 450

#player chips positions:
pc_x = 125  
pc_y = 450

#player text positions:
t_x = 235
t_y = 450

#hit button
h_x = 225
h_y = 300

#stand button
s_x = 475
s_y = 300

#play again
pa_x = 350
pa_y = 300

#logo position:
logox = 250
logoy = 35

def player_card_show(cards):

	x = 392
	y = 450
	for i in cards:
		screen.blit(i,(x,y))
		x += 62

def dealer_card_show_all(cards):

	x = 392
	y = 150
	for i in cards:
		screen.blit(i,(x,y))
		x += 62


def dealer_card_show(card_h,cards):

	x = 392
	y = 150
	screen.blit(card_h,(x,y))
	x += 62
	for i in cards[1:]:
		screen.blit(i,(x,y))
		x += 62

def hand_value(cards):

	hand_values = []

	ace = 11

	for i in cards:
		hand_values.append(new_deck.get_value(i))

	if sum(hand_values) > 21 and ace in hand_values:

		return sum(hand_values) - 10

	else:
		return sum(hand_values)

def play_again(play_button,x,y):
	screen.blit(play_button,(x,y))
		

default_bet = 20



new_deck.shuffle_deck()

for n in range(2):
	player.add_cards(new_deck.get_card())
	dealer.add_cards(new_deck.get_card())

player_chips = chips.value
dealer_chips = chips.value*10

running = True

player_turn = True

dealer_turn = False

while running:

	screen.fill((0,0,0))

	screen.blit(background,(0,0))

	player_py = []
	dealer_py = []

	for c in player.cards:
		player_py.append(deck.py_card_conversion(c))

	for c in dealer.cards:
		dealer_py.append(deck.py_card_conversion(c))

	player_card_show(player_py)

	if player_turn:

		dealer_card_show(d_hidden_c,dealer_py)

	else:
		dealer_card_show_all(dealer_py)
		play_again(play_button,pa_x,pa_y)

	mouse = pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if pygame.mouse.get_pressed() == (1,0,0):

			if h_x + 100 > mouse[0] > h_x and h_y + 62 > mouse[1] > h_y:
				card_sound = mixer.Sound('card.wav')
				card_sound.play()
				player.add_cards(new_deck.get_card())


			if s_x + 100 > mouse[0] > s_x and s_y + 62 > mouse[1] > s_y:
				card_sound = mixer.Sound('card.wav')

				card_sound.play()

				dealer_turn = True

				player_turn = False

				while dealer_turn:

					if hand_value(dealer.cards) < 17:
						dealer.add_cards(new_deck.get_card())
					else:
						dealer_turn = False
						
			if hand_value(player.cards) == hand_value(dealer.cards) and dealer_turn == False and player_turn == False:
				h_x += -2000
				h_y += -2000
				s_x += -2000
				s_y += -2000
				play_again(play_button,pa_x,pa_y)
				if pa_x + 100 > mouse[0] > pa_x and pa_y + 62 > mouse[1] > pa_y:
					new_deck = deck.Deck()
					new_deck.shuffle_deck()
					player_turn = True
					h_x = 225
					h_y = 300
					s_x = 475
					s_y = 300
					player.cards.clear()
					dealer.cards.clear()
					for n in range(2):
						player.add_cards(new_deck.get_card())
						dealer.add_cards(new_deck.get_card())

			elif hand_value(player.cards) > hand_value(dealer.cards) and dealer_turn == False and player_turn == False:
				dealer_chips -= default_bet
				player_chips += default_bet
				h_x += -2000
				h_y += -2000
				s_x += -2000
				s_y += -2000
				play_again(play_button,pa_x,pa_y)
				if pa_x + 100 > mouse[0] > pa_x and pa_y + 62 > mouse[1] > pa_y:
					new_deck = deck.Deck()
					new_deck.shuffle_deck()
					player_turn = True
					h_x = 225
					h_y = 300
					s_x = 475
					s_y = 300
					player.cards.clear()
					dealer.cards.clear()
					for n in range(2):
						player.add_cards(new_deck.get_card())
						dealer.add_cards(new_deck.get_card())

			elif hand_value(player.cards) > hand_value(dealer.cards) and dealer_turn == False and player_turn == False:
				dealer_chips += default_bet
				player_chips -= default_bet
				h_x += -2000
				h_y += -2000
				s_x += -2000
				s_y += -2000
				play_again(play_button,pa_x,pa_y)
				if pa_x + 100 > mouse[0] > pa_x and pa_y + 62 > mouse[1] > pa_y:
					new_deck = deck.Deck()
					new_deck.shuffle_deck()
					player_turn = True
					h_x = 225
					h_y = 300
					s_x = 475
					s_y = 300
					player.cards.clear()
					dealer.cards.clear()
					for n in range(2):
						player.add_cards(new_deck.get_card())
						dealer.add_cards(new_deck.get_card())			

			elif hand_value(player.cards) > 21:
				dealer_turn = True
				player_turn = False
				player_chips -= default_bet
				dealer_chips += default_bet
				h_x += -2000
				h_y += -2000
				s_x += -2000
				s_y += -2000
				if pa_x + 100 > mouse[0] > pa_x and pa_y + 62 > mouse[1] > pa_y:
					new_deck = deck.Deck()
					new_deck.shuffle_deck()
					player_turn = True
					h_x = 225
					h_y = 300
					s_x = 475
					s_y = 300
					player.cards.clear()
					dealer.cards.clear()
					for n in range(2):
						player.add_cards(new_deck.get_card())
						dealer.add_cards(new_deck.get_card())

			elif hand_value(dealer.cards) > 21:
				dealer_chips -= default_bet
				player_chips += default_bet
				s_x += -2000
				s_y += -2000
				h_x += -2000
				h_y += -2000
				play_again(play_button,pa_x,pa_y)
				if pa_x + 100 > mouse[0] > pa_x and pa_y + 62 > mouse[1] > pa_y:
					new_deck = deck.Deck()
					new_deck.shuffle_deck()
					player_turn = True
					s_x = 475
					s_y = 300
					h_x = 225
					h_y = 300
					player.cards.clear()
					dealer.cards.clear()
					for n in range(2):
						player.add_cards(new_deck.get_card())
						dealer.add_cards(new_deck.get_card())

			elif 21 >= hand_value(dealer.cards)> 17 and 17 <= hand_value(player.cards) < hand_value(dealer.cards):
				player_chips -= default_bet
				dealer_chips += default_bet
				h_x += -2000
				h_y += -2000
				s_x += -2000
				s_y += -2000
				play_again(play_button,pa_x,pa_y)
				if pa_x + 100 > mouse[0] > pa_x and pa_y + 62 > mouse[1] > pa_y:
					new_deck = deck.Deck()
					new_deck.shuffle_deck()
					player_turn = True
					h_x = 225
					h_y = 300
					s_x = 475
					s_y = 300
					player.cards.clear()
					dealer.cards.clear()
					for n in range(2):
						player.add_cards(new_deck.get_card())
						dealer.add_cards(new_deck.get_card())

			elif 21 >= hand_value(player.cards)> 17 and 17 <= hand_value(dealer.cards) < hand_value(player.cards):
				player_chips += default_bet
				dealer_chips -= default_bet
				h_x += -2000
				h_y += -2000
				s_x += -2000
				s_y += -2000
				play_again(play_button,pa_x,pa_y)
				if pa_x + 100 > mouse[0] > pa_x and pa_y + 62 > mouse[1] > pa_y:
					new_deck = deck.Deck()
					new_deck.shuffle_deck()
					player_turn = True
					h_x = 225
					h_y = 300
					s_x = 475
					s_y = 300
					player.cards.clear()
					dealer.cards.clear()
					for n in range(2):
						player.add_cards(new_deck.get_card())
						dealer.add_cards(new_deck.get_card())

			elif player_chips < 20:
				h_x += -2000
				h_y += -2000
				s_x += -2000
				s_y += -2000
				play_again(play_button,pa_x,pa_y)
				if pa_x + 100 > mouse[0] > pa_x and pa_y + 62 > mouse[1] > pa_y:
					new_deck = deck.Deck()
					new_deck.shuffle_deck()
					player_turn = True
					h_x = 225
					h_y = 300
					s_x = 475
					s_y = 300
					player.cards.clear()
					dealer.cards.clear()
					player_chips = chips.value
					dealer_chips = chips.value*10
					for n in range(2):
						player.add_cards(new_deck.get_card())
						dealer.add_cards(new_deck.get_card())


	if h_x + 100 > mouse[0] > h_x and h_y + 62 > mouse[1] > h_y:
		h_button = screen.blit(hit_button_bright,(h_x,h_y))
	else:
		screen.blit(hit_button,(h_x,h_y))

	if s_x + 100 > mouse[0] > s_x and s_y + 62 > mouse[1] > s_y:
		s_button = screen.blit(stand_button_bright,(s_x,s_y))
	else:
		screen.blit(stand_button,(s_x,s_y))

	dealer_text(dealer_chips,dt_x,dt_y)
	player_text(player_chips,t_x,t_y)

	screen.blit(bj_logo,(logox,logoy))
	screen.blit(chip_img,(pc_x,pc_y))
	screen.blit(chip_img,(dc_x,dc_y))

	pygame.display.update()