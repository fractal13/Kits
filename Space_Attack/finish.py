import pygame
from myLibrary import *
import time
import random

## this will tell pygame to start
pygame.init()

## decide how big the window size will be
display_width = 1600
display_height = 800
## this will keep track of time throughout the game
clock = pygame.time.Clock()

## this will make the screen display, you can also give your program a name
programName = "Your programs name here"
gameDisplay = start_display(display_width, display_height, programName)

bullets1 = []
bullets2 = []
asteroidList = []

## this block of code defines our ship
class Ship:
    def __init__(self, x_position, y_position, delta_x, delta_y, width, height, image):
        self.mX = x_position 						# this sets where our x position will be
        self.mY = y_position 						# this sets where our y position will be
        self.mDX = delta_x							# this tells us how fast our ship moves
        self.mDY = delta_y							
        self.mWidth = width 						# this sets our ships width
        self.mHeight = height 						# this sets our ships height
        self.mImage = pygame.image.load(image) 	# this tells us which picture to use for our ship

class Bullet:
    def __init__(self, x_position, y_position, delta_x, delta_y, width, height, image, damage):
        self.mX = x_position                        # this sets where our x position will be
        self.mY = y_position                        # this sets where our y position will be
        self.mDX = delta_x                          # this tells us how fast our bullet moves
        self.mDY = delta_y                          
        self.mWidth = width                         # this sets our ships width
        self.mHeight = height                       # this sets our ships height
        self.mImage = pygame.image.load(image)  # this tells us which picture to use for our bullet
        self.mDamage = damage

class Asteroid:
    def __init__(self, x_position, y_position, delta_x, delta_y, width, height, image):
        self.mX = x_position                        # this sets where our x position will be
        self.mY = y_position                        # this sets where our y position will be
        self.mDX = delta_x                          # this tells us how fast our asteroid moves
        self.mDY = delta_y                          
        self.mWidth = width                         # this sets our ships width
        self.mHeight = height                       # this sets our ships height
        self.mImage = pygame.image.load(image)  # this tells us which picture to use for our asteroid

def makeShip(image, start_x, start_y):
	x_position = start_x
	y_position = start_y
	delta_x = 0
	delta_y = 0
	width = 70
	height = 100
	ship = Ship(x_position, y_position, delta_x, delta_y, width, height, image)
	return ship

def drawShip(ship):
	draw_image(gameDisplay, ship.mX, ship.mY, ship.mImage)

def moveShip(ship):
    ship.mX += ship.mDX
    ship.mY += ship.mDY
    if out_of_bounds(ship):         ## if the ship is out of bounds, undo the last movement
        ship.mX -= ship.mDX
        ship.mY -= ship.mDY

## this will draw the stars in the background
def drawStars():
 	for i in range(25):
 		x = random.randint(0, display_width)
 		y = random.randint(0, display_height)
 		color = white 
 		drawCircle(gameDisplay, x, y, color)

def makeAsteroids():
    for i in range(15):
        asteroid = Asteroid(random.randint(0, display_width), random.randint(-900, -60), random.uniform(-1,1), 3, 60, 60, 'Asteroid.png')
        asteroidList.append(asteroid)

def draw_move_Asteroids():
    for asteroid in asteroidList:
        draw_object(gameDisplay, asteroid)
        asteroid.mX += asteroid.mDX
        asteroid.mY += asteroid.mDY
        if asteroid.mY > display_height:
            asteroid.mX = random.randint(0, display_width)
            asteroid.mY = random.randint(-900, -60)
            asteroid.mDX = random.uniform(-1,1)

## Player 1 functions
def makePlayer1Bullet(player1):
    if len(bullets1) < 5:
        bullet = Bullet(player1.mX + player1.mWidth, player1.mY + player1.mHeight / 2, 5, 0, 50, 16, 'Bullet1.png', 1)
        bullets1.append(bullet)

def drawPlayer1Bullets():
    for bullet in bullets1:
        draw_object(gameDisplay, bullet)

def movePlayer1Buttets():
    for bullet in bullets1:
        bullet.mX += bullet.mDX
        if out_of_bounds(bullet):
            bullets1.remove(bullet)

