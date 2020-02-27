# coding = utf-8
from tkinter import Button, Tk, Toplevel

import pygame
from AircraftLib import *


class PlaneGame(object):

    def __init__(self):
        # print("initialize")
        # 1.game interface
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2.game clock
        self.clock = pygame.time.Clock()
        # 3.create sprites
        self.__create_sprites()
        # 4.timer for enemies
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 300)
        # 5.timer for bullets
        pygame.time.set_timer(HERO_FIRE_EVENT, 300)

    def __create_sprites(self):
        # background sprite group
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # enemies sprite group
        self.enemy_group = pygame.sprite.Group()

        # hero sprite group
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("BEGIN")

        while True:
            # 1.Refresh frequency
            self.clock.tick(FRAME_PER_SEC)
            # 2.event handler
            self.__event_handler()
            # 3.collide
            self.__check_collide()
            # 4.sprite
            self.__update_sprites()
            # 5.update display
            pygame.display.update()
            pass

    def __event_handler(self):
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # print("enemy appear")
                # enemies sprites
                enemy = Enemy()

                # enemies sprites add to enemies sprites group
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        # Using the method provided by the keyboard to obtain keyboard keys -- key tuples
        keys_pressed = pygame.key.get_pressed()
        # Determine the key index value 1 in the tuple
        if keys_pressed[pygame.K_RIGHT]:
            # print("right")
            self.hero.speed = 5
        elif keys_pressed[pygame.K_LEFT]:
            # print("left")
            self.hero.speed = -5
        else:
            self.hero.speed = 0

    def __check_collide(self):
        # 1.bullet crash enemies
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        # 2.enemies crash hero
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        # 3.judge list has content
        if len(enemies) > 0:
            # hero lose
            self.hero.kill()
            # end game
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        # print("End")
        pygame.quit()
        exit()


if __name__ == '__main__':
    # game object
    game = PlaneGame()

    # start
    game.start_game()
