import pygame

class TextDialogue():
	def __init__(self,engine):
		self.engine = engine
		self.tick = 0
		self.text = ''
		self.last_char = ''
		self.page = True
		self.rect = pygame.Rect(0,380,800,100)
		self.xx ,self.yy = 50,30
		self.surface = pygame.Surface((self.rect.w,self.rect.h))
		self.font = pygame.font.Font(None, 25)
		self.surface.fill((0,0,0))
		
		

	def text_seive(self):
		char = self.text[:1]
		self.text =  self.text[1:]
		return char

	def draw_text(self, text, x, y):
		img = self.font.render(text, True, (200,200,140))#colour
		self.surface.blit(img, (x, y))

	def show(self, text):
		self.text = text

	def update(self):
		self.tick+=self.engine.tick

		if self.engine.SPACE_KEY:
			self.tick+=50

		
		if self.tick>50:
			self.tick =0
			char = self.text_seive()
			if self.xx >= 690 and self.page and char==' ':
				self.xx ,self.yy = 50,55
				self.page = False
				self.last_char = ''
			elif self.xx >= 690 and not(self.page) and char==' ' :
				self.xx ,self.yy = 50,30
				self.surface.fill((0,0,0))
				self.page = True
				self.last_char = ''
			elif char == '@' :
				self.xx ,self.yy = 50,30
				self.surface.fill((0,0,0))
				self.page = True
				self.last_char = ''
			elif  char:
				i =self.font.size(self.last_char)[0]
				self.xx += i
				self.last_char = char
				self.draw_text(char,self.xx,self.yy)
				self.engine.screen.blit(self.surface,(self.rect.x,self.rect.y))
			

			elif not(char):
				
				if self.engine.SPACE_KEY:
					self.engine.game_state = 0
					self.xx ,self.yy = 50,30
					self.surface.fill((0,0,0))
					self.page = True
					self.last_char = ''
		
