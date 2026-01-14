from turtle import Screen, Turtle
from aircraft_manager import AirCraft
from bullets import Bullets
from enemy import Enemy
from scoreboard import ScoreBoard
import random
import winsound


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("AIR-COMBAT")
screen.tracer(0)


air_craft = AirCraft()
scoreboard = ScoreBoard()

bullets_list = []
enemy_list = []
stars = []

enemy_spawn_counter = 0
game_is_on = True


def create_stars():
    for _ in range(40):
        star = Turtle()
        star.hideturtle()
        star.penup()
        star.color("white")
        star.shape("circle")
        star.shapesize(0.1, 0.1)
        star.goto(random.randint(-390, 390), random.randint(-300, 300))
        star.showturtle()
        stars.append(star)

def move_stars():
    for star in stars:
        star.sety(star.ycor() - 2)
        if star.ycor() < -300:
            star.sety(300)


def explosion(position):
    boom = Turtle()
    boom.hideturtle()
    boom.penup()
    boom.color("orange")
    boom.shape("circle")
    boom.goto(position)
    boom.showturtle()
    boom.shapesize(1.5, 1.5)
    screen.update()
    boom.clear()
    boom.hideturtle()


def fire_bullet():
    bullet = Bullets(air_craft.position())
    bullets_list.append(bullet)

screen.listen()
screen.onkey(air_craft.l_move, "Left")
screen.onkey(air_craft.r_move, "Right")
screen.onkey(fire_bullet, "space")


def game_loop():
    global enemy_spawn_counter, game_is_on

    if not game_is_on:
        return

    move_stars()


    for bullet in bullets_list[:]:
        bullet.move()
        if bullet.ycor() > 300:
            bullet.hideturtle()
            bullets_list.remove(bullet)


    enemy_spawn_counter += 1
    if enemy_spawn_counter == 60:
        enemy_list.append(Enemy())
        enemy_spawn_counter = 0


    for enemy in enemy_list[:]:
        enemy.move()
        if enemy.ycor() < -320:
            enemy.hideturtle()
            enemy_list.remove(enemy)


    for enemy in enemy_list[:]:
        for bullet in bullets_list[:]:
            if bullet.distance(enemy) < 20:
                explosion(enemy.position())
                winsound.Beep(1000, 100)
                bullet.hideturtle()
                enemy.hideturtle()
                bullets_list.remove(bullet)
                enemy_list.remove(enemy)
                scoreboard.increase_score()


    for enemy in enemy_list:
        if enemy.distance(air_craft) < 35:
            scoreboard.game_over()
            return

    screen.update()
    screen.ontimer(game_loop, 16)


create_stars()
game_loop()
screen.exitonclick()

