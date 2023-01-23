"""This is the core module of the application which will
   handle all the client processing"""

import sys

import pygame as pg

from controller import preload
from controller import settings
from controller import sprites


class Client:
    """This is the game client class which manages all the
       core processing"""

    def __init__(self):
        self.init_pygame()
        self.screen = pg.display.set_mode((settings.width, settings.height))
        pg.display.set_caption(settings.app_title)
        self.fps = settings.fps
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 80)
        self.load_data()

    def init_pygame(self):
        """This method will initialize pygame"""
        pg.init()

    def load_data(self):
        """This method loads all the external data to the game Client"""
        self.map_data = []
        with open("controller/map.txt", "rt") as f:
            for line in f:
                self.map_data.append(line)

    def new_game(self):
        """This method will initialize all the variables and
           start a new game"""
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.water = pg.sprite.Group()
        # self.grass = pg.sprite.Group()
        self.key = pg.sprite.Group()
        self.door = pg.sprite.Group()
        self.guardian = pg.sprite.Group()
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == "1":
                    sprites.Wall(self, col, row)
                if tile == "X":
                    self.player = sprites.Player(self, col, row)
                #if tile == "G":
                    #sprites.Grass(self, col, row)
                if tile == "W":
                    sprites.Water(self, col, row)
                if tile == "F":
                    sprites.Guardian(self, col, row)
                if tile == "K":
                    sprites.Key(self, col, row)
                if tile == "D":
                    sprites.Door(self, col, row)

    def run_client(self):
        """As the method name says itself, it will run the game client"""
        self.running = True
        while self.running:
            self.delta = self.clock.tick(self.fps) / 1000
            self.events()
            self.update()
            self.draw()

    def log_actions(self):
        """To be reworked"""
        self.logs = None

    def quit_client(self):
        """Clearly quits the game client, self-descriptive"""
        pg.quit()
        sys.exit()

    def update(self):
        """This method will update the game sprites"""
        self.all_sprites.update()

    def draw_grid(self):
        """Self-descriptive. Draws the grids on the map"""
        for x in range(0, settings.width, settings.tile_size):
            pg.draw.line(self.screen, settings.ground_color,
                         (x, 0), (x, settings.height))
        for y in range(0, settings.height, settings.tile_size):
            pg.draw.line(self.screen, settings.ground_color,
                         (0, y), (settings.width, y))

    def draw(self):
        temp_background_image = pg.image.load("controller/images/background.jpg")
        self.screen.blit(temp_background_image, temp_background_image.get_rect())
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        """This method will catch all the events and perform
           specific actions"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.log_actions()
                self.quit_client()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit_client()
                if event.key == pg.K_SPACE:
                    self.quit_client()
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=+1)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy=+1)


if __name__ == '__main__':
    client = Client()
    preload = preload.Preload()
    while True:
        client.new_game()
        client.run_client()
