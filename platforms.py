"""
Module for managing platforms.
"""
import pygame
import constants 
import spritesheet_functions
 
# These constants define our platform types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite
 
WOOD_SMALL            = (0, 0, 50, 50)
WOOD_MEDIUM           = (0, 0, 100, 100)
WOOD_TALL             = (0, 0, 50, 150)
WOOD_LONG             = (0, 0, 150, 50)
STONE_SMALL            = (250, 0, 50, 50)
STONE_MEDIUM           = (250, 0, 100, 100)
STONE_TALL             = (250, 0, 50, 150)
STONE_LONG             = (250, 0, 150, 50)

class Gate(pygame.sprite.Sprite):
    identity = "gate"
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("gate.png").convert()
        self.rect = self.image.get_rect()
class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """
    identity = "platform"
    def __init__(self, sprite_sheet_data):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        pygame.sprite.Sprite.__init__(self)
 
        sprite_sheet = spritesheet_functions.SpriteSheet("tile_sheet.png")
        # Grab the image for this platform
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
 
        self.rect = self.image.get_rect()
 
class MovingPlatform(Platform):
    """ This is a fancier platform that can actually move. """
    change_x = 0
    change_y = 0
 
    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0
 
    level = None
    p1 = None
    identity = "movingPlatform"
    def update(self):
        """ Move the platform.
            If the player is in the way, it will shove the player
            out of the way. This does NOT handle what happens if a
            platform shoves a player into another object. Make sure
            moving platforms have clearance to push the player around
            or add code to handle what happens if they don't. """
 
        # Move left/right
        self.rect.x += self.change_x
 
        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.p1)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.
 
            # If we are moving right, set our right side
            # to the left side of the item we hit
            if self.change_x < 0:
                self.p1.rect.right = self.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.p1.rect.left = self.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we the player
        hit = pygame.sprite.collide_rect(self, self.p1)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y < 0:
                self.p1.rect.bottom = self.rect.top
            else:
                self.p1.rect.top = self.rect.bottom
 
        # Check the boundaries and see if we need to reverse
        # direction.
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1
 
        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
class Button(pygame.sprite.Sprite):
    """ Platform the user can jump on """
    image = None
    button_type = ""
    def __init__(self, button_image, y, x):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        pygame.sprite.Sprite.__init__(self)
        self.image = button_image
        self.image.set_colorkey(constants.WHITE)
        # Grab the image for this platform
 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y =y        
#class Start_Button(Button):
  #  def action(self):
       # pygame.mixer.music.play() 

