import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)

turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
correct_answers = []
all_states = states_data.state.to_list()

while len(correct_answers) < 50:
    answer_state = (screen.textinput(title=f"{len(correct_answers)}/50 States Correct",
                                     prompt="What's another state name? ")).title()
    if answer_state == "Exit":
        states_to_learn = states_data[~states_data.state.isin(correct_answers)].state
        states_to_learn.to_csv("states_to_learn.csv")
        break
    if (answer_state in all_states) and (answer_state not in correct_answers):
        correct_answers.append(answer_state)
        answer_state_data = states_data[states_data.state == answer_state]
        new_state = turtle.Turtle()
        new_state.hideturtle()
        new_state.penup()
        new_state.goto(int(answer_state_data.x), int(answer_state_data.y))
        new_state.write(answer_state, align="center", font=("Arial", 8, "normal"))

screen.exitonclick()
