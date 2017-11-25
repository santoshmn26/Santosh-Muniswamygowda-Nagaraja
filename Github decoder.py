# same code in python 3.6
import turtle
def drawans(answer):        # a function to handel the drawing
    t=turtle.Turtle()
    t.write(answer,font=(None,40,"bold"))   # drawing the answer using the turtle
    turtle.done()
x =int(input('Enter a number'))             #input for the first number
y= int(input('Enter the second number'))    #input for the second number
operation=input("Enter the operation")      #input for the operation symbol (+,-,/ or *)
if(operation=='+'):                         #if and else conditions for various symbols
    answer=x+y
    print(answer)
    drawans(answer)
    exit()
elif(operation=='-'):
    answer=x+y
    print(answer)
    drawans(answer)
    exit()
elif(operation=='*'):
    answer=x+y
    print(answer)
    drawans(answer)
    exit()
elif(operation=='/'):
    answer=x+y
    print(answer)
    drawans(answer)
    exit()
