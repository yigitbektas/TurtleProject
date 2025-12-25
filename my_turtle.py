import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Turtle Application")

turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(100)

def turtle_backward():
    turtle_instance.backward(100)

def turtle_left():
    turtle_instance.left(100)
    #turtle_instance.setheading(turtle_instance.heading()+10)

def turtle_right():
    turtle_instance.right(100) #bununla direkt sağ 100 derece olarak yonu degisir
    # turtle_instance.setheading(turtle_instance.heading()-10) bununla mevcut açı yönüne göre -10 right yapar

def clear_screen():
    turtle_instance.clear()

def turtle_return_home():
    turtle_instance.home()

def turtle_penup():
    turtle_instance.penup()

def turtle_pendown():
    turtle_instance.pendown()

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward, key="Up")
drawing_board.onkey(fun=turtle_backward, key="Down")
drawing_board.onkey(fun=turtle_right, key="Right")
drawing_board.onkey(fun=turtle_left, key="Left")
drawing_board.onkey(fun=clear_screen, key="c")
drawing_board.onkey(fun=turtle_return_home, key="h")
drawing_board.onkey(fun=turtle_penup, key="w")
drawing_board.onkey(fun=turtle_pendown, key="s")

turtle.mainloop()