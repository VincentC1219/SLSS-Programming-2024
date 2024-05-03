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

        self.image("./Images/coin.png")
        self.rect = self.image.get_rect()

        # Random initial position
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)
    

def start():
    """Environment Setup and Game Loop"""

    pg.init()

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()

    pg.display.set_caption("screen")

    # Create a player and store it in a variable

    player = Player()

    all_sprites.add(player)

    pg.display.set_caption("Jewel Thief Clone (Don't sue us Nintendo)")

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # --- Update the world state

        all_sprites.update()

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