import turtle

def draw(turtle,sides,len):
    
    for _ in range(sides):
        turtle.forward(len)
        turtle.left(360/sides)


win=turtle.Screen()
t=turtle.Turtle()
t.speed(1)

a=int(input("please enter number of sides"))
b=int(input("please enter len of sides"))

draw(t,a,b)

win.mainloop()