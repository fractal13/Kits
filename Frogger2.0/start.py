import pygame
from myLibrary import *
import time

## this will tell pygame to start
pygame.init()

## decide how big the window size will be
display_width = 600
display_height = 600
## this will keep track of time throughout the game
clock = pygame.time.Clock()
## this will make the screen display, you can also give your program a name
programName = "Your programs name here"
gameDisplay = start_display(display_width, display_height, programName)

bg = setBackground("images/FroggerBG.png")


## this block of code defines our ship
class Frog:
    def __init__(self, x_position, y_position, delta_x, delta_y, width, height):
        self.mX = x_position 								# this sets where our x position will be
        self.mY = y_position 								# this sets where our y position will be
        self.mDX = delta_x									# this tells us how fast our frog moves
        self.mDY = delta_y							
        self.mWidth = width 								# this sets our ships width
        self.mHeight = height 								# this sets our ships height
        self.mImage = pygame.image.load('images/Frog.png') 	# this tells us which picture to use for our Frog

def makeFrog():
	return Frog(display_width*.45, display_height*.9, 0,0, 50, 45)

def draw_frog(frog):
	draw_image(gameDisplay, frog.mX, frog.mY, frog.mImage)
	return

def move_frog(frog):
	frog.mX += frog.mDX
	frog.mY += frog.mDY



## this block is what calls the rest of our code 
def main_loop():
    gameOver = False
    frog = makeFrog()

    ## this while loop will repeat over and over until the game ends
    while not gameOver:
    	## this for loop keeps track of all the keys that you push in the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT: ## this would be the X button in the top right corner
                pygame.quit()
                quit()
            ## this if statement will keep track of all keys pressed DOWN
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_LEFT:
                	# if the Left arrow key was pressed
                	frog.mX += -10
                if event.key == pygame.K_RIGHT:
                	# if the Right arrow key was pressed
                	frog.mX += 10
                if event.key == pygame.K_UP:
                	# if the Up arrow key was pressed
                	if frog.mY < display_height*.4:
                		frog.mY -= 70
                	else:
                		frog.mY -= 55
                if event.key == pygame.K_DOWN:
                	# if the Down arrow key was pressed
                	frog.mDY = 3
                if event.key == pygame.K_SPACE:
                	# if the Space key was pressed
                	print("space key pressed")
                if event.key == pygame.K_r:
                	# if the R key was pressed
                	print("restart key pressed")
            ## this if statement will keep track of all keys RELEASED
            if event.type == pygame.KEYUP:
                 if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                 	frog.mDX = 0
                 if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                 	frog.mDY = 0

        drawBackground(gameDisplay, bg) 				## set the background
       
        draw_frog(frog) 								## draw the frog every frame
        move_frog(frog) 								## tell the frog to move
       
        # this will refresh the screen and make updates
        update()
        clock.tick(60)
main_loop()