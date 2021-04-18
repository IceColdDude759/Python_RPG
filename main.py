import pygame
from spritesheetparser import Spritesheet
from tiles import TileMap
from camera import *
from Player import *
from hud import *
import json


class Engine():
	def __init__(self):
		
		pygame.init()
		#pygame.mixer.pre_init(44100, -16, 2, 512)
		#mixer.init()
		self.clock = pygame.time.Clock()
		self.FPS = 60
		self.running = True
		self.menu_bol = False
		self.screen_width, self.screen_height = 800, 480
		self.tile_size = 32
		self.flags = pygame.RESIZABLE | pygame.SCALED
		
		self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), self.flags)
		self.title = "A GAME"
		pygame.display.set_caption(self.title)

		
		self.reset_level('mainmap')
		
		
		
		self.dt = 0
		self.time = 0
		self.menu = False
		self.game_state = 0		
		self.tick = 0
		self.init_keys()
		self.dialoge_box = TextDialogue(self)
		self.dia = True


	def reset_level(self, level):
		self.game_state = 0
		self.house_group = HomeGroup(self)
		self.grass_group = ModifiedGroup(self)
		self.water_group = ModifiedGroup(self)
		self.enemy_group = ModifiedGroup(self)
		self.teleport_group = ModifiedGroup(self)
		self.tree_group = ModifiedGroup(self)

		with open('map/mainmap.json') as f:
			self.gates = json.load(f)
		level = self.gates[level]
		self.world = TileMap(f'map/{level}.csv', self)
		self.tiles = self.world.tiles
		self.left_border = 0
		self.top_border = 0
		self.bottom_border = self.world.map_h
		self.right_border = self.world.map_w

		self.player = Player(self)
		self.camera = Camera(self)
		self.follow = Follow(self)
		self.border = Border(self)
		self.auto = Auto(self)
		self.camera.setmethod(self.border)

	
	def menuload(self):
		pass

	
	def init_keys (self):
		self.LEFT_KEY, self.RIGHT_KEY = False, False
		self.UP_KEY, self.DOWN_KEY = False, False
		self.SPACE_KEY = False


	def daynight(self):
		time=self.time
		if time >= 4800:
				time = 0
				print('1')
		elif time >= 2400:
				print('2')

	def input(self):
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				self.running = False

				## PROCESS KEYPRESS
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					self.LEFT_KEY = True
				elif event.key == pygame.K_RIGHT:
					self.RIGHT_KEY = True
				elif event.key == pygame.K_UP:
					self.UP_KEY = True
				elif event.key == pygame.K_DOWN:
					self.DOWN_KEY = True
				elif event.key == pygame.K_SPACE:
					self.SPACE_KEY = True

				## HANDEL CAMERA MOVEMENT	
				elif event.key == pygame.K_1:
					self.camera.setmethod(self.follow)
				elif event.key == pygame.K_2:
					self.camera.setmethod(self.auto)
				elif event.key == pygame.K_3:
					self.camera.setmethod(self.border)

				elif event.key == pygame.K_ESCAPE:
					self.running = False

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					self.LEFT_KEY = False
				elif event.key == pygame.K_RIGHT:
					self.RIGHT_KEY = False
				elif event.key == pygame.K_UP:
					self.UP_KEY = False
				elif event.key == pygame.K_DOWN:
					self.DOWN_KEY = False
				elif event.key == pygame.K_SPACE:
					self.SPACE_KEY = False


	def update(self):
		#print(self.clock.tick(60))
		self.player.update()
		self.camera.scroll()
		self.water_group.update(self.tick)
		self.grass_group.update(self.tick)
		self.enemy_group.update(self.tick)


	def draw(self):
		#self.screen.fill((0,200,240))	
		self.screen.fill((0,0,0))
		self.world.draw_world()
		self.water_group.draw()
		self.house_group.draw()
		self.grass_group.draw()
		self.enemy_group.draw()
		self.tree_group.draw()
		self.player.draw()
		
		#pygame.draw.rect(self.screen, (255, 0, 0), self.player.rect, 2)
		


	def mainloop(self):
		self.dt = self.clock.tick(60) * .001 * self.FPS 
		self.tick = self.clock.get_time()
		self.time += self.tick/1000
		self.daynight()
		self.input()

		if self.menu:
			self.mainmenu.draw()
			if self.mainmenu.buttons['Exit'][1]:
				self.running = False
			if self.mainmenu.buttons['Start'][1]:
				self.menu = False
			if self.mainmenu.buttons['Options'][1]:
				pass
		
		else :
			

			if self.game_state == 0:
				self.draw()
				self.update()
				#self.draw_hud()

			elif self.game_state == -1:
				#for combat
				pass

			elif self.game_state == 2:
				#dialoge
				#print("aaa")
				if self.dia:
					self.dialoge_box.show("Everything was going \nwell@ on the village , up till one day, whenit was attacked by the Skylers . Houses were set on fire, people were killed, crops were destroyed. They seeked the golden sword. It was believed to have contain the flames of the holy nine-tails#shit for centuries. It is said that only worthy villagers ")
					self.dia =False
				self.dialoge_box.update()
				
				

			elif self.game_state == 1:
				#for entering house and shit
				pass

			elif self.game_state == 5:
				#pause menu
				pass
		pygame.display.update()





if __name__=="__main__":
	engine = Engine()
	while engine.running :
		engine.mainloop()