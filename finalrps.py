# file created by Kyle Herbold

# import libraries

from time import sleep

from random import randint

import pygame as pg

import os

# libraries
# import time to create suspense
from time import sleep
# random number generater to make the game fair
from random import randint

# setup asset folders -images and sounds 
game_folder = os.path.dirname(__file__)
print(game_folder)

# game settings
WIDTH = 500
HEIGHT = 500
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Rock Paper Scissors")
clock = pg.time.Clock()

# imports images
rock_image = pg.image.load(os.path.join(game_folder,  "rock.jpg")).convert()
paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.jpg')).convert()
welcome_image = pg.image.load(os.path.join(game_folder, 'welcome screen.png')).convert()
tied_image = pg.image.load(os.path.join(game_folder, 'tied.jpg')).convert()
winrock_image = pg.image.load(os.path.join(game_folder, 'winrock.png')).convert()
loserock_image = pg.image.load(os.path.join(game_folder, 'loserock.png')).convert()
winpaper_image = pg.image.load(os.path.join(game_folder, 'winpaper.png')).convert()
losepaper_image = pg.image.load(os.path.join(game_folder, 'losepaper.png')).convert()
winscissors_image = pg.image.load(os.path.join(game_folder, 'winscissors.png')).convert()
losescissors_image = pg.image.load(os.path.join(game_folder, 'losescissors.png')).convert()


# creates transparency
rock_image.set_colorkey(GREEN)
paper_image.set_colorkey(GREEN)
scissors_image.set_colorkey(GREEN)


# gets the geometry of the image
welcome_rect = welcome_image.get_rect()
rock_rect = rock_image.get_rect()
paper_rect = paper_image.get_rect()
scissors_rect = scissors_image.get_rect()
tied_rect = tied_image.get_rect()
winrock_rect = winrock_image.get_rect()
loserock_rect = loserock_image.get_rect()
winpaper_rect = winpaper_image.get_rect()
losepaper_rect = losepaper_image.get_rect()
winscissors_rect = winscissors_image.get_rect()
losescissors_rect = winpaper_image.get_rect()


# moves the image 
paper_rect.y = HEIGHT/2.3
paper_rect.x = WIDTH/8
scissors_rect.x = WIDTH/1.5
rock_rect.y = HEIGHT/1.8
rock_rect.x = WIDTH/1.8

# Scales the images to take over the screen if called on
welcome_image = pg.transform.scale(welcome_image, (350,300))
tied_image = pg.transform.scale(tied_image, (500,500))
winrock_image = pg.transform.scale(winrock_image, (500,500))
loserock_image = pg.transform.scale(loserock_image, (500,500))
winpaper_image= pg.transform.scale(winpaper_image, (500,500))
losepaper_image= pg.transform.scale(losepaper_image, (500,500))
winscissors_image= pg.transform.scale(winscissors_image, (500,500))
losescissors_image= pg.transform.scale(losescissors_image, (500,500))

# instructions in the console
print("let's play a game!: rock paper scissors")
sleep(1)
print("choose rock paper or scissors")

# define  the choices and computer choice by taking a random number
choices = ["rock", "paper", "scissors"]
def cpu_choice():
    return choices[randint(0,2)]
   
    
# start of the loop
running = True
welcome_screen = True
user_choice = ""
cpu_picked = " "
mouse_coords = (0,0)
while running:
    clock.tick(FPS)
    # Input
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_coords = pg.mouse.get_pos()
            print("welcome screen is off...")
 # finding the user choice and gets the computer choice
            if (rock_rect.collidepoint(mouse_coords)) == True :
                print ("you chose rock")
                user_choice = "rock"
                cpu_picked = cpu_choice()
                print("the computer chose " + cpu_picked)
            elif paper_rect.collidepoint(mouse_coords) == True :
                print("you chose paper")
                user_choice = "paper"
                cpu_picked = cpu_choice()
                print("the computer chose " + cpu_picked)
            elif scissors_rect.collidepoint(mouse_coords) == True:
                print("you chose scissors")
                user_choice = "scissors"
                cpu_picked = cpu_choice()
                print("the computer chose " + cpu_picked)
            else :   
                print("you did not choose")
 # creates the value judgements and displays the winner along with the user choice and computer choice
    ####### Update ##########
    # Not used....
    
    
    ########## Draw Loop ###############
    screen.fill(WHITE)

    if user_choice == "":
            print("welcome screen is on...")
            screen.blit(welcome_image, welcome_rect)
            screen.blit(scissors_image, scissors_rect)
            screen.blit(paper_image, paper_rect)
            screen.blit(rock_image, rock_rect)
    elif user_choice == cpu_picked:
            print("tie")
            screen.blit(tied_image, tied_rect)
    elif user_choice == "rock" and cpu_picked == "scissors" :
            print ("WINNER!")  
            screen.blit(winrock_image, winrock_rect)
    elif user_choice == "rock" and cpu_picked == "paper" :
            print ("LOSE!")  
            screen.blit(loserock_image, loserock_rect)
    elif user_choice == "paper" and cpu_picked == "scissors" :
            print ("LOSE!")  
            screen.blit(losepaper_image, losepaper_rect)
    elif user_choice == "paper" and cpu_picked == "rock" :
            print ("WINNER!") 
            screen.blit(winpaper_image, winpaper_rect) 
    elif user_choice == "scissors" and cpu_picked == "rock" :
            print ("LOSE!")  
            screen.blit(losescissors_image,losepaper_rect)
    elif user_choice == "scissors" and cpu_picked == "paper" :
            print ("WINNER!")    
            screen.blit(losescissors_image,losescissors_rect)  
    

    pg.display.flip()


pg.quit()




