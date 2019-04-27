import pygame

## window constants, these will be adjusted upon calling start_display
display_width = 1600
display_height = 800

# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (255, 0, 255)


###################### example class #################################

# class Thing:
#     def __init__(self, x_position, y_position, delta_x, delta_y, width, height, image):
#         self.mX = x_position 						# this sets where our x position will be
#         self.mY = y_position 						# this sets where our y position will be
#         self.mDX = delta_x						# this tells us how fast our object moves to the left or right
#         self.mDY = delta_y						# this tells us how fast our object moves up or down
#         self.mWidth = width 						# this sets our ships width
#         self.mHeight = height 					# this sets our ships height
#         self.mImage = pygame.image.load(image) 	# this tells us which picture to use for our object

############################# Functions #############################
## ************ Use example class as a reference for objects ********* ##

## take in three parameters, width, height and the programs name. Returns the Display
def start_display(width, height, name):
	display_width = width
	display_height = height
	display = pygame.display.set_mode((width,height))
	pygame.display.set_caption(name)
	return display

## takes text and displays is to the center of the screen in the given size
def display_message(display, text, size):
    textFont = pygame.font.Font('CourierNewBold.ttf', size)
    textSurface = textFont.render(text, True, white)
    textRect = textSurface.get_rect()
    textRect.center = (display_width/2, display_height/2)
    display.blit(textSurface, textRect)
    pygame.display.update()

## returns true if the objects are touching, false otherwise (assuming the objects are both rects) image sprites are rects
## both objects must have .mX and .mY and .mWidth and .mHeight data members
def collide_rect(object1, object2):
	if object1.mX + object1.mWidth > object2.mX > object1.mX and object1.mY + object1.mHeight > object2.mY > object1.mY:
		## top left corner of object2 is inside object1, return true
		return True 
	if object1.mX + object1.mWidth > object2.mX + object2.mWidth > object1.mX and object1.mY + object1.mHeight > object2.mY > object1.mY:
		## top right corner of object2 is inside object1, return true
		return True
	if object1.mX + object1.mWidth > object2.mX > object1.mX and object1.mY + object1.mHeight > object2.mY + object2.mHeight > object1.mY:
		## bottom left corner of object2 is inside object1, return true
		return True
	if object1.mX + object1.mWidth > object2.mX + object2.mWidth > object1.mX and object1.mY + object1.mHeight > object2.mY + object2.mHeight > object1.mY:
		## bottom right corner of object2 is inside object1, return true
		return True
	if object2.mX + object2.mWidth > object1.mX > object2.mX and object2.mY + object2.mHeight > object1.mY > object2.mY:
		## top left corner of object2 is inside object1, return true
		return True 
	if object2.mX + object2.mWidth > object1.mX + object1.mWidth > object2.mX and object2.mY + object2.mHeight > object1.mY > object2.mY:
		## top right corner of object2 is inside object1, return true
		return True
	if object2.mX + object2.mWidth > object1.mX > object2.mX and object2.mY + object2.mHeight > object1.mY + object1.mHeight > object2.mY:
		## bottom left corner of object2 is inside object1, return true
		return True
	if object2.mX + object2.mWidth > object1.mX + object1.mWidth > object2.mX and object2.mY + object2.mHeight > object1.mY + object1.mHeight > object2.mY:
		## bottom right corner of object2 is inside object1, return true
		return True
	else:
		return False 

## will return true is the object is touching out of bounds, false otherwise
## requires object to have .mX, .mY, .mWidth, and .mHeight data members
def out_of_bounds(object1):
	if object1.mX < 0:
		return True 
	elif object1.mX > display_width - object1.mWidth:
		return True 
	elif object1.mY < 0:
		return True 
	elif object1.mY > display_height - object1.mHeight:
		return True 
	else: 
		return False

## loads image and returns the image
def load_image(image_name):
	image = pygame.image.load(image_name)
	return image

## draws image onto display at x,y
def draw_image(display, x, y, image):
	display.blit(image, (x, y))
	return
## this will draw an object that has an x and y coordinate as well as an image
def draw_object(display, object1):
	display.blit(object1.mImage, (object1.mX, object1.mY))

## updates the display
def update():
	pygame.display.update()

def drawCircle(display, x, y, color):
	pygame.draw.circle(display, color, (x,y), 0, 0)

def randomNumber(start, end):
	return random.randint(start, end)

def randomDecimal(start, end):
	return random.uniform(start, end)







