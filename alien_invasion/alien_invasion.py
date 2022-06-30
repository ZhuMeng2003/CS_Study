import sys
import pygame
from pygame.sprite import Group
from settings import Settings 
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize pygame, settings, and screen object.
    # Initialize game and create a screen object.
    pygame.init() #(initializes background settings)
    
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion") #(caption of the screen)
    #bg_color = (0, 0, 255)

    #make a ship
    ship = Ship(ai_settings, screen)
    
    # Make a group to store bullets in.
    bullets = Group()

    
    # Start the main loop for the game.
    while True: #(while loopwthat contains an event loop and code that manages screen updates)(An event is an action that the user performs while playing the game)
        gf.check_events(ai_settings, screen, ship, bullets) #(The main loop checks for player input )
        ship.update() #(updates the position of the ship)
        gf.update_bullets(bullets) #(any bullets that have been fired)
        gf.update_screen(ai_settings, screen, ship, bullets)  #(use the updated positions to draw a new screen)
        
        for event in pygame.event.get(): #(The for loop atxis an event loop)
            if event.type == pygame.QUIT:
                sys.exit()
                
        screen.fill(ai_settings.bg_color)  #(fill the backgroud color)
        # screen.blit(IMAGE_SMALL, 50,50)
        ship.blitme()
        
        # Make the most recently drawn screen visible.
        pygame.display.flip()
run_game()