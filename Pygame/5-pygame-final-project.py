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

class Cursor(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = self.image = pg.Surface((10,10))
        self.image.fill(WHITE)


        self.rect = self.image.get_rect()

    def update(self):
        """Updates the loction of sprite to mouse cursor"""

        next_pos = pg.mouse.get_pos()

        self.rect.center = next_pos

        # See if we hit anything
        Game_over = pg.sprite.spritecollide(self, self.level.platform_list, False)
        for block in Game_over:
            pg.quit()

class Platform(pg.sprite.Sprite):
    """ Platform the user can jump on """
 
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super().__init__()
 
        self.image = pg.Surface([width, height])
        self.image.fill(BLUE)
 
        self.rect = self.image.get_rect()

# class End(pg.sprite.Sprite):
#     """ Platform the user can jump on """
 
#     def __init__(self, width, height):
#         """ Platform constructor. Assumes constructed with user passing in
#             an array of 5 numbers like what's defined at the top of this
#             code. """
#         super().__init__()
 
#         self.image = pg.Surface([width, height])
#         self.image.fill(GREEN)
 
#         self.rect = self.image.get_rect()
 
 
class Level(object):
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """
 
    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pg.sprite.Group()
        self.enemy_list = pg.sprite.Group()
        self.player = player
         
        # Background image
        self.background = None
 
    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()
 
    def draw(self, screen):
        """ Draw everything on this level. """
 
        # Draw the background
        screen.fill(BLACK)
 
        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
 
 
# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        # Array with width, height, x, and y of platform
        level = [
            [WIDTH - 250, 275, 100, 75],
                 [WIDTH - 100, 25, 100, 0],
                 [100, HEIGHT, 0, 100],
                 [WIDTH - 1180, HEIGHT, 1180, 0],
                 [WIDTH, HEIGHT - 400, 1035, 400],
                 [WIDTH - 985, HEIGHT - 450, 700, 350],
                 [WIDTH, 100, 0, HEIGHT - 50],
                 [100, HEIGHT - 395, 600, 300],
                 [700, 55, 0, HEIGHT - 55],
                 [565, 300, 0, 500],
                 [400, 30, 200, 350],
                 [365, 100, 200, 410],
                 [100, 100, 100, 450]]
    
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)



def start():
    """Environment Setup and Game Loop"""

    pg.init()
    pg.mouse.set_visible(False)

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()

    cursor = Cursor()

    all_sprites.add(cursor)

    # Create all the levels
    level_list = []
    level_list.append( Level_01(cursor) )
 
    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
 
    active_sprite_list = pg.sprite.Group()

    cursor.level = current_level

    active_sprite_list.add(cursor)    

    pg.display.set_caption("Maze")

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # --- Update the world state
        
        # Update the player.
        active_sprite_list.update()
 
        # Update items in the level
        current_level.update()

        all_sprites.update()

        # --- Draw items
        screen.fill(BLACK)

        all_sprites.draw(screen)
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()