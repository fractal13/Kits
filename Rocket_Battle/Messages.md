Messages
--------

At some point in the game, you may want to display a message to the user.
We are going to assume that the message will either be a "You Win" or "You Lose" message

To do this, you simply need to call the display_message function.

display_message takes 3 parameters.
	First, is the Display,
	Second, is the text you wish to display, and,
	Third, is the font size


An example of calling this function would be to paste this code in our mainLoop below 
check_invader_collision(): 

if len(InvaderList) == 0:
    display_message(gameDisplay, "You Win", 100)
    time.sleep(2)
    gameOver = True

This would check if you have destroyed all the invaders and say that you have won.

Another example would be to replace 

if check_invader_collision(ship):
	gameOver = True

with

if check_invader_collision(ship):
	display_message(gameDisplay, "You Lose", 100)
	time.sleep(2)
	gameOver = True



