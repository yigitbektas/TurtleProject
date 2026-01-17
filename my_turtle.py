import turtle
import random

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Turtle Application")
FONT = ('Arial', 25, 'normal')
grid_size = 10
x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [-20, -10, 0, 10, 20]
turtle_list = []
score = 0
game_over = False

#Score
turtle_score = turtle.Turtle()

turtle_countdown = turtle.Turtle()

def setup_score_turtle():
    turtle_score.hideturtle()
    turtle_score.penup()
    turtle_score.color("red")

    top_height = drawing_board.window_height() / 2
    y = top_height * 0.8

    turtle_score.goto(0,y)
    turtle_score.write("Score: 0", False, align="center", font=FONT)

#welcome

def welcome_message_turtle():
    username = drawing_board.textinput("NAME", "Name of first player:")
    turtle_welcome = turtle.Turtle()
    turtle_welcome.hideturtle()
    turtle_welcome.penup()
    turtle_welcome.color("dark blue")

    top_height = drawing_board.window_height() / 2
    y = top_height * 0.9

    turtle_welcome.goto(0,y)
    turtle_welcome.write(f"Welcome {username}!", False, align="center", font=FONT)


def make_turtle(x,y):
    t=turtle.Turtle()

    def handle_click(x,y):
        global score
        score += 1
        turtle_score.clear()
        turtle_score.write(f"Score: {score}", False, align="center", font=FONT)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.color("green")
    t.shapesize(2,2)
    t.goto(x* grid_size,y * grid_size)
    turtle_list.append(t)


def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

#recursive function
def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        drawing_board.ontimer(show_turtles_randomly, 500)

def countdown(time):
    global game_over
    turtle_countdown.hideturtle()
    turtle_countdown.penup()
    turtle_countdown.color("white")

    top_height = drawing_board.window_height() / 2
    top_width = drawing_board.window_width() / 2
    y = top_height * 0.8
    x = top_width * 0.9
    turtle_countdown.goto(x, y)
    turtle_countdown.clear()


    if time > 0:
        turtle_countdown.clear()
        turtle_countdown.write(f"Time: {time}", False, align="right", font=FONT)
        drawing_board.ontimer(lambda: countdown(time - 1), 500)
    else:
        game_over = True
        turtle_countdown.clear()
        turtle_countdown.hideturtle()
        turtle_countdown.write("GAME OVER", False, align="right", font=FONT)

def start_game_up():
    turtle.tracer(0)
    welcome_message_turtle()
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdown(10)
    turtle.tracer(1)

start_game_up()

turtle.mainloop()