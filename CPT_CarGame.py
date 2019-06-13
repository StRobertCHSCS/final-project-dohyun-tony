'''
-------------------------------------------------------------------------------
Name:		CPT_CarGame.py
Purpose:	This program is a car game. Player have to reach the finish line without collision with boxes.

Authors:	Kim. D, Dong. T

Created:	17/06/2019
------------------------------------------------------------------------------
'''

import arcade, random

# setting variables
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

ROW_COUNT = 5
COLUMN_COUNT = 1

WIDTH = 1500
HEIGHT = 100
finish = 1500

box = arcade.ShapeElementList()
box_x_position = []
box_y_position = []

up_pressed = False
down_pressed = False
left_pressed = False
right_pressed = False
collision = False
player_x = 50
player_y = 250
grid = []

# setting images
texture_car = arcade.load_texture("images/CPT_car.png")
texture_line = arcade.load_texture("images/CPT_finishline.png")
texture_box = arcade.load_texture("images/CPT_box.jpeg")
texture_crash = arcade.load_texture("images/CPT_crash.jpg")
texture_win = arcade.load_texture("images/CPT_win.jpg")
texture_trophy = arcade.load_texture("images/CPT_trophy.jpg")

# provide the random values to the boxes
for _ in range(25):
    x = random.randrange(525, finish)
    y = random.randrange(0, 475)

    box_x_position.append(x)
    box_y_position.append(y)


def on_update(delta_time):
    global up_pressed, down_pressed, left_pressed, right_pressed, player_x, player_y, finish, collision

    # control the player car by up and down key
    if up_pressed and player_y <= SCREEN_HEIGHT - 15:
        player_y += 5
    if down_pressed and player_y >= 15:
        player_y -= 5
    if left_pressed and player_x >= 25:
        player_x -= 3
    if right_pressed and player_x <= 475:
        player_x += 4

# ---------------------------------------------------------------------------------

    # check if the car collides with any of the boxes
    for index in range(len(box_x_position)):
        box_x_position[index] -= 4
        if ((box_x_position[index] - player_x) ** 2 + (box_y_position[index] - player_y) ** 2) <= 1550 and finish >= 50:
            collision = True
        if box_x_position[index] < -25:
            box_x_position[index] = random.randrange(525, 1475)
            box_y_position[index] = random.randrange(0, 475)
    finish -= 1




def on_draw():
    global player_x, player_y, finish, collision, texture_car, texture_line
    arcade.start_render()

    # drawing player, finish line, and boxed
    if finish >= 50:
        arcade.draw_texture_rectangle(finish, 250, 100, 500, texture_line, 0)
        arcade.draw_texture_rectangle(player_x, player_y, 80, 50, texture_car, 0)
        for x, y in zip(box_x_position, box_y_position):
            arcade.draw_texture_rectangle(x, y, 35, 35, texture_box, 0)

    # end the game if it collides with box
    if collision == True and finish > 50:
        arcade.draw_rectangle_filled(250, 250, 500, 500, arcade.color.WHITE)
        arcade.draw_texture_rectangle(250, 275, 500, 500, texture_crash, 0)
        arcade.draw_text("Game Over", 110, 250, arcade.color.BLACK, 35)

    # end the game if it reaches the finish line
    elif collision == False and finish <= 50:
        arcade.draw_rectangle_filled(250, 250, 500, 500, arcade.color.WHITE)
        arcade.draw_texture_rectangle(250, 400, 500, 300, texture_win, 0)
        arcade.draw_texture_rectangle(250, 120, 150, 150, texture_trophy, 0)
        arcade.draw_text("You Win!", 120, 250, arcade.color.BLACK, 40)



def on_key_press(key, modifiers):
    global up_pressed, down_pressed, left_pressed, right_pressed
    if key == arcade.key.UP:
        up_pressed = True
    if key == arcade.key.DOWN:
        down_pressed = True
    if key == arcade.key.LEFT:
        left_pressed = True
    if key == arcade.key.RIGHT:
        right_pressed = True


def on_key_release(key, modifiers):
    global up_pressed, down_pressed, left_pressed, right_pressed
    if key == arcade.key.UP:
        up_pressed = False
    if key == arcade.key.DOWN:
        down_pressed = False
    if key == arcade.key.LEFT:
        left_pressed = False
    if key == arcade.key.RIGHT:
        right_pressed = False


def setup():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Car Racing Game")
    arcade.set_background_color(arcade.color.ANTI_FLASH_WHITE)
    arcade.schedule(on_update, 1/60)


    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


if __name__ == '__main__':
    setup()