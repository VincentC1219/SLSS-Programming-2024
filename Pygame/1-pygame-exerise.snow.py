
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

class Snowflake(pg.sprite.Sprite):
    # create contructor
    #   image, rect
    def __init__(self, size: int):
        super().__init__()
        # Createing a 'blank" image

        self.image = pg.Surface((size, size))
        
        # Draw a circle on the "blank imahe"
        pg.draw.circle(self.image, WHITE, (size // 2, size // 2), size // 2)

        self.rect = self.image.get_rect()
        
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)
        self.vel_x = 0
        self.vel_y = 2

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if self.rect.bottom > HEIGHT:
            self.rect.y = 0



def start():
    """Environment Setup and Game Loop"""

    pg.init()

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    # All sprites go in this sprite Group

    all_sprites = pg.sprite.Group()

    # add one snowflake to the sprite Group
    for _ in range(100):
        all_sprites.add(Snowflake(10))

    pg.display.set_caption("screen")

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
    pg.quit()


def main():
    start()


if __name__ == "__main__":
    main()