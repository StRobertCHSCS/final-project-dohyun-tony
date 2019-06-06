import arcade, random

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
status = False
player_y = 250
grid = []


for _ in range(25):
    x = random.randrange(500, finish)
    y = random.randrange(0, 300)

    box_x_position.append(x)
    box_y_position.append(y)


def on_update(delta_time):
    global up_pressed, down_pressed, player_y, finish, status
    if up_pressed and player_y <= SCREEN_HEIGHT - 15:
        player_y += 5
    if down_pressed and player_y >= 15:
        player_y -= 5
    for index in range(len(box_x_position)):
        box_x_position[index] -= 5
        if ((box_x_position[index] - 50) ** 2 + (box_y_position[index] - player_y) ** 2) <= 1000:
            status = True
        if box_x_position[index] < -25:
            box_x_position[index] = random.randrange(500, 1475)
            box_y_position[index] = random.randrange(0, 475)
    finish -= 10




def on_draw():
    global player_y, finish, status
    arcade.start_render()
    if status == True and finish > 50:
        arcade.draw_rectangle_filled(250, 250, 500, 500, arcade.color.WHITE)
        arcade.draw_text("Game Over", 120, 250, arcade.color.BLACK, 40)
    elif status == False and finish <= 50:
        arcade.draw_rectangle_filled(250, 250, 500, 500, arcade.color.WHITE)
        arcade.draw_text("You Win!", 120, 250, arcade.color.BLACK, 40)
    else:
        arcade.draw_rectangle_filled(finish, 250, 50, 500, arcade.color.BLACK)
        arcade.draw_circle_filled(50, player_y, 20, arcade.color.RED)
        for x, y in zip(box_x_position, box_y_position):
            arcade.draw_rectangle_filled(x, y, 50, 50, arcade.color.BRICK_RED)


def on_key_press(key, modifiers):
    global up_pressed, down_pressed
    if key == arcade.key.UP:
        up_pressed = True
    if key == arcade.key.DOWN:
        down_pressed = True


def on_key_release(key, modifiers):
    global up_pressed, down_pressed
    if key == arcade.key.UP:
        up_pressed = False
    if key == arcade.key.DOWN:
        down_pressed = False


def setup():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/60)


    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


if __name__ == '__main__':
    setup()