import turtle as t
import pandas as pd

#csv & img on ipad

screen = t.Screen()
screen.title("US States Quiz")

image = "blank_states_img.gif"
screen.addshape(image)

t.shape(image)

df = pd.read_csv("50_states.csv")

df_states = df.state
df_x = df.x
df_y = df.y

states = pd.Series.tolist(df_states)

#print(type(states))

print(df["state"])

guessed_states = []

while len(guessed_states) < len(states):
  guess_state = screen.textinput(title=f"{len(guessed_states)}/{len(states)} states guessed.", prompt="Enter a state.").title()

  if guess_state == "Exit":
    missing_states = []
    for state in states:
      if state not in guessed_states:
        missing_states.append(state)
    df2 = pd.DataFrame(missing_states)
    df2.to_csv("to-do")
    
  if guess_state in states:
    steven = t.Turtle()
    steven.hideturtle()
    steven.penup()
    state_input = df[df.state == guess_state]
    steven.goto(x = float(state_input.x), y = float(state_input.y))
    steven.write(guess_state)
    guessed_states.append(guess_state)

