import arcade
import random

WIDTH = 640
HEIGHT = 480

player_x = 30
player_y = HEIGHT//2
player2_x = WIDTH - 30
player2_y = HEIGHT//2

ball_y = HEIGHT//2
ball_x = WIDTH//2
deltax = random.uniform(1.8, 2.1)
deltay = random.uniform(1.8, 2.1)
deltax, deltay = 6, 7
points, points2 = 0, 0

up_pressed = False
down_pressed = False
left_pressed = False
right_pressed = False

W_pressed = False
S_pressed = False

def on_update(delta_time):
    global player_x, player_y, player2_x, player2_y, ball_x, ball_y, deltax, deltay, points, points2
    arcade.set_background_color(arcade.color.BLACK)

    ball_y += deltay
    ball_x += deltax

    if ball_y < 10 or ball_y > HEIGHT - 10:
        if deltay < 2:
            deltay *= -1.1
        else:
            deltay *= -1
    if ball_x < 40 and ball_x> 10:
        if (player_y - 30 < ball_y) and player_y+30 > ball_y:
            deltax *= -1
        else:
            points2 += 1
            ball_x = WIDTH//2
            ball_y = HEIGHT//2
            deltax, deltay = random.choice([-1, 1])*(random.randint(5, 7)), random.choice([-1, 1])*random.randint(5, 7)
    
    if ball_x > WIDTH-40:
        if ball_x < WIDTH-40:
            points += 1
            ball_x = WIDTH//2
            ball_y = HEIGHT//2
            deltax, deltay = random.choice([-1, 1])*(random.randint(5, 7)), random.choice([-1, 1])*random.randint(5, 7)
            
        elif player2_y - 30 < ball_y and player2_y + 30 > ball_y:
            if deltax < 2:
                deltax *= -1.1
            else:
                deltax *= -1
        else:
            points += 1
            ball_x = WIDTH//2
            ball_y = HEIGHT//2
            deltax, deltay = random.choice([-1, 1])*(random.randint(5, 7)), random.choice([-1, 1])*random.randint(5, 7)
    

    if up_pressed and player_y < HEIGHT-35:
        player_y += 7.5
    if down_pressed and player_y > 35:
        player_y = player_y - 7.5
    if right_pressed and player_x < WIDTH-40 and False:
        player_x += 7.5
    if left_pressed and player_x > 30 and False:
        player_x = player_x - 7.5
    
    if W_pressed and player2_y < HEIGHT-35:
        player2_y += 7.5
    if S_pressed and player2_y > 35:
        player2_y -= 7.5

    



def on_draw():
    global player_x, player_y
    arcade.start_render()
    arcade.draw_rectangle_filled(player_x, player_y, 10, 60, arcade.color.BLUE)
    arcade.draw_rectangle_filled(player2_x, player2_y, 10, 60, arcade.color.BLUE)
    arcade.draw_circle_filled(ball_x, ball_y, 10, arcade.color.AERO_BLUE)
    text = "You have " + str(points) + " points"
    text2 = "You have " + str(points2) + " points"
    arcade.draw_line(WIDTH//2, 0, WIDTH//2, HEIGHT, arcade.color.RED, 5)
    arcade.draw_line(0, 0, 0, HEIGHT, arcade.color.RED, 10)
    arcade.draw_line(WIDTH, 0, WIDTH, HEIGHT, arcade.color.RED, 10)
    arcade.draw_line(0, HEIGHT, WIDTH, HEIGHT, arcade.color.RED, 10)
    arcade.draw_line(0, 0, WIDTH, 0, arcade.color.RED, 10)
    arcade.draw_text(text2, WIDTH//2 + 100, 20, arcade.color.TAN, 12)
    arcade.draw_text(text, WIDTH//2 -200, 20, arcade.color.TAN, 12)

        

def on_key_press(key, modifiers):
    global up_pressed, down_pressed, left_pressed, right_pressed, W_pressed, S_pressed
    if key == arcade.key.W:
        up_pressed = True
    if key == arcade.key.S:
        down_pressed = True
    if key == arcade.key.A:
        left_pressed = True
    if key == arcade.key.D:
        right_pressed = True
    
    if key == arcade.key.UP:
        W_pressed = True
    if key == arcade.key.DOWN:
        S_pressed = True


def on_key_release(key, modifiers):
    global up_pressed, down_pressed, left_pressed, right_pressed, W_pressed, S_pressed
    if key == arcade.key.W:
        up_pressed = False
    if key == arcade.key.S:
        down_pressed = False
    if key == arcade.key.A:
        left_pressed = False
    if key == arcade.key.D:
        right_pressed = False

    if key == arcade.key.UP:
        W_pressed = False
    if key == arcade.key.DOWN:
        S_pressed = False

def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "PING PONG", resizable=True)
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/60)
    
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


if __name__ == '__main__':
    setup()