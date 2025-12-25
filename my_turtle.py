import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Turtle Application")

turtle_instance = turtle.Turtle()

drawing_board.textinput("NAME", "Name of first player:")
turtle_instance.shape("turtle")
turtle.write("Welcome = ", True, align="left", font=("Arial", 24, "bold"))
turtle.write((0,0), True)

turtle.mainloop()