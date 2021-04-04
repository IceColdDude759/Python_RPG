import pygame, csv, os
from objects import *

class Tile(pygame.sprite.Sprite):
	def __init__(self, image, x, y,can_collide):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image+".png")
		#self.image = pygame.transform.scale(img, (50, 80))
		#self.image = spritesheet.get_sprite(image), spritesheet
		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y = x, y
		self.can_collide = can_collide

	def draw(self, surface):
		surface.blit(self.image, (self.rect.x, self.rect.y))

class TileMap():
	def __init__(self, filename, engine):
		self.engine = engine
		self.tile_size = self.engine.tile_size
		self.start_x, self.start_y = 0, 0
		#self.spritesheet = spritesheet
		self.tiles = self.load_tiles(filename)
		self.map_surface = pygame.Surface((self.map_w, self.map_h))
		self.map_surface.set_colorkey((0, 0, 0))
		self.load_map()
		self.tiles=[elem for elem in self.tiles if elem.can_collide]
	

	def draw_world(self):
		self.engine.screen.blit(self.map_surface, (0 - self.engine.camera.offset.x, 0 - self.engine.camera.offset.y))

	def load_map(self):
		for tile in self.tiles:
			tile.draw(self.map_surface)

	def read_csv(self, filename):
		map = []
		with open(os.path.join(filename)) as data:
			data = csv.reader(data, delimiter=',')
			for row in data:
				map.append(list(row))
		return map

	def load_tiles(self, filename):
		tiles = []
		map = self.read_csv(filename)
		x, y = 0, 0
		for row in map:
			x = 0
			for tile in row:
				#grass
				if tile == '0':
					tiles.append(Tile('img/rpgTile000', x * self.tile_size, y * self.tile_size, False))
				elif tile == '1':
					tiles.append(Tile('img/rpgTile001', x * self.tile_size, y * self.tile_size, False))
				elif tile == '2':
					tiles.append(Tile('img/rpgTile002', x * self.tile_size, y * self.tile_size, False))
				elif tile == '9':
					tiles.append(Tile('img/rpgTile018', x * self.tile_size, y * self.tile_size, False))
				elif tile == '10':
					tiles.append(Tile('img/rpgTile019', x * self.tile_size, y * self.tile_size, False))
				elif tile == '11':
					tiles.append(Tile('img/rpgTile020', x * self.tile_size, y * self.tile_size, False))
				elif tile == '18':
					tiles.append(Tile('img/rpgTile036', x * self.tile_size, y * self.tile_size, False))
				elif tile == '19':
					tiles.append(Tile('img/rpgTile037', x * self.tile_size, y * self.tile_size, False))
				elif tile == '20':
					tiles.append(Tile('img/rpgTile038', x * self.tile_size, y * self.tile_size, False))

				#water
				elif tile == '6':
					tiles.append(Tile('img/rpgTile010', x * self.tile_size, y * self.tile_size, True))
				elif tile == '7':
					tiles.append(Tile('img/rpgTile011', x * self.tile_size, y * self.tile_size, True))
				elif tile == '8':
					tiles.append(Tile('img/rpgTile012', x * self.tile_size, y * self.tile_size, True))
				elif tile == '15':
					tiles.append(Tile('img/rpgTile028', x * self.tile_size, y * self.tile_size, True))
				elif tile == '16':
					self.engine.water_group.add(Water(x * self.tile_size, y * self.tile_size, self.tile_size))
					tiles.append(Tile('img/rpgTile029', x * self.tile_size, y * self.tile_size, True))
				elif tile == '17':
					tiles.append(Tile('img/rpgTile030', x * self.tile_size, y * self.tile_size, True))
				elif tile == '24':
					tiles.append(Tile('img/rpgTile044', x * self.tile_size, y * self.tile_size, True))
				elif tile == '25':
					tiles.append(Tile('img/rpgTile045', x * self.tile_size, y * self.tile_size, True))
				elif tile == '26':
					tiles.append(Tile('img/rpgTile046', x * self.tile_size, y * self.tile_size, True))

				#dirt
				elif tile == '3':
					tiles.append(Tile('img/rpgTile005', x * self.tile_size, y * self.tile_size, False))
				elif tile == '4':
					tiles.append(Tile('img/rpgTile006', x * self.tile_size, y * self.tile_size, False))
				elif tile == '5':
					tiles.append(Tile('img/rpgTile007', x * self.tile_size, y * self.tile_size, False))
				elif tile == '12':
					tiles.append(Tile('img/rpgTile023', x * self.tile_size, y * self.tile_size, False))
				elif tile == '13':
					tiles.append(Tile('img/rpgTile024', x * self.tile_size, y * self.tile_size, False))
				elif tile == '14':
					tiles.append(Tile('img/rpgTile025', x * self.tile_size, y * self.tile_size, False))
				elif tile == '21':
					tiles.append(Tile('img/rpgTile041', x * self.tile_size, y * self.tile_size, False))
				elif tile == '22':
					tiles.append(Tile('img/rpgTile042', x * self.tile_size, y * self.tile_size, False))
				elif tile == '23':
					tiles.append(Tile('img/rpgTile043', x * self.tile_size, y * self.tile_size, False))
				
				#tree
				elif tile == '27':
					tiles.append(Tile('img/grass', x * self.tile_size, y * self.tile_size, True))
					tiles.append(Tile('img/rpgTile177', x * self.tile_size, y * self.tile_size, True))
				elif tile == '28':
					tiles.append(Tile('img/grass', x * self.tile_size, y * self.tile_size, True))
					tiles.append(Tile('img/rpgTile179', x * self.tile_size, y * self.tile_size, True))
					#tiles.append(Tile('img/rpgTile157', x * self.tile_size, y * self.tile_size, True))

				elif tile == '29':
					tiles.append(Tile('img/grass', x * self.tile_size, y * self.tile_size, True))
					tiles.append(Tile('img/rpgTile197', x * self.tile_size, y * self.tile_size, True))
				elif tile == '30':

					tiles.append(Tile('img/rpgTile199', x * self.tile_size, y * self.tile_size, True))

				#house
				elif tile == '31':
					tiles.append(Tile('img/rpgTile200', x * self.tile_size, y * self.tile_size, True))
				elif tile == '32':
					tiles.append(Tile('img/rpgTile201', x * self.tile_size, y * self.tile_size, True))
				elif tile == '33':
					tiles.append(Tile('img/grass', x * self.tile_size, y * self.tile_size, False))
					self.engine.house_group.add(House( x * self.tile_size, y * self.tile_size, self.tile_size, 'small'))
					#tiles.append(Tile('img/rpgTile202', x * self.tile_size, y * self.tile_size, True))
				
				#nps
				elif tile == '34':
					tiles.append(Tile('img/rpgTile203', x * self.tile_size, y * self.tile_size, True))
				elif tile == '35':
					tiles.append(Tile('img/rpgTile204', x * self.tile_size, y * self.tile_size, True))
				elif tile == '36':
					tiles.append(Tile('img/rpgTile205', x * self.tile_size, y * self.tile_size, True))
				
				#objects
				elif tile == '37':
					tiles.append(Tile('img/rpgTile206', x * self.tile_size, y * self.tile_size, True))
				elif tile == '38':
					tiles.append(Tile('img/rpgTile207', x * self.tile_size, y * self.tile_size, True))
				elif tile == '39':
					tiles.append(Tile('img/rpgTile208', x * self.tile_size, y * self.tile_size, True))
				elif tile == '40':
					tiles.append(Tile('img/rpgTile209', x * self.tile_size, y * self.tile_size, True))
				elif tile == '41':
					tiles.append(Tile('img/rpgTile210', x * self.tile_size, y * self.tile_size, True))
				elif tile == '42':
					tiles.append(Tile('img/rpgTile211', x * self.tile_size, y * self.tile_size, True))
				
				#teleport
				elif tile == '43':
					tiles.append(Tile('img/grass', x * self.tile_size, y * self.tile_size, False))
					self.engine.teleport_group.add(Teleport(x * self.tile_size, y * self.tile_size, self.tile_size))

				#grass
				elif tile == '44':
					tiles.append(Tile('img/grass', x * self.tile_size, y * self.tile_size, False))
					self.engine.grass_group.add(Grass(x * self.tile_size, y * self.tile_size, self.tile_size))

				#tree
				elif tile == '45':
					tiles.append(Tile('img/grass', x * self.tile_size, y * self.tile_size, False))
				
				#deadtree
				elif tile == '46':
					tiles.append(Tile('img/grass', x * self.tile_size, y * self.tile_size, False))
				
				#flower
				elif tile == '47':
					tiles.append(Tile('img/grass', x * self.tile_size, y * self.tile_size, False))
				
				#fire
				elif tile == '48':
					tiles.append(Tile('img/grass', x * self.tile_size, y * self.tile_size, False))
				
					# Move to next tile in current row
				x += 1

			# Move to next row
			y += 1
			# Store the size of the tile map
		self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
		return tiles





