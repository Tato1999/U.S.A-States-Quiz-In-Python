import turtle
import pandas
screen = turtle.Screen()
image = "/Users/programing/Desktop/programing/us-states-game-start/blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("/Users/programing/Desktop/programing/us-states-game-start/50_states.csv")
correct_states = []
counter = 0
game_on = True

while game_on:
    false_counter = 0
    ans = screen.textinput(title=f"Guess State {len(correct_states)}/50", prompt="What is next State?").title()
    counter = -1
    if ans == "Exit":
        game_on = False
    else:  
        for i in data["state"]:
            counter += 1
            if ans == i:
                correct_states.append(i)
                corX = data[data["state"] == i].x
                corY = data[data["state"] == i].y
                answer = turtle.Turtle()
                answer.penup()
                answer.goto(corX[counter],corY[counter])
                answer.hideturtle()
                answer.write(f"{ans}",font=('Arial', 12, 'normal'))
            else:
                false_counter += 1
                if false_counter == 50:
                    answer = turtle.Turtle()
                    game_on = False
                    answer.hideturtle()
                    answer.color("red")
                    answer.write(f"Wrong, You Lose",align = "center", font=('Arial', 30, 'normal'))
                    
        
    if len(correct_states) == 50:
            answer.write(f"Congrats You Win",align = "center", font=('Arial', 30, 'normal'))
            break
      
        

# def get_cor(x,y):
#     print(x,y)

# screen.onscreenclick(get_cor)
turtle.mainloop()









