Collision
---------

As our game is right now, our ships go right through everything.  Nothing happens when 2 objects touch each other.  We want to change this so that the game has some meaning.  We care that the asteroids don't touch the ships, that the lasers touch the asteroids, and finally that the lasers touch the ships.

To implement this, lets make a function called check_for_collisions() as follows:

def check_for_collisions(player1, player2):
    for laser in player1Lasers:
        if collide_rect(laser, player2):
            return 1        ## player1 hit player 2, give player1 a point
    for laser in player2Lasers:
        if collide_rect(laser, player1):
            return 2        ## player2 hit player1, give player2 a point
    for asteroid in asteroidList:
        if collide_rect(asteroid, player2):
            return 1        ## player 2 was hit by asteroid, player1 wins
        elif collide_rect(asteroid, player1):
            return 2 
        for laser in player1Lasers:
            if collide_rect(asteroid, laser):
                asteroidList.remove(asteroid)
                player1Lasers.remove(laser)
                break
        for laser in player2Lasers:
            if collide_rect(asteroid, laser):
                asteroidList.remove(asteroid)
                player2Lasers.remove(laser)
                break
    return 0                ## no one got hit, just return 0


This function will return a 1, 2, or a 0.  If it returns a 1, then player1 wins because player2 was either hit by an asteroid or by one of player1's lasers.  If it returns a 2, then player2 wins because player1 was either hit by an asteroid or by one of player2's lasers.  If it returns a 0, then nothing collided with either player.  
NOTE: This function will also check to see if any lasers hit asteroids.  If a laser collides with an asteroid, both the laser and the asteroid will disappear.  

Finally we just need to decide what happens with the number that our collide function returns.

in our main loop just under movePlayer2Lasers() write:

x = check_for_collisions(player1, player2)
if x == 1:
    display_message(gameDisplay, "Player1 wins!", 100)
    time.sleep(3)
    gameOver = True
elif x == 2:
    display_message(gameDisplay, "Player2 wins!", 100)
    time.sleep(3)
    gameOver = True


This will end the game when a player wins!