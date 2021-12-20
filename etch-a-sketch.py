import turtle as t

steven = t.Turtle()
screen = t.Screen()

def move_fwd():
    steven.forward(10)

def move_bcw():
    steven.backward(10)

def move_left():
    steven.left(10)

def move_right():
    steven.right(10)

def clear():
    steven.clear()
    steven.penup()
    steven.home()
    steven.pendown()




screen.listen()
screen.onkey(key="w", fun=move_fwd)
screen.onkey(key="s", fun=move_bcw)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
