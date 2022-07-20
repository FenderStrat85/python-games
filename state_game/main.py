
import pandas
import turtle
import string

from state_writing import State_Writing

screen = turtle.Screen()
screen.title('US States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

state_writing = State_Writing()

state_data = pandas.read_csv("50_states.csv")
state_names = state_data['state'].to_list()

correct_guess_list = []

game_is_on = True
while game_is_on: 
  user_guess = screen.textinput(f'{len(correct_guess_list)}/50 states correct', 'Guess a state: ')
  
  capitaliseGuess = string.capwords(user_guess)

  if capitaliseGuess == 'Exit':
    missing_states(state_names, correct_guess_list)
    break

  if capitaliseGuess in correct_guess_list:
    continue

  if capitaliseGuess in state_names:
    selected_state = state_data[state_data.state == capitaliseGuess]
    x_coor = int(selected_state.x)
    y_coor = int(selected_state.y)
    state_writing.write_state(x_coor, y_coor, capitaliseGuess)
    correct_guess_list.append(capitaliseGuess)
  
  if len(correct_guess_list) == 50:
    state_writing.game_over()



  def missing_states(full_list, user_guesses):
    states_to_learn = [state for state in full_list if state not in user_guesses]
    data = pandas.DataFrame(states_to_learn)
    data.to_csv('states_to_learn.csv')

# Alternative to screenexitonclick
# Screen will not close on click
turtle.mainloop()
