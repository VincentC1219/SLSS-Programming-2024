# Shoot 'em up

import pygame as pg
import random

# --CONSTANTS--
# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

WIDTH = 720  # Pixels
HEIGHT = 1000
SCREEN_SIZE = (WIDTH, HEIGHT)

NUM_ENEMIES = 6

# TODO: player class
#       - Mouse movement
#       - Limit player position to the bottom
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./Images/galaga_ship_360.png")

        self.rect = self.image.get_rect()

    def update(self):
        """Follow mouse"""

        self.rect.center = pg.mouse.get_pos()

        # Keep at bottom of screen
        if self.rect.top < HEIGHT - 200:
            self.rect.top = HEIGHT - 200


# TODO: Bullets/ lasers
#       - Image - picture or pygame surface
#       - Spawn at the player
#       - Vertical velocity

class Bullet(pg.sprite.Sprite):
    def __init__(self, player_loc: list):
        """Params:
            player_loc: x, y coords of centerx and top"""
        super().__init__()

        self.image = pg.Surface((10,25))
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()

        # Spawn at player
        self.rect.centerx = player_loc[0]
        self.rect.bottom = player_loc[1]

        self.vel_y = -20

    def update(self):
        self.rect.y += self.vel_y

# TODO: Enemies
#       - Move left to right to left
class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()


        # # Load image
        # ENEMY_IMG = pg.image.load("./Images/green-shell.png")

        # # Scale the image

        # self.image = pg.transform.scale(
        #     ENEMY_IMG,
        #     (ENEMY_IMG.get_width() // 2.5, ENEMY_IMG.get_height() //2.5)
        # )
        ENEMY_IMG = pg.image.load("./Images/galaga-enemy.webp")

        self.image = pg.transform.scale(
            ENEMY_IMG,
            (ENEMY_IMG.get_width() //10, ENEMY_IMG.get_height() // 10)
        )
        self.rect = self.image.get_rect()

        self.vel_y = 5
        self.vel_x = 2

        self.rect.x = random.randrange(0, WIDTH - self.rect.width)

        # self.rect.x = random.randrange(0, WIDTH - self.rect.width)

    def update(self):
        self.rect.y += self.vel_y
        self.rect.x += self.vel_x

        if self.rect.right > WIDTH:
            self.vel_x *= -1

        if self.rect.left < 0:
            self.vel_x *= -1


def start():
    """Environment Setup and Game Loop"""

    pg.init()

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()
    bullet_sprite = pg.sprite.Group()
    enemy_sprites = pg.sprite.Group()

    # Craete player sprite
    player = Player()

    all_sprites.add(player)

    for _ in range(NUM_ENEMIES):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemy_sprites.add(enemy)


    pg.display.set_caption("<Shoot 'em up>")

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                bullet = (Bullet((player.rect.centerx, player.rect.top)))
                all_sprites.add(bullet)
                bullet_sprite.add(bullet)

            if event.type == pg.KEYDOWN:
                if pg.key.get_pressed()[pg.K_SPACE]:
                    bullet = (Bullet((player.rect.centerx, player.rect.top)))
                    all_sprites.add(bullet)
                    bullet_sprite.add(bullet)

        # --- Update the world state

        all_sprites.update()
        
        enemies_collided = pg.sprite.groupcollide(enemy_sprites, bullet_sprite, True, True)
        for enemy in enemies_collided:
            enemy = Enemy()
            all_sprites.add(enemy)
            enemy_sprites.add(enemy)

        player_collided = pg.sprite.spritecollide(player, enemy_sprites, True)
        for enemy in player_collided:
            pg.quit()


        # coins_collided = pg.sprite.spritecollide(player, coin_sprites, True)
        # --- Draw items
        screen.fill(BLACK)

        all_sprites.draw(screen)

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()