import pygame
 
import constants
import levels
import enemy
import player

"""some code is borrowed from"""
 
def main():
    """ Main Program """
    pygame.init()
    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Right to Vengeance")
 
    # Create the player
    p1 = player.Player()
 
    # Create all the levels
    level_list = []
    level_list.append(levels.Start_Menu(p1))
    level_list.append(levels.Options_Menu(p1))
    level_list.append(levels.Help_Menu(p1))
    level_list.append(levels.Level_01(p1))
    level_list.append(levels.Level_02(p1))
    level_list.append(levels.Win_Screen(p1))
 
    # Set the current level
    current_level_no = 0
    previous_level_no = 0
    current_level = level_list[current_level_no]
 
    active_sprite_list = pygame.sprite.Group()
    p1.level = current_level
    enemy.level = current_level
 
    p1.rect.x = p1.level.player_x
    p1.rect.y = p1.level.player_y
    active_sprite_list.add(p1)
    
    pygame.mixer.music.load('brass_song.wav')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.set_volume(p1.music_volume)
 
    #Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    menu_up = True
 
    # -------- Main Program Loop -----------
    while not done:
        while not done and menu_up:
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    done = True # Flag that we are done so we exit this loop
     
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        current_level_no = 3
                        menu_up = False
                        current_level = level_list[current_level_no]
                        p1.level = current_level 
                        pygame.mixer.music.play() 
                    if event.key == pygame.K_2:
                        current_level_no = 4
                        menu_up = False
                        current_level = level_list[current_level_no]
                        p1.level = current_level   
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    x,y = event.pos
                
                    for button in current_level.platform_list:
                        if button.rect.collidepoint(x,y): 
                            if button.button_type == "start":
                                pygame.mixer.music.play() 
                                previous_level_no = current_level_no
                                current_level_no = 3
                                menu_up = False
                                current_level = level_list[current_level_no]
                                p1.level = current_level 
                            if button.button_type == "options":
                                previous_level_no = current_level_no
                                current_level_no = 1
                                current_level = level_list[current_level_no]
                            if button.button_type == "gooptions":
                                current_level_no = 1
                                current_level = level_list[current_level_no]                                
                            if button.button_type == "back":
                                temp = current_level_no
                                current_level_no = previous_level_no
                                previous_level_no = temp
                                current_level = level_list[current_level_no]
                                if current_level_no >= 3:
                                    p1.level = current_level 
                                    menu_up = False
                                    pygame.mixer.music.unpause() 
                            if button.button_type == "quit":
                                pygame.quit()
                            if button.button_type == "help":
                                current_level_no = 2
                                current_level = level_list[current_level_no]
                            if button.button_type == "music_plus":
                                if (p1.music_volume <= .95):
                                    p1.music_volume += .05
                                    pygame.mixer.music.set_volume(p1.music_volume)
                            if button.button_type == "music_minus":
                                if (p1.music_volume >= .05):
                                    p1.music_volume -= .05
                                    pygame.mixer.music.set_volume(p1.music_volume)
                            if button.button_type == "difficulty_plus":
                                if (p1.difficulty <= 5):
                                    p1.difficulty += 1
                                    p1.dif_multiplier = p1.dif_multiplier * 2
                            if button.button_type == "difficulty_minus":
                                if (p1.difficulty >= 1):
                                    p1.difficulty -=1
                                    p1.dif_multiplier = p1.dif_multiplier / 2

            # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
            current_level.draw_menu(screen)
            if current_level_no == 1:
                pygame.draw.rect(screen, constants.GREEN, [500, 300, p1.music_volume*200, 20])
            if current_level_no == 1:
                pygame.draw.rect(screen, constants.GREEN, [500, 385, p1.difficulty  * 50, 20])                
            # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
     
            # Limit to 60 frames per second
            clock.tick(60)
     
            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()      
        if not done:
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    done = True # Flag that we are done so we exit this loop
        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        current_level_no = 3 
                        current_level.player_x = p1.rect.x
                        current_level.player_y = p1.rect.y
                        current_level = level_list[current_level_no]
                        p1.level = current_level
                        p1.rect.x = current_level.player_x
                        p1.rect.y = current_level.player_y
                    if event.key == pygame.K_2:
                        current_level_no = 4
                        current_level.player_x = p1.rect.x
                        current_level.player_y = p1.rect.y
                        current_level = level_list[current_level_no] 
                        p1.level = current_level
                        p1.rect.x = current_level.player_x
                        p1.rect.y = current_level.player_y                                    
                    if event.key == pygame.K_j:
                        p1.p_attack = True                   
                    if event.key == pygame.K_a:
                        p1.go_left()
                    if event.key == pygame.K_d:
                        p1.go_right()
                    if event.key == pygame.K_w:
                        p1.jump()
                        #in event handling:  
                    if event.key == pygame.K_ESCAPE:
                        previous_level_no = current_level_no
                        current_level_no = 1
                        menu_up = True
                        current_level = level_list[current_level_no] 
                        pygame.mixer.music.pause() 
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_j:
                        p1.p_attack = False 
                    if event.key == pygame.K_a and p1.change_x < 0:
                        p1.stop()
                    if event.key == pygame.K_d and p1.change_x > 0:
                        p1.stop()
                if event.type == pygame.constants.USEREVENT:
                    # This event is triggered when the song stops playing.
                    pygame.mixer.music.load('level1_song.wav')
                    pygame.mixer.music.play()            
            # Update the player.
            active_sprite_list.update()
        
            # Update items in the level
            current_level.update()
        
            # If the player gets near the right side, shift the world left (-x)
            if p1.rect.x >= constants.RIGHT_SHIFT:
                diff = p1.rect.x - constants.RIGHT_SHIFT
                p1.rect.x = constants.RIGHT_SHIFT
                current_level.shift_world(-diff)
        
            # If the player gets near the left side, shift the world right (+x)
            if p1.rect.x <= constants.LEFT_SHIFT:
                diff = constants.LEFT_SHIFT - p1.rect.x
                p1.rect.x = constants.LEFT_SHIFT
                current_level.shift_world(diff)
        
            # If the player gets to the end of the level, go to the next level
            current_position = p1.rect.x + current_level.world_shift
            if p1.won == True:
                p1.rect.x = 120
                p1.won = False
                current_level_no += 1
                current_level = level_list[current_level_no]
                p1.level = current_level
            if p1.level_2_win == True:
                current_level_no = 5
                menu_up = True
                current_level = level_list[current_level_no] 
                pygame.mixer.music.pause()                 
            if (p1.hp < 1) :
                p1.rect.x = current_position -320
                p1.rect.y = constants.SCREEN_HEIGHT - p1.rect.height
                p1.hp = p1.MAX_HP
        
            # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
            current_level.draw(screen)
            active_sprite_list.draw(screen)
        
            # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        
            # Limit to 60 frames per second
            clock.tick(60)
        
            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
 
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
 
if __name__ == "__main__":
    main()
