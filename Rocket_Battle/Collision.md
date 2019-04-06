Collision
---------


Now that we have made Invaders and bullets, we need to do something if our bullets crash into the invaders.

This is simple.  Copy this function below drawShip().

def check_bullet_collisions():
    for bullet in BulletList:
        for invader in InvaderList:
            if collide_rect(invader, bullet):
                BulletList.remove(bullet)
                InvaderList.remove(invader)


And call this function in our mainLoop right below drawShip.

check_bullet_collisions()

Now that bullets will hit Invaders, we need to check and see if Invaders will hit our ship.

This is also simple. Copy this function below check_bullet_collisions().

def check_invader_collision(ship):
	for invader in InvaderList:
		if collide_rect(invader, ship):
			return True
	return False


And call this function in our main loop right below check_bullet_collisions()

if check_invader_collision(ship):
	game_over = True