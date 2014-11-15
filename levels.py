import pygame
 
import constants
import platforms
import enemy
import player
 
class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """
 
    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game. """
    platform_list = None
    enemy_list = None
    player_x = 320
    player_y = constants.SCREEN_HEIGHT - 150
    # Background image
    background = None
    p1 = None
    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit_right = -1000
 	
    def __init__(self, p1):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.p1 = p1
 
    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update() 
        self.enemy_list.update()
 
    def draw(self, screen):
        """ Draw everything on this level. """
 
        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.BLUE)
        screen.blit(self.background,(self.world_shift // 40,0))
 
        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.draw_player_health(screen)
        for enemy in self.enemy_list:
            enemy.draw_health(screen)
    def draw_menu(self, screen):
        """ Draw everything on this level. """
 
        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.BLUE)
        screen.blit(self.background,(self.world_shift // 12,0))
        self.platform_list.draw(screen)
        # Draw all the sprite lists that we have
    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """
 
        # Keep track of the shift amount
        self.world_shift += shift_x
 
        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x
 
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
    def draw_player_health(self,screen):
        if (self.p1.hp > 0):
            pygame.draw.rect(screen, constants.GREEN, [50, 50, self.p1.hp/10, 20])
class Start_Menu(Level):
    def __init__(self, p1):
        Level.__init__(self, p1)
        self.background = pygame.image.load("Start_Menu.png").convert()
        self.background.set_colorkey(constants.WHITE)

        start_button = pygame.image.load("Start_Button.png").convert()
        button1 = platforms.Button(start_button, 150, 500)   
        button1.p1 = self.p1
        button1.level = self
        button1.button_type = "start"
        self.platform_list.add(button1)
        
        option_button = pygame.image.load("Option_Button.png").convert()
        button1 = platforms.Button(option_button, 200, 500)   
        button1.p1 = self.p1
        button1.level = self
        button1.button_type = "options"
        self.platform_list.add(button1)    
        
        quit_button = pygame.image.load("Quit_Button.png").convert()
        button1 = platforms.Button(quit_button, 250, 500)   
        button1.p1 = self.p1
        button1.level = self
        button1.button_type = "quit"
        self.platform_list.add(button1)         
class Options_Menu(Level):
    def __init__(self, p1):
        Level.__init__(self, p1)
        self.background = pygame.image.load("Start_Menu.png").convert()
        self.background.set_colorkey(constants.WHITE)

        back_button = pygame.image.load("Back_Button.png").convert()
        button1 = platforms.Button(back_button, 150, 495)   
        button1.p1 = self.p1
        button1.level = self
        button1.button_type = "back"
        self.platform_list.add(button1)  
        
        quit_button = pygame.image.load("Quit_Button.png").convert()
        button1 = platforms.Button(quit_button, 400, 500)   
        button1.p1 = self.p1
        button1.level = self
        button1.button_type = "quit"
        self.platform_list.add(button1)   
        
        help_button = pygame.image.load("Help_Button.png").convert()
        button1 = platforms.Button(help_button, 200, 505)   
        button1.p1 = self.p1
        button1.level = self
        button1.button_type = "help"
        self.platform_list.add(button1) 
        
        music_plus_button = pygame.image.load("Plus_Button.png").convert()
        button1 = platforms.Button(music_plus_button, 250, 680)   
        button1.p1 = self.p1
        button1.level = self
        button1.button_type = "music_plus"
        self.platform_list.add(button1) 
        
        music_minus_button = pygame.image.load("Minus_Button.png").convert()
        button1 = platforms.Button(music_minus_button, 250, 470)   
        button1.p1 = self.p1
        button1.level = self
        button1.button_type = "music_minus"
        self.platform_list.add(button1)  
        
        music_button = pygame.image.load("Music_Button.png").convert()
        button1 = platforms.Button(music_button, 250, 500)   
        button1.p1 = self.p1
        button1.level = self
        self.platform_list.add(button1)    

        difficulty_plus_button = pygame.image.load("Plus_Button.png").convert()
        button1 = platforms.Button(difficulty_plus_button, 330, 750)   
        button1.p1 = self.p1
        button1.level = self
        button1.button_type = "difficulty_plus"
        self.platform_list.add(button1) 
        
        difficulty_minus_button = pygame.image.load("Minus_Button.png").convert()
        button1 = platforms.Button(difficulty_minus_button, 330, 470)   
        button1.p1 = self.p1
        button1.level = self
        button1.button_type = "difficulty_minus"
        self.platform_list.add(button1)  
        
        difficulty_button = pygame.image.load("Difficulty_Button.png").convert()
        button1 = platforms.Button(difficulty_button, 330, 495)   
        button1.p1 = self.p1
        button1.level = self
        self.platform_list.add(button1) 
               
class Help_Menu(Level):
    def __init__(self, p1):
        Level.__init__(self, p1)
        self.background = pygame.image.load("Start_Menu.png").convert()
        self.background.set_colorkey(constants.WHITE)

        back_button = pygame.image.load("Back_Button.png").convert()
        button1 = platforms.Button(back_button, 150, 500)   
        button1.p1 = self.p1
        button1.level = self
        button1.button_type = "gooptions"
        self.platform_list.add(button1)  
        
        help_button = pygame.image.load("keys.png").convert()
        button1 = platforms.Button(help_button, 50, 100)   
        button1.p1 = self.p1
        button1.level = self
        button1.button_type = "help"
        self.platform_list.add(button1)         

class Win_Screen(Level):
    def __init__(self, p1):
        Level.__init__(self, p1)
        self.background = pygame.image.load("Win_Screen.png").convert()
        self.background.set_colorkey(constants.WHITE)

        quit_button = pygame.image.load("Quit_Button.png").convert()
        button1 = platforms.Button(quit_button, 400, 500)   
        button1.p1 = self.p1
        button1.level = self
        button1.button_type = "quit"
        self.platform_list.add(button1) 


class Level_01(Level):
    """ Definition for level 1. """
 
    def __init__(self, p1):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, p1)
 
        self.background = pygame.image.load("hut_background.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit_right = -8300
                 
        
        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.WOOD_TALL, 250, 0],
                  [platforms.WOOD_TALL, 250, 150],
                  [platforms.WOOD_TALL, 250, 300],
                  [platforms.WOOD_TALL, 250, 450],
                  [platforms.WOOD_LONG, 500, 350],
                  [platforms.WOOD_TALL, 800, 450],
                  [platforms.WOOD_TALL, 800, 300],
                  [platforms.WOOD_LONG, 2000, 450],
                  [platforms.STONE_SMALL, 2100, 450],
                  [platforms.STONE_LONG, 2150, 450],
                  [platforms.STONE_TALL, 2300, 300],
                  [platforms.STONE_MEDIUM, 3950, 450],
                  [platforms.STONE_LONG, 4150, 300],
                  [platforms.STONE_LONG, 4300, 300],
                  [platforms.STONE_LONG, 4450, 300],
                  [platforms.STONE_LONG, 4600, 300],
                  [platforms.WOOD_TALL, 5300, 0],
                  [platforms.WOOD_TALL, 5300, 150],
                  [platforms.WOOD_SMALL, 5300, 300],
                  [platforms.STONE_LONG, 6300, 300],
                  [platforms.STONE_LONG, 6450, 300],
                  [platforms.STONE_LONG, 6600, 300],
                  [platforms.STONE_LONG, 6750, 300],
                  [platforms.STONE_LONG, 7150, 300],
                  [platforms.STONE_LONG, 7300, 300],
                  [platforms.STONE_LONG, 7450, 300],
                  [platforms.STONE_LONG, 7600, 300],
                  [platforms.STONE_LONG, 8050, 300],
                  ]
 
 
        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.p1 = self.p1
            self.platform_list.add(block)
            
        pride = [ [1100, 450],
                  [1600, 450],
                  [2700, 450],
                  [3500, 450],
                  [4400, 150],
                  [4800, 450],
                  [5500, 450],
                  [6400, 450],
                  [7400, 150],
                  [8500, 450],  
                  ]
        
        for lion in pride:
            lion1 = enemy.Lion()
            lion1.rect.x = lion[0]
            lion1.rect.y = lion[1]
            lion1.boundary_left = lion1.rect.x -200
            lion1.boundary_right = lion1.rect.x +200
            lion1.change_x = 1
            lion1.p1 = self.p1
            lion1.level = self
            self.enemy_list.add(lion1)     
        
        
        gate = platforms.Gate()
        gate.rect.x = 9000
        gate.rect.y = 300
        gate.p1 = self.p1
        self.platform_list.add(gate)        
        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.WOOD_SMALL)
        block.rect.x = 1750
        block.rect.y = 280       
        block.boundary_left = block.rect.x
        block.boundary_right = block.rect.x + 300
        block.change_x = 1
        block.p1 = self.p1
        block.level = self
        self.platform_list.add(block)
 
 
# Create platforms for the level
class Level_02(Level):
    """ Definition for level 2. """
 
    def __init__(self, p1):
        """ Create level 2. """
 
        # Call the parent constructor
        Level.__init__(self, p1)
 
        self.background = pygame.image.load("background_02.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit_right = -1000
 
        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.WOOD_TALL, 50, 0],
                  [platforms.WOOD_TALL, 50, 150],
                  [platforms.WOOD_TALL, 50, 300],
                  [platforms.WOOD_TALL, 50, 450],
                  [platforms.WOOD_TALL, 1300, 0],
                  [platforms.WOOD_TALL, 1300, 150],
                  [platforms.WOOD_TALL, 1300, 300],
                  [platforms.WOOD_TALL, 1300, 450],
                  ]
 
 
        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.p1 = self.p1
            self.platform_list.add(block)
        
        lion1 = enemy.BigLion()
        lion1.rect.x = 700
        lion1.rect.y = 400
        lion1.boundary_left = lion1.rect.x -600
        lion1.boundary_right = lion1.rect.x +300
        lion1.boundary_top = lion1.rect.y -400
        lion1.boundary_bottom = lion1.rect.y +200
        lion1.change_x = 1
        lion1.change_y = 1
        lion1.p1 = self.p1
        lion1.level = self
        self.enemy_list.add(lion1)
 
