import pygame
from abc import ABC, abstractmethod

class Camera:
	def __init__(self, engine):
		self.engine = engine
		self.player = self.engine.player
		self.offset_float = pygame.math.Vector2(0, 0)
		self.offset = pygame.math.Vector2(0, 0)
		self.screen_width, self.screen_height = self.engine.screen_width, self.engine.screen_height
		self.CONST = pygame.math.Vector2(-self.screen_width / 2 + self.player.rect.w / 2, -self.screen_height / 2 + self.player.rect.h/2 )

	def setmethod(self, method):
		self.method = method

	def scroll(self):
		self.method.scroll()

	def reset_cam(self):
		self.offset = pygame.math.Vector2(0, 0)
		self.scrollval = pygame.math.Vector2(0, 0)

class CamScroll(ABC):
	def __init__(self, engine):
		self.engine = engine
		self.camera = engine.camera
		self.player = engine.player

	@abstractmethod
	def scroll(self):
		pass

class Follow(CamScroll):
	def __init__(self, engine):
		CamScroll.__init__(self, engine)

	def scroll(self):
		self.camera.offset_float.x += (self.player.rect.x - self.camera.offset_float.x + self.camera.CONST.x)
		self.camera.offset_float.y += (self.player.rect.y - self.camera.offset_float.y + self.camera.CONST.y)
		self.camera.offset.x, self.camera.offset.y = int(self.camera.offset_float.x), int(self.camera.offset_float.y)

class Border(CamScroll):
	def __init__(self, engine):
		CamScroll.__init__(self, engine)

	def scroll(self):
		self.camera.offset_float.x += (self.player.rect.x - self.camera.offset_float.x + self.camera.CONST.x)
		self.camera.offset_float.y += (self.player.rect.y - self.camera.offset_float.y + self.camera.CONST.y)
		self.camera.offset.x, self.camera.offset.y = int(self.camera.offset_float.x), int(self.camera.offset_float.y)
		self.camera.offset.x = max(self.engine.left_border, self.camera.offset.x)
		self.camera.offset.x = min(self.camera.offset.x, self.engine.right_border - self.camera.screen_width)
		self.camera.offset.y = max(self.engine.top_border, self.camera.offset.y)
		self.camera.offset.y = min(self.camera.offset.y, self.engine.bottom_border - self.camera.screen_height)

class Auto(CamScroll):
	def __init__(self,engine):
		CamScroll.__init__(self,engine)

	def scroll(self):
		self.camera.offset.x += 1


