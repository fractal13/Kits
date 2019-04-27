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

bg = setBackground("BG.png")
trucks1 = []
trucks2 = []
cars1 = []
cars2 = []
logs1 = []
logs2 = []
logs3 = []

## this block of code defines our ship
class Frog:
    def __init__(self, x_position, y_position, delta_x, delta_y, width, height):
        self.mX = x_position 							# this sets where our x position will be
        self.mY = y_position 							# this sets where our y position will be
        self.mDX = delta_x								# this tells us how fast our frog moves
        self.mDY = delta_y							
        self.mWidth = width 							# this sets our ships width
        self.mHeight = height 							# this sets our ships height
        self.mImage = pygame.image.load('Frog.png') 	# this tells us which picture to use for our Frog

def draw_frog(frog):
	draw_image(gameDisplay, frog.mX, frog.mY, frog.mImage)
	return

def move_frog(frog):
	frog.mX += frog.mDX
	frog.mY += frog.mDY

class Moving_Object:
    def __init__(self, x_position, y_position, delta_x, delta_y, width, height, image):
        self.mX = x_position 							# this sets where our x position will be
        self.mY = y_position 							# this sets where our y position will be
        self.mDX = delta_x								# this tells us how fast our object moves
        self.mDY = delta_y							
        self.mWidth = width 							# this sets our object width
        self.mHeight = height 							# this sets our object height
        self.mImage = pygame.image.load(image) 

def make_all_objects():
	## make 7 of each object
	for i in range(1,4):
		leftTruck = Moving_Object(display_width + (200 * i), display_height*.81, -2, 0, 107, 57, 'Truck.png')
		trucks1.append(leftTruck)

		leftCar = Moving_Object(display_width + (300 * i), display_height*.715, -3, 0, 106, 57, 'Car2.png')
		cars2.append(leftCar)

		rightTruck = Moving_Object(0 - (200 * i), display_height*.61, 2, 0, 105, 57, 'Truck2.png')
		trucks2.append(rightTruck)

		rightCar = Moving_Object(0 - (300 * i), display_height*.525, 3, 0, 105, 57, 'Car.png')
		cars1.append(rightCar)

		leftLog1 = Moving_Object(display_width + (300 * i), display_height*.33, -2.5, 0, 236, 59, 'Log.png')
		logs1.append(leftLog1)

		leftLog2 = Moving_Object(display_width + (350 * i), display_height*.1, -2.5, 0, 236, 59, 'Log.png')
		logs2.append(leftLog2)

		rightLog = Moving_Object(0 - (350 * i), display_height*.2, 2.5, 0, 236, 59, 'Log.png')
		logs3.append(rightLog)
	return

def draw_vehicles():
	for truck in trucks1:
		draw_image(gameDisplay, truck.mX, truck.mY, truck.mImage)
	for truck in trucks2:
		draw_image(gameDisplay, truck.mX, truck.mY, truck.mImage)
	for car in cars1:
		draw_image(gameDisplay, car.mX, car.mY, car.mImage)
	for car in cars2:
		draw_image(gameDisplay, car.mX, car.mY, car.mImage)
	
def move_vehicles():
	for truck in trucks1:
		truck.mX += truck.mDX
		if truck.mX < (truck.mWidth * -1):
			truck.mX = 1000
	for truck in trucks2:
		truck.mX += truck.mDX
		if truck.mX > (truck.mWidth + display_width):
			truck.mX = -1000
	for car in cars1:
		car.mX += car.mDX
		if car.mX > (car.mWidth + display_width):
			car.mX = -1000
	for car in cars2:
		car.mX += car.mDX
		if car.mX < (car.mWidth * -1):
			car.mX = 1000
		
	
def draw_logs():
	for log in logs1:
		draw_image(gameDisplay, log.mX, log.mY, log.mImage)
	for log in logs2:
		draw_image(gameDisplay, log.mX, log.mY, log.mImage)
	for log in logs3:
		draw_image(gameDisplay, log.mX, log.mY, log.mImage)

def move_logs():
	for log in logs1:
		log.mX += log.mDX
		if log.mX < (log.mWidth * -1):
			log.mX = 1000
	for log in logs2:
		log.mX += log.mDX
		if log.mX < (log.mWidth * -1):
			log.mX = 1000
	for log in logs3:
		log.mX += log.mDX
		if log.mX > (log.mWidth + display_width):
			log.mX = -1000
		

def car_hits_frog(frog):
	for truck in trucks1:
		if collide_rect(truck, frog):
			return True
	for truck in trucks2:
		if collide_rect(truck, frog):
			return True
	for car in cars1:
		if collide_rect(car, frog):
			return True
	for car in cars2:
		if collide_rect(car, frog):
			return True
	return False

def frog_in_water(frog):
	if frog.mY + frog.mHeight < display_height/2: 
		for log in logs1:
			if collide_rect(log, frog):
				return False
		for log in logs2:
			if collide_rect(log, frog):
				return False
		for log in logs3:
			if collide_rect(log, frog):
				return False
		return True
	else:
		return False

def frog_on_log(frog):
	for log in logs1:
		if collide_rect(log, frog):
			frog.mDX = log.mDX
	for log in logs2:
		if collide_rect(log, frog):
			frog.mDX = log.mDX
	for log in logs3:
		if collide_rect(log, frog):
			frog.mDX = log.mDX

def frog_gets_home(frog):
	if frog.mY < 25:
		return True
	return False

## this block is what calls the rest of our code 
def main_loop():
    make_all_objects()
    gameOver = False
    frog = Frog(display_width*.45, display_height*.9, 0,0, 50, 45)
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
        ## draw the logs
        draw_logs()
        move_logs()
        ## draw the frog
        draw_frog(frog) 								## draw the frog every frame
        move_frog(frog) 								## tell the frog to move
        ## check out of bounds
        if out_of_bounds(frog):
        	gameOver = True 
        ## draw truck and car stuff
        draw_vehicles()
        move_vehicles()

        ## check if frog hits a car
        if car_hits_frog(frog):
        	gameOver = True
        ## check if frog is in water
        if frog_in_water(frog):
        	gameOver = True
        ## check if frog lands on log
        frog_on_log(frog)

        if frog_gets_home(frog):
        	display_message(gameDisplay, "YOU WIN", 100)
        	time.sleep(5)

        # this will refresh the screen and make updates
        pygame.display.update()
        clock.tick(60)

main_loop()