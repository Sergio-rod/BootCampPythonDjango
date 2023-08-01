import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.setup(725, 495)
screen.addshape(image)

turtle.shape(image)
data = pd.read_csv('50_states.csv')
state_names = data.state.str.lower()

game_on = True

while game_on:

    answer_state = screen.textinput(title='Choose a state', prompt='What`s the state name?')
    answer_state = answer_state.lower()

    if len(data[state_names == answer_state]) > 0:
        xcor = data[state_names == answer_state].x.iloc[0]
        ycor = data[state_names == answer_state].y.iloc[0]

        new = turtle.Turtle()
        new.penup()
        new.goto(xcor, ycor)
        new.write(data[state_names == answer_state].state.iloc[0])
        new.hideturtle()
        new.speed('fastest')

    else:
        print('nel')



# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

