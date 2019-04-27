Collision
---------

As our game is now, our frog can move through any of our objects.  Let's add collision so that our game has a little challenge. First we have to check and see if a Car hits our character, then if the Frog is on a Log, then if the frog is in the water, and finally if our frog has reached the goal. Implement the following code just below the move_logs() function.

Check for Car hitting Frog
--------------------------

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


Check for Frog on Log
---------------------

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

Check for Frog in Water
-----------------------

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

Check if Frog arrives at Goal
-----------------------------

def frog_gets_home(frog):
	if frog.mY < 25:
		return True
	return False


Now that we have all the functions needed to detect if our frog collides with anything, all thats left to do is to decide what will happen if the frog DOES hit something.  Implement this logic.

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


Now the game will end if the frog is hit by a car or falls in the river, but the frog will be carried on the logs and will win if the frog reaches the grass.