"""This module does contain Player and Walls
   sprites that will be used in game client"""

import pygame as pg

from controller import settings


class Player(pg.sprite.Sprite):
    """This class manages the Player class and its movements"""

    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.character = pg.image.load(
            "controller/images/macgyver.png").convert_alpha()
        self.character = pg.transform.scale(self.character, (32, 32))
        self.image = pg.Surface.convert_alpha(self.character)
        self.rect = self.character.get_rect()
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        if not self.track_collisions(dx, dy):
            self.x += dx
            self.y += dy

    def update(self):
        self.rect.x = self.x * settings.tile_size
        self.rect.y = self.y * settings.tile_size

    def track_collisions(self, dx=0, dy=0):
        """This method will track movements and detect collisions
           between Player and Walls classes"""
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False


class Wall(pg.sprite.Sprite):
    """This class manages the Walls class and collisions"""

    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.wall = pg.image.load("controller/images/wall.jpg").convert_alpha()
        self.wall = pg.transform.scale(self.wall, (32, 32))
        self.image = pg.Surface.convert_alpha(self.wall)
        #  self.image.fill(self.image)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * settings.tile_size
        self.rect.y = y * settings.tile_size


class Water(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.water = pg.image.load(
            "controller/images/water.png").convert_alpha()
        self.water = pg.transform.scale(self.water, (32, 32))
        self.image = pg.Surface.convert_alpha(self.water)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * settings.tile_size
        self.rect.y = y * settings.tile_size


class Guardian(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.guardian = pg.image.load(
            "controller/images/guardian.png").convert_alpha()
        self.guardian = pg.transform.scale(self.guardian, (32, 32))
        self.image = pg.Surface.convert_alpha(self.guardian)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * settings.tile_size
        self.rect.y = y * settings.tile_size
