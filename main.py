import pygame
from spritesheetparser import Spritesheet
from tiles import TileMap
from camera import *
from Player import *



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

		#self.main_tiles = Spritesheet('resources/Blockz')
		self.house_group = HomeGroup(self)
		self.world = TileMap('map.csv', self)
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
		
		#self.player.position.x, self.player.position.y = self.world.start_x, self.world.start_y
		self.dt = 0
		self.game_state = 0
		self.tick = 0
		self.tiles = self.world.tiles
		self.init_keys()


	def reset_level(self, level):
		pass

	
	def menu(self):
		pass

	
	def init_keys (self):
		self.LEFT_KEY, self.RIGHT_KEY = False, False
		self.UP_KEY, self.DOWN_KEY = False, False


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

	def update(self):
		self.dt = self.clock.tick(60) * .001 * self.FPS 
		#print(self.clock.tick(60))
		self.tick = self.clock.get_time()
		self.player.update()
		self.camera.scroll()

	def draw(self):
		#self.screen.fill((0,200,240))
		self.screen.fill((0,0,0))
		self.world.draw_world()
		
		self.house_group.draw()
		self.player.draw()
		
		pygame.draw.rect(self.screen, (255, 0, 0), self.player.rect, 2)
		pygame.display.update()







if __name__=="__main__":
	engine = Engine()
	while engine.running :
		engine.input()
		engine.update()
		engine.draw()	