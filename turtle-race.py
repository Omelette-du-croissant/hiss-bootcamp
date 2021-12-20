import turtle as t
import random

screen = t.Screen()
screen.setup(width=500, height=400)

steven = t.Turtle()
steven.color('black')
style = ('Calibri', 30, 'italic')
steven.write('Welcome to Turtle Race!', font=style, align="center")
steven.hideturtle()

user_bet = screen.textinput(title="Make a bet!", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "blue", "green", "violet", "yellow"]
y_pos = [80, 50, 20, -10, -40, -70]
print(user_bet)

turtle_list = []

for turtle_ind in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_ind])
    new_turtle.goto(x=-230, y=y_pos[turtle_ind])
    turtle_list.append(new_turtle)

if user_bet:
    is_racing = True
    steven.clear()

while is_racing:
    for turtle in turtle_list:
        if turtle.xcor() > 200:
            is_racing = False
            win_color = turtle.pencolor()
            if win_color == user_bet.lower():
                style = ('Calibri', 15, 'italic')
                print(f"You win! The {win_color} turtle is the winner.")
                steven.write(f"You win! The {win_color} turtle is the winner.", font=style, align="center")
            else:
                style = ('Calibri', 15, 'italic')
                steven.write(f"You lose! The {win_color} turtle is the winner.", font=style, align="center")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
