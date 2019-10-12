# Space invaders using turtle
import turtle
import math
import random

# set up screen
screen = turtle.Screen()
screen.setup(600, 600, 300, 50)
screen.bgpic("space_bg.png")
screen.title("Space Invaders by Duke of Burritoshire")
turtle.register_shape("enemy 1.gif")
turtle.register_shape("xwing.gif")
turtle.register_shape("xwing_left.gif")
turtle.register_shape("xwing_right.gif")

# set up player
player = turtle.Turtle()
player.speed(0)
player.showturtle()
player.penup()
player.setposition(0, -240)
player.shape("xwing.gif")
player.setheading(90)
player.speed(3)
playerspeed = 60


# list of enemies
number_of_enemies = 5
enemies = []
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())
for enemy in enemies:
    # set up enemy 1
    enemy.speed(0)
    enemy.showturtle()
    enemy.penup()
    #enemy.setposition(0, 240)
    enemy.setposition(random.randint(-270, 270), random.randint(150, 240))
    enemy.shape("enemy 1.gif")
    enemy.setheading(270)
    enemy.speed(1)
enemyspeed = 10
enemymoving = False


# set up player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.speed(0)
bullet.penup()
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
bulletspeed = 20
bulletstate = "ready"


# moving player
def move_left():
    x = player.xcor()
    x -= playerspeed / 2
    if x > -300:
        player.shape("xwing_left.gif")
        player.setx(x)

        x -= playerspeed / 2
        player.shape("xwing.gif")
        player.setx(x)


def move_right():
    x = player.xcor()
    x += playerspeed / 2
    if x < 300:
        player.shape("xwing_right.gif")
        player.setx(x)

        x += playerspeed / 2
        player.shape("xwing.gif")
        player.setx(x)


def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fired"
        x = player.xcor()
        y = player.ycor() + 20
        bullet.setposition(x, y)
        bullet.showturtle()


def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 40:
        return True
    else:
        return False


# key bindings
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(fire_bullet, "space")
screen.listen()


# Main game loop
while True:
    for enemy in enemies:
        # moving the bullet
        if bulletstate == "fired":
            y = bullet.ycor()
            y += bulletspeed
            bullet.sety(y)
            if bullet.ycor() > 300:
                bulletstate = "ready"
            if isCollision(enemy, bullet):
                # reset the bullet
                bulletstate = "ready"
                bullet.hideturtle()
                # reset the enemy
                enemy.hideturtle()
                enemy.setposition(random.randint(-270, 270), 240)
                enemy.showturtle()
                enemyspeed = math.fabs(enemyspeed)
        # moving the enemy
        x = enemy.xcor()
        x += enemyspeed
        if -270 < x < 270:
            enemy.setx(x)
        else:
            enemyspeed *= -1
            for enemy1 in enemies:
                enemy1.sety(enemy1.ycor() - 60)
        # this is the end
        if enemy.ycor() < -220:
            screen.bye()
            print("Game over")


