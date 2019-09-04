Making Cars and Trucks and Logs
-------------------------------

To make Frogger a little more interesting, we will add cars and trucks to cross the road in different directions. To complete the Cars and trucks we will DEFINE a car or truck, DRAW them on the screen, and finally MOVE them.  

Defining A Truck or Car or Log
-------------------------------

We will use a class called Moving_Object to help us with this:

class Moving_Object:
    def __init__(self, x_position, y_position, delta_x, delta_y, width, height, image):
        self.mX = x_position 							# this sets where our x position will be
        self.mY = y_position 							# this sets where our y position will be
        self.mDX = delta_x								# this tells us how fast our object moves
        self.mDY = delta_y							
        self.mWidth = width 							# this sets our object width
        self.mHeight = height 							# this sets our object height
        self.mImage = pygame.image.load(image) 

This class will be used for all of the moving objects in our game.  Put this code right under the Frog class.  

Next we need to make a few lists to hold all of our moving objects data.  Write the following lists at the top of the file just above the Frog Class.

trucks1 = []
trucks2 = []
cars1 = []
cars2 = []
logs1 = []
logs2 = []
logs3 = []

Now to call this code to make all of our objects, implement this function called make_all_objects():

def make_all_objects():
	## make 7 of each object
	for i in range(1,8):
		leftTruck = Moving_Object(display_width + (200 * i), display_height*.81, -2, 0, 107, 57, 'images/Truck.png')
		trucks1.append(leftTruck)
		leftCar = Moving_Object(display_width + (300 * i), display_height*.715, -3, 0, 106, 57, 'images/Car2.png')
		cars2.append(leftCar)

		rightTruck = Moving_Object(0 - (200 * i), display_height*.61, 2, 0, 105, 57, 'images/Truck2.png')
		trucks2.append(rightTruck)
		rightCar = Moving_Object(0 - (300 * i), display_height*.525, 3, 0, 105, 57, 'images/Car.png')
		cars1.append(rightCar)

		leftLog1 = Moving_Object(display_width + (300 * i), display_height*.33, -2.5, 0, 236, 59, 'images/Log.png')
		logs1.append(leftLog1)
		leftLog2 = Moving_Object(display_width + (350 * i), display_height*.1, -2.5, 0, 236, 59, 'images/Log.png')
		logs2.append(leftLog2)

		rightLog = Moving_Object(0 - (350 * i), display_height*.2, 2.5, 0, 236, 59, 'images/Log.png')
		logs3.append(rightLog)

Finally, call make_all_objects() at the very top of the mainLoop function, as this will make all our objects.

make_all_objects()



Drawing A Truck or Car or Log
-------------------------------

Now that all of our moving objects data is stored in the lists at the top of our file, we now need to draw them. Implement these draw functions for each of the lists that we've made just under the make_all_objects function.

def draw_vehicles():
	for truck in trucks1:
		draw_image(gameDisplay, truck.mX, truck.mY, truck.mImage)
	for truck in trucks2:
		draw_image(gameDisplay, truck.mX, truck.mY, truck.mImage)
	for car in cars1:
		draw_image(gameDisplay, car.mX, car.mY, car.mImage)
	for car in cars2:
		draw_image(gameDisplay, car.mX, car.mY, car.mImage)
	
def draw_logs():
	for log in logs1:
		draw_image(gameDisplay, log.mX, log.mY, log.mImage)
	for log in logs2:
		draw_image(gameDisplay, log.mX, log.mY, log.mImage)
	for log in logs3:
		draw_image(gameDisplay, log.mX, log.mY, log.mImage)

We now have objects that are drawn onto our game display, but they cannot move at all yet.


Moving A Truck or Car or Log
-----------------------------

Moving an object that has been drawn is the final piece of the this puzzle. Implement the following code just under the draw_vehicles and draw_logs functions.

def move_vehicles():
	for truck in trucks1:
		truck.mX += truck.mDX
		if truck.mX < (truck.mWidth * -1):
			truck.mX = 1000
	for truck in trucks2:
		truck.mX += truck.mDX
		if truck.mX > (truck.mWidth + displayWidth):
			truck.mX = -1000
	for car in cars1:
		car.mX += car.mDX
		if car.mX < (car.mWidth * -1):
			car.mX = 1000
	for car in cars2:
		car.mX += car.mDX
		if car.mX > (car.mWidth + displayWidth):
			car.mX = -1000

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

This code will move our objects and give life to the game. Finally, call all of these functions in the Main_loop() just below the move_frog(frog) function.

draw_vehicles()
move_vehicles()

Since we want the frog to be drawn ON TOP OF THE LOGS, we need to draw the logs before we draw the frog. Call these functions just before the draw_frog() function.

draw_logs()
move_logs()