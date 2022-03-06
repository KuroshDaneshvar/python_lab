import turtle

#function for draw oval

def draw_oval(turtle,rad):
      for i in range(2):
        # two arcs
        turtle.circle(rad,90)
        turtle.circle(rad//2,90)

#create turtle

win=turtle.Screen()
laki=turtle.Turtle()
laki.hideturtle()

laki.seth(-45)

#paint the shape and call function

laki.begin_fill()

draw_oval(laki,170)

laki.fillcolor('red')

laki.end_fill()



win.mainloop()
