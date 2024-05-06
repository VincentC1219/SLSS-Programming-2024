import random
import pygame as pg


        
# --CONSTANTS--
# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

WIDTH = 1280  # Pixels
HEIGHT = 720
SCREEN_SIZE = (WIDTH, HEIGHT)

NUM_COIN = 10

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image= pg.image.load("./Images/mario.png")
        self.rect = self.image.get_rect()

    def update(self):
        """Updates the loction of sprite to mouse cursor"""
        self.rect.centerx = pg.mouse.get_pos()[0]
        self.rect.centery = pg.mouse.get_pos()[1]

class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./Images/coin.png")
        self.rect = self.image.get_rect()

        # Random initial position
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./Images/green-shell.png")
        self.rect = self.image.get_rect()

        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)

        self.vel_x = 2
        self.vel_y = 2
    
    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if self.rect.bottom > HEIGHT:
            self.vel_y *= -1

        # Top
        if self.rect.top < 0:
            self.vel_y *= -1

        # Left
        if self.rect.right > WIDTH:
            self.vel_x *= -1

        # Right
        if self.rect.left < 0:
            self.vel_x *= -1
    

def start():
    """Environment Setup and Game Loop"""

    pg.init()
    pg.mouse.set_visible(False)

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    score = 0

    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()

    # Coin sprites
    coin_sprites = pg.sprite.Group()

    for _ in range (NUM_COIN):
        coin = Coin()

        all_sprites.add(coin)
        coin_sprites.add(coin)

    pg.display.set_caption("screen")

    # Create a player and store it in a variable

    player = Player()

    all_sprites.add(player)

    enemy = Enemy()

    all_sprites.add(enemy) 

    pg.display.set_caption("Jewel Thief Clone (Don't sue us Nintendo)")

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # --- Update the world state
        all_sprites.update()

        # Collisi between player and coin_sprite
        # Get a list of ALL coin_sprites that collide
        #   with the player
        # For every coin that collides, print "COLLISION"
        coins_collided = pg.sprite.spritecollide(player, coin_sprites, True)

        for coin in coins_collided:
            # increase score by 1
            score += 1

            print(score)

        # if the coin_sprites group is empty
        # respawn all the coins
        if len(coin_sprites) <= 0:
            for _ in range(NUM_COIN):
                coin = Coin()
                all_sprites.add(coin)
                coin_sprites.add(coin)

        enemy_collided = pg.sprite.spritecollide(player, enemy, False)

        for enemy in enemy_collided:
            # decrease score by 1
            score -= 1

            print(score)


        # --- Draw items
        screen.fill(WHITE)

        all_sprites.draw(screen)

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()