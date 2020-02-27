# coding = utf-8

import random
import pygame

# screen
SCREEN_RECT = pygame.Rect(0, 0, 520, 700)
# refresh
FRAME_PER_SEC = 60
# Create timer constant for enemy aircraft
CREATE_ENEMY_EVENT = pygame.USEREVENT
# Hero shot
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_name, speed=1):

        super().__init__()

        # object attributes
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # Move in the vertical direction of the screen
        self.rect.y += self.speed


class Background(GameSprite):

    def __init__(self, is_alt=False):
        # 1.Calling parent method to create Sprite（image/rect/speed）
        super().__init__("./reindeerMap2.png")

        # 2.Determine whether to alternate images, if so, set the initial position
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 1.Method implementation of calling parent class
        super().update()

        # 2.Determine whether the screen moves out of the screen. If you move out of the screen, set the image to the top of the screen
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):

    def __init__(self):
        # 1.Call the parent method, create the enemy spirit, and specify the enemy image at the same time
        super().__init__("./tree.png")
        # 2.Initial random speed of designated enemy aircraft 2-4
        self.speed = random.randint(2, 3)
        # 3.Specify the initial random position of the enemy aircraft
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)
        pass

    def update(self):
        # 1.Call the parent method to keep the vertical flight
        super().update()
        # 2.Determine whether to fly out of the screen. If so, you need to delete the enemy aircraft from the sprite group
        if self.rect.y >= SCREEN_RECT.height:
            # print("Fly out of screen, need to remove from sprite group……")
            # The kill method can remove the sprite from all sprite groups, and the sprite will be destroyed automatically
            self.kill()

    def __del__(self):
        # print("Enemy killed  %s"%self.rect)

        pass


class Hero(GameSprite):

    def __init__(self):
        # 1.Call the parent method to set image &amp; speed
        super().__init__("./car.png", 0)
        # 2.Set the hero's initial position
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 50
        # 3.Create the sprite group of bullets
        self.bullets = pygame.sprite.Group()

    def update(self):
        # Hero moves horizontally
        self.rect.x += self.speed
        # Control hero can't leave the screen
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        # print("shoot")

        # 1.Create bullet Genie
        bullet = Bullet()
        # 2.Set sprite location
        bullet.rect.bottom = self.rect.y
        bullet.rect.centerx = self.rect.centerx
        # 3.Add sprites to sprite group
        self.bullets.add(bullet)


class Bullet(GameSprite):

    def __init__(self):
        # Call the parent method, set the bullet image, and set the initial speed
        super().__init__("./gift.png", -2)

    def update(self):
        # Call the parent method to let the bullet fly in the vertical direction
        super().update()
        # Determine if the bullet flies out of the screen
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        pass


