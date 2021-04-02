import pygame
from spritesheetparser import Spritesheet

class Player(pygame.sprite.Sprite):
	def __init__(self,engine):
		pygame.sprite.Sprite.__init__(self)
		self.engine = engine
		self.friction = -0.09
		self.image = pygame.image.load('img/rpgTile211.png')
		self.image = pygame.transform.scale(self.image, (32,32))
		self.rect = self.image.get_rect()
		self.position, self.velocity = pygame.math.Vector2(100,100), pygame.math.Vector2(0,0)
		self.acceleration = pygame.math.Vector2(5,5)
		self.max_vel = 8
		self.bump = False

	def draw(self):
		self.engine.screen.blit(self.image, (self.rect.x - self.engine.camera.offset.x, self.rect.y - self.engine.camera.offset.y))


	def update(self):
		
		#print(self.rect)
		#print(self.rect.w)
		self.vertical_movement(self.engine.dt)
		self.checkCollisionsy(self.engine.tiles)
		
		self.horizontal_movement(self.engine.dt)
		self.checkCollisionsx(self.engine.tiles)


	def horizontal_movement(self,dt):		
		self.acceleration.x = 0
		if self.engine.LEFT_KEY and not self.bump:
			self.acceleration.x -= .6
		elif self.engine.RIGHT_KEY and not self.bump:
			self.acceleration.x += .6
		self.acceleration.x += self.velocity.x * self.friction
		self.velocity.x += self.acceleration.x * dt
		self.limit_x_velocity(self.max_vel)
		self.position.x += self.velocity.x * dt + (self.acceleration.x * .5) * (dt * dt)
		self.rect.x = self.position.x
		


	def vertical_movement(self,dt):
		self.acceleration.y = 0
		if self.engine.UP_KEY and not self.bump:
			self.acceleration.y -= .6
		elif self.engine.DOWN_KEY and not self.bump:
			self.acceleration.y += .6
		self.acceleration.y += self.velocity.y * self.friction
		self.velocity.y += self.acceleration.y * dt
		self.limit_y_velocity(self.max_vel)
		self.position.y += self.velocity.y * dt + (self.acceleration.y * .5) * (dt * dt)
		self.rect.y = self.position.y


	def limit_x_velocity(self, max_vel):
		self.velocity.x = max(-max_vel, min(self.velocity.x, max_vel))
		if abs(self.velocity.x) < .11: self.velocity.x = 0


	def limit_y_velocity(self, max_vel):
		self.velocity.y = max(-max_vel, min(self.velocity.y, max_vel))
		if abs(self.velocity.y) < .11: self.velocity.y = 0


	def get_hits(self, tiles):
		hits = []
		for tile in tiles:
			if self.rect.colliderect(tile):
				if tile.can_collide :
					hits.append(tile)
					#print(tile.rect)
		return hits


	def checkCollisionsx(self, tiles):
		collisions = self.get_hits(tiles)
		self.bump = False
		for tile in collisions:
			if self.velocity.x > 0:  # Hit tile moving right
				self.position.x = tile.rect.left - self.rect.w
				self.rect.x = self.position.x 
				self.velocity.x = 0
				self.bump = True
			elif self.velocity.x < 0:  # Hit tile moving left
				self.position.x = tile.rect.right
				self.rect.x = self.position.x 
				self.velocity.x = 0
				self.bump = True
		
			

	def checkCollisionsy(self, tiles):
		collisions = self.get_hits(tiles)
		self.bump = False
		for tile in collisions:
			if self.velocity.y > 0:  # Hit tile moving down
				self.position.y = tile.rect.top - self.rect.h
				self.rect.y = self.position.y
				self.bump = True 
				#- 2
				self.velocity.y = 0
			elif self.velocity.y < 0:  # Hit tile moving up
				self.position.y = tile.rect.bottom
				self.rect.y = self.position.y 
				self.velocity.y = 0
				self.bump = True
		