## Player 2 functions
def makePlayer2Bullet(player2):
    if len(bullets2) < 5:
        bullet = Bullet(player2.mX - 50, player2.mY + player2.mHeight / 2, -5, 0, 50, 16, 'Bullet2.png', 1)
        bullets2.append(bullet)

def drawPlayer2Bullets():
    for bullet in bullets2:
        draw_object(gameDisplay, bullet)

def movePlayer2Bullets():
    for bullet in bullets2:
        bullet.mX += bullet.mDX
        if out_of_bounds(bullet):
            bullets2.remove(bullet)

def check_for_collisions(player1, player2):
    for bullet in bullets1:
        if collide_rect(bullet, player2):
            return 1        ## player1 hit player 2, give player1 a point
    for bullet in bullets2:
        if collide_rect(bullet, player1):
            return 2        ## player2 hit player1, give player2 a point
    for asteroid in asteroidList:
        if collide_rect(asteroid, player2):
            return 1        ## player 2 was hit by asteroid, player1 wins
        elif collide_rect(asteroid, player1):
            return 2 
        for bullet in bullets1:
            if collide_rect(asteroid, bullet):
                asteroidList.remove(asteroid)
                bullets1.remove(bullet)
                break
        for bullet in bullets2:
            if collide_rect(asteroid, bullet):
                asteroidList.remove(asteroid)
                bullets2.remove(bullet)
                break
    return 0                ## no one got hit, just return 0

## this block is what calls the rest of our code 
def main_loop():
    gameOver = False 

    player1 = makeShip('ShipLeft.png', display_width * .1, display_height * .7) 			#this will make our ship
    player2 = makeShip('ShipRight.png',display_width * .9, display_height * .7)
    makeAsteroids()
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

                ## Player1  
                if event.key == pygame.K_a:
                    # if the Left arrow key was pressed
                    player1.mDX = -3
                if event.key == pygame.K_d:
                    # if the Right arrow key was pressed
                    player1.mDX = 3
                if event.key == pygame.K_w:
                    # if the Up arrow key was pressed
                    player1.mDY = -3
                if event.key == pygame.K_s:
                    # if the Down arrow key was pressed
                    player1.mDY = 3
                if event.key == pygame.K_SPACE:
                    # if the Space key was pressed
                    print("Space key pressed")
                    makePlayer1Bullet(player1)

                ## Player 2
                if event.key == pygame.K_LEFT:
                    # if the Left arrow key was pressed
                    player2.mDX = -3
                if event.key == pygame.K_RIGHT:
                    # if the Right arrow key was pressed
                    player2.mDX = 3
                if event.key == pygame.K_UP:
                    # if the Up arrow key was pressed
                    player2.mDY = -3
                if event.key == pygame.K_DOWN:
                    # if the Down arrow key was pressed
                    player2.mDY = 3
                if event.key == pygame.K_RETURN:
                    # if the Space key was pressed
                    print("enter key pressed")
                    makePlayer2Bullet(player2)

                if event.key == pygame.K_r:
                	# if the R key was pressed
                	print("restart key pressed")
            ## this if statement will keep track of all keys RELEASED
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    player1.mDX = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player1.mDY = 0
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player2.mDX = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                 	player2.mDY = 0

        gameDisplay.fill(black) 									## set the background to be black (other colors available in myLibrary.py)
        drawStars()
        draw_move_Asteroids()
        ## manage players
        drawShip(player1)										 		## this will draw our ship
        drawShip(player2)
        moveShip(player1)                                              ## this will update our ships position
        moveShip(player2)
        ## manage bullets
        drawPlayer1Bullets()
        movePlayer1Buttets()
        drawPlayer2Bullets()
        movePlayer2Bullets()
        ## manage collisions
        x = check_for_collisions(player1, player2)
        if x == 1:
            display_message(gameDisplay, "Player1 wins!", 100)
            time.sleep(3)
            gameOver = True
        elif x == 2:
            display_message(gameDisplay, "Player2 wins!", 100)
            time.sleep(3)
            gameOver = True
        # this will refresh the screen and make updates
        update()
        clock.tick(60)

main_loop()