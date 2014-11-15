"""
This module is used to hold the lion class. The Player represents the user-
controlled sprite on the screen.
"""
import pygame
 
import constants
import levels
import player
 
class Lion(pygame.sprite.Sprite):
 
    # -- Attributes
    # Set speed vector of player
    change_x = 0
    change_y = 0
  
    
    boundary_left = 0
    boundary_right = 0
    # What direction is the lion facing?
    direction = "" 
 
    MAX_HEALTH = 1
    health = 1
    walk_right = ""  
    walk_left = ""    

    # List of sprites we can bump against
    level = None
    p1 = None

    def __init__(self):
        """ Constructor function """
        self.MAX_HEALTH = 400
        self.health = self.MAX_HEALTH
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
 
        image = pygame.image.load("lion.png").convert()
        self.walk_right = image
        self.walk_right.set_colorkey(constants.WHITE)  
        self.walk_left = self.walk_right
        self.walk_left.set_colorkey(constants.WHITE)     
        self.walk_right = pygame.transform.flip(image, True, False)
 
        self.rawr = pygame.mixer.Sound("rawr.wav")
        # Set the image the player starts with
        self.image = image
 
        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Move the lion. """
        # Move left/right
        self.rect.x += self.change_x  
        
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
            self.change_dir()
            
            
        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.p1)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.
 
            # If we are moving right, set our right side
            # to the left side of the item we hit
            self.rect.x -= self.change_x
            self.attack_player()
            
        # Check the boundaries and see if we need to reverse
        # direction.
 
        cur_pos = self.rect.x - self.level.world_shift
        if (cur_pos < self.boundary_left and self.change_x < 0) or (cur_pos > self.boundary_right and self.change_x > 0):
            self.change_dir()
        
        # update image
        if (self.direction == "R"):
            self.image = self.walk_right
        else:
            self.image = self.walk_left
        if self.health < 1:
            self.level.enemy_list.remove(self)
            del self        
                        
    def change_dir(self): 
        self.change_x *= -1
        if (self.direction == "R"):
            self.direction = "L"
        else:
            self.direction = "R"  
            
    def attack_player(self):
        self.p1.hp -= self.p1.dif_multiplier * .25
        self.rawr.play()
    def draw_health(self,screen):
        if (self.health > 0):
            pygame.draw.rect(screen, constants.RED, [self.rect.x, self.rect.y -2,self.health * (self.rect.right-self.rect.x)/ self.MAX_HEALTH, 2]) 
class BigLion(Lion):
        def __init__(self):
            # Call the parent's constructor
            boundary_bottom = None
            boundary_top = None
            pygame.sprite.Sprite.__init__(self)
            image = pygame.image.load("lion_aslan.png").convert()
            self.walk_right = image
            self.walk_right.set_colorkey(constants.WHITE)  
            self.walk_left = self.walk_right
            self.walk_left.set_colorkey(constants.WHITE)     
            self.walk_right = pygame.transform.flip(image, True, False)
            self.rawr = pygame.mixer.Sound("rawr.wav")
            self.image = image
            self.rect = self.image.get_rect()
            self.MAX_HEALTH = 4000
            self.health = self.MAX_HEALTH
        def attack_player(self):
            self.p1.hp -= self.p1.dif_multiplier * .6
            self.rawr.play()  
        def update(self):
            # Move left/right
            self.rect.x += self.change_x
     
            # See if we hit the player
            hit = pygame.sprite.collide_rect(self, self.p1)
            if hit:
                # We did hit the player. Shove the p1 around and
                # assume he/she won't hit anything else.
     
                # If we are moving right, set our right side
                # to the left side of the item we hit
                self.attack_player()
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
                # We did hit the p1. Shove the player around and
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
                self.change_dir()         
    # update image
            if (self.direction == "R"):
                self.image = self.walk_right
            else:
                self.image = self.walk_left
            if self.health < 1:
                self.p1.level_2_win = True
                self.level.enemy_list.remove(self)
                del self                    
