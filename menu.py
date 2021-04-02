import pygame


class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.clicked = False

	def draw(self,screen):
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False


		#draw button
		screen.blit(self.image, self.rect)

		return action


class Menu():
	def __init__ (self,engine):
		self.engine = engine 
		self.buttons = {}
		self.font = pygame.font.SysFont("Verdana", 70)#, True, True)
		self.white = (255,255,255)
		self.black = (0,0,0)
		self.colour = self.black

	def draw(self):
		for button in self.buttons :
			self.buttons[button][1] = (self.buttons[button][0].draw(self.engine.screen))
	
	def draw_text(self, text, colour):
		img = self.font.render(text, True, colour)
		return img

	def add(self, text, x, y):
		self.buttons[text] = [Button(x, y, self.draw_text(text, self.colour)), False]


class Mainmenu(Menu):
	def __init__(self, engine):
		Menu.__init__(self,engine)
		self.font = pygame.font.SysFont("Verdana", 30, True, True)
		self.colour = (170, 255, 255)
		self.add('A GAME', 320, 50)
		self.add('Start', 370, 150)
		self.add('Options',340,250)
		self.add('Exit', 370, 350)


class Deadmenu(Menu):
	def __init__(self, engine):
		Menu.__init__(self,engine)
		self.font = pygame.font.SysFont("Verdana", 30, True, True)
		self.colour = (170, 255, 255)
		self.add('Exit', 550, 250)
		self.add('Restart', 170, 250)



