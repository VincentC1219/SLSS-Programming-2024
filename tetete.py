import pygame as pg
import random
# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 1280
HEIGHT = 720
TITLE = "Snowing"
NUM_SNOW = 100
class Snow(pg.sprite.Sprite):
    def __init__(self, width: int):
        super().__init__()
        self.image = pg.Surface((width, width))
        # Found by Duncan, he says Yippee!
        pg.draw.circle(self.image, SKY_BLUE, (width // 2, width // 2), width // 2)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = 0
        self.vel_x = 0
        self.vel_y = random.choice([1, 2])
    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        if self.rect.bottom > HEIGHT:
            self.rect.y = 0
def main():
    pg.init()
    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pg.display.set_mode(size)
    pg.display.set_caption(TITLE)
    # ----- LOCAL VARIABLES
    done = False
    clock = pg.time.Clock()
    # Create a snow sprites group
    snow_sprites = pg.sprite.Group()
    # Create more snow
    for _ in range(50):
        snow_sprites.add(Snow(10))
    # ----- MAIN LOOP
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
        snow_sprites.update()
        screen.fill(BLACK)
        snow_sprites.draw(screen)
        # ----- UPDATE DISPLAY
        pg.display.flip()
        clock.tick(60)
    pg.quit()
if __name__ == "__main__":
    main()