from PIL import Image
from random import shuffle
import pygame

card_image = Image.open('deck-of-cards-tutorial.png')
chip_100 = Image.open("poker_chip_100.png")
chip_200 = Image.open('poker_chip_200.png')
chip_400 = Image.open('poker_chip_400.png')

class Deck:

	def __init__(self):

		self.card_images = []

		total_w = 800
		total_h = 324

		w = 800/13
		h = 81
		x = 0
		y = 0

		while y != total_h:
	        
			card = card_image.crop((x,y,w,h))
			self.card_images.append(card)

			w += 800/13
			x += 800/13

			if x == 800:

				w = 800/13
				x = 0
				h += 81
				y += 81

			if y == total_h:
				break

		self.deck = []
	
		for i in self.card_images:

			self.deck.append(i)

		self.spades = self.card_images[0:13]
		self.clubs = self.card_images[13:26]
		self.diamonds = self.card_images[26:39]
		self.hearts = self.card_images[39:]

		self.spades_values = {}
		self.clubs_values = {}
		self.diamonds_values = {}
		self.hearts_values = {}

		value_of_cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

		i = 0
		for c in self.spades:
			self.spades_values.update({str(c):value_of_cards[i]})
			i += 1

		i = 0
		for c in self.clubs:
			self.clubs_values.update({str(c):value_of_cards[i]})
			i += 1

		i = 0
		for c in self.diamonds:
			self.diamonds_values.update({str(c):value_of_cards[i]})
			i += 1

		i = 0
		for c in self.hearts:
			self.hearts_values.update({str(c):value_of_cards[i]})
			i += 1

		self.suits_ranks = [self.spades_values,self.clubs_values,self.diamonds_values,self.hearts_values]

	def shuffle_deck(self):

		shuffle(self.deck)

	def get_card(self):

		card = self.deck.pop()
		return card

	def get_value(self,card):

		for suit in self.suits_ranks:
			for k in suit:
				if str(card) in k:
					return suit[str(card)]



class Chips:

	def __init__(self,value=100):
		self.value = value


class Player(Deck):

	def __init__(self):
		super().__init__()

		self.cards = []
		self.values = []
		self.sum_values = 0
		self.chips = []
		self.c_values = []
		self.sum_c_values = None

	def add_cards(self,card):

		self.cards.append(card)

	def adjust_for_ace(self,values):

		if self.sum_values > 21 and 11 in self.values:
			self.sum_values -= 10

def py_card_conversion(card):

    mode = card.mode
    size = card.size
    data = card.tobytes()
    py_card = pygame.image.fromstring(data,size,mode)
    return py_card
