import turtle
import pandas

# Set up the screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read from CSV and get the state names
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()



# # Main game loop
# while True:
#     answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
#     if not answer_state:
#         break
#
#     # Convert the guess to title case
#     guess = answer_state.title()
#     print(guess)
#
#     # Check if the guess is among the 50 states
#     if guess in states:
#         print("Correct!")
#         # Optionally, you can add logic here to mark the state on the map
#     else:
#         print("Not valid, try again.")
#
#
# #write correct guesses onto map
#
# #use a for loop to allow the user to keep guessing
# for attempt in range:
#     try:
#         guess = screen.textinput(title="Guess the State", prompt="What's another state's name?")
#         if guess != states:
#             print("Incorrect, try again.")
#         else:
#             print("Good, you guessed a state.")
#             break
# #record correct guesses in a list
#
# #keep track of the score
#
#


