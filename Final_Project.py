import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

ROW_COUNT = 5
COLUMN_COUNT = 1

WIDTH = 1500
HEIGHT = 100

MARGIN = 5

up_pressed = False
down_pressed = False
player_y = 250

grid = []


def on_update(delta_time):
    global up_pressed, down_pressed, player_y
    if up_pressed and player_y <= 400:
        player_y += 100
        up_pressed = False
    if down_pressed and player_y >= 100:
        player_y -= 100
        down_pressed = False


def on_draw():
    global player_y
    arcade.start_render()
    arcade.draw_circle_filled(50, player_y, 20, arcade.color.RED)
    if player_y > 550 or player_y < -50:
        player_y = 150


def on_key_press(key, modifiers):
    global up_pressed, down_pressed
    if key == arcade.key.UP:
        up_pressed = True
    if key == arcade.key.DOWN:
        down_pressed = True


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/60)

    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()