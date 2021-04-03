import pygame
from pygame import Rect



class Enemy1(pygame.sprite.Sprite):

	def __init__(self, x, y,q):
		pygame.sprite.Sprite.__init__(self)
		self.images_right = []
		self.images_left = []
		self.index = 0
		self.size = (40, 40)
		for num in range(1, 6):
			img_left = pygame.image.load(f'img/blob/l{num}.png')
			img_right = pygame.image.load(f'img/blob/r{num}.png')
			img_right = pygame.transform.scale(img_right, self.size)
			img_left = pygame.transform.scale(img_left, self.size)
			self.images_left.append(img_left)
			self.images_right.append(img_right)
		for num in range(1, 6):
			img_left = pygame.image.load(f'img/blob/l{num}.png')
			img_right = pygame.image.load(f'img/blob/r{num}.png')
			img_right = pygame.transform.scale(img_right, self.size)
			img_left = pygame.transform.scale(img_left, self.size)
			img_left = pygame.transform.flip(img_right, True, False)
			img_right = pygame.transform.flip(img_left, True, False)
			self.images_left.append(img_left)
			self.images_right.append(img_right)
		self.image = self.images_right[self.index]
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.move_direction = 1
		self.move_counter = 0
		self.x_correction=0
		self.direction=False
		self.tick = 0

	def update(self,tick):
		walk_cooldown = 15
		self.tick += tick

		#update movemnets
		self.rect.x += self.move_direction
		self.move_counter += 1
		if abs(self.move_counter) > 63:
			 
			self.direction = not(self.direction)
			self.move_direction *= -1
			self.move_counter *= -1
			#print(self.move_direction)

		#update animation
		if abs(self.move_counter) > walk_cooldown and self.tick > 32:
			self.tick=0
			self.counter = 0	
			self.index += 1
			if self.index >= len(self.images_right) or self.index >= len(self.images_left) :
				self.index = 0
			if  self.move_direction == 1:
				self.image = self.images_right[self.index]
			if  self.move_direction == -1:
				self.image = self.images_left[self.index]


class Lava(pygame.sprite.Sprite):
	def __init__(self, x, y,tile_size):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('img/lava.png')
		self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.tick = 0

	def update(self,tick):
		self.tick +=tick
		# To animate the lava //in ms 4fps
		if self.tick > 250 :
			self.tick = 0
			self.image = pygame.transform.flip(self.image, True, False)


class House(pygame.sprite.Sprite):
	def __init__(self, x, y, tile_size, type):
		pygame.sprite.Sprite.__init__(self)
		if type == 'small':
			img = pygame.image.load('img/house0.png')
			self.image = pygame.transform.scale(img,(128,128))
			self.offset = 48
		elif type == 'mid':
			img = pygame.image.load('img/house_final.png')
			self.image = pygame.transform.scale(img,(128,128))
			self.offset = 48
		elif type == 'big':
			img = pygame.image.load('img/house_final.png')
			self.image = pygame.transform.scale(img,(128,128))
			self.offset = 48

		self.tick = 0
		self.can_collide = True
		self.rect = self.image.get_rect()
		self.rect.x = x 
		self.rect.y = y + self.offset
		self.rect.h = self.rect.h - self.offset


		


class Enemy2(pygame.sprite.Sprite):
	def __init__(self, x, y,tile_size):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('img/coin.png')
		self.image = pygame.transform.scale(img, (tile_size//2, tile_size // 2))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.tick = 0
	

class Exit(pygame.sprite.Sprite):
	def __init__(self, x, y,tile_size):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('img/Exit.png')
		self.image = pygame.transform.scale(img, (tile_size, tile_size * 2))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y - tile_size
		self.tick = 0

