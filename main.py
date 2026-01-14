from aircraft_manager import AirCraft
from bullets import Bullets
from enemy import Enemy
from scoreboard import *
import winsound
# ---------------- SCREEN SETUP ----------------
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("AIR-COMBAT")
screen.tracer(0)

# ---------------- GAME OBJECTS ----------------
air_craft = AirCraft()
scoreboard=ScoreBoard()
bullets_list = []
enemy_list = []

enemy_spawn_counter = 0
game_is_on = True

# ---------------- CONTROLS ----------------
def fire_bullet():
    bullet = Bullets(air_craft.position())
    bullets_list.append(bullet)

screen.listen()
screen.onkey(air_craft.l_move, "Left")
screen.onkey(air_craft.r_move, "Right")
screen.onkey(fire_bullet, "space")

# ---------------- GAME LOOP ----------------
def game_loop():
    global enemy_spawn_counter, game_is_on

    if not game_is_on:
        return

    # ---- MOVE BULLETS ----
    for bullet in bullets_list:
        bullet.move()
        if bullet.ycor() > 300:
            bullet.hideturtle()
            bullets_list.remove(bullet)

    # ---- SPAWN ENEMIES ----
    enemy_spawn_counter += 1
    if enemy_spawn_counter == 60:
        enemy_list.append(Enemy())
        enemy_spawn_counter = 0

    # ---- MOVE ENEMIES ----
    for enemy in enemy_list:
        enemy.move()
        if enemy.ycor() < -320:
            enemy.hideturtle()
            enemy_list.remove(enemy)

    # ---- BULLET–ENEMY COLLISION ----
    for enemy in enemy_list:
        for bullet in bullets_list:
            if bullet.distance(enemy) < 20:
                bullet.hideturtle()
                enemy.hideturtle()
                winsound.Beep(1000,100)
                bullets_list.remove(bullet)
                enemy_list.remove(enemy)
                scoreboard.increase_score()

    # ---- PLAYER–ENEMY COLLISION ----
    for enemy in enemy_list:
        if enemy.distance(air_craft) < 20:
            scoreboard.game_over()
            return

    screen.update()
    screen.ontimer(game_loop, 16)
# ---------------- START ----------------
game_loop()
screen.exitonclick()

