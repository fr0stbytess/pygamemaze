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
        self.keys = 0
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        if not self.track_collisions(dx, dy):
            self.x += dx
            self.y += dy

    def update(self):
        self.rect.x = self.x * settings.tile_size
        self.rect.y = self.y * settings.tile_size
        if pg.sprite.spritecollide(self, self.game.key, True):
            self.game.key.remove()
        if self.keys == 2:
            if pg.sprite.spritecollide(self, self.game.door, True):
                self.game.door.remove()

    def track_collisions(self, dx=0, dy=0):
        """This method will track movements and detect collisions
           between Player and Walls classes"""
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        for water in self.game.water:
            if water.x == self.x + dx and water.y == self.y + dy:
                print("You died. Avoid water next time!")
                exit()
        for guardian in self.game.guardian:
            if guardian.x == self.x + dx and guardian.y == self.y + dy:
                print("You won!")
                exit()
        for key in self.game.key:
            if key.x == self.x + dx and key.y == self.y + dy:
                print("Key picked up")
                self.keys += 1
        for door in self.game.door:
            if door.x == self.x + dx and door.y == self.y + dy:
                if self.keys == 0:
                    return True
                elif self.keys == 2:
                    return False
                else:
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
        self.groups = game.all_sprites, game.water
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
        self.groups = game.all_sprites, game.guardian
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


class Key(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.key
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.x = x
        self.y = y
        self.key = pg.image.load("controller/images/key.png").convert_alpha()
        self.key = pg.transform.scale(self.key, (32, 32))
        self.image = pg.Surface.convert_alpha(self.key)
        self.rect = self.image.get_rect()
        self.rect.x = x * settings.tile_size
        self.rect.y = y * settings.tile_size


class Door(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.door
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.x = x
        self.y = y
        self.door = pg.image.load("controller/images/door.jpg").convert_alpha()
        self.door = pg.transform.scale(self.door, (32, 32))
        self.image = pg.Surface.convert_alpha(self.door)
        self.rect = self.image.get_rect()
        self.rect.x = x * settings.tile_size
        self.rect.y = y * settings.tile_size
