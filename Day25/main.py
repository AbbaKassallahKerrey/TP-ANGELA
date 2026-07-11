"""with open("weather_data.csv") as file:
    content = file.read()
    print(content)
"""
"""

import pandas   as pd
data = pd.read_csv("weather_data.csv")
print(data)
# Pour affciher le type de données
#print(type(data["temp"]))
data_dict=data.to_dict()
#print(data_dict)
list_data=data["temp"].to_list()
print(list_data)
# Pour afficher la moyenne de la température
print(f"La moyenne de la température est : {data['temp'].mean()}")

# Centre-pARK_SQUIRELL
data2=pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data2)
"""
import pandas as pd
import turtle
screen = turtle.Screen()

image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")

#answer_state = turtle.textinput(title="Guess the State", prompt="What's another state's name?").title()
#print(answer_state)
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_state = turtle.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

if answer_state in all_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    t.goto(int(state_data.x), int(state_data.y))
    t.write(answer_state)


def get_mouse_click_coor(x, y):
    print(x, y)
turtle.onscreenclick(get_mouse_click_coor)
screen.title("My Turtle Game")

turtle.mainloop()
#screen.exitonclick()
