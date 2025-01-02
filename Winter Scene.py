import turtle

screen= turtle.Screen()
screen.screensize(800,800)
screen.bgcolor("lightsteelblue")

t=turtle.Turtle()
t_ground= turtle.Turtle()
t_ground.speed(0)
t.speed(0)

t_ground.pencolor('white')
t_ground.fillcolor("white")
t_ground.penup()
t_ground.goto(-1000,-100)
t_ground.pendown()
t_ground.begin_fill()
t_ground.goto(1000,-100)
t_ground.goto(1000,-1000)
t_ground.goto(1000,-1000)
t_ground.goto(-1000,-1000)
t_ground.end_fill()
t.penup()
t.goto(0,0)
t.end_fill()






# tree top tri
t.goto(0,50)
t.fillcolor("green")
t.pendown()
t.begin_fill()
t.goto(-40,10)
t.goto(40,10)
t.goto(0,50)
t.penup()
t.end_fill()


#second tri
t.goto(0,25)
t.fillcolor("green")
t.pendown()
t.begin_fill()
t.goto(-60,-25)
t.goto(60,-25)
t.goto(0,25)
t.penup()
t.end_fill()




#third tri
t.goto(0,0)
t.fillcolor("green")
t.pendown()
t.begin_fill()
t.goto(-80,-70)
t.goto(80,-70)
t.goto(0,0)
t.end_fill()

#stump
t.penup()
t.fillcolor("brown")
t.goto(-5,-70)
t.pendown()
t.begin_fill()
t.goto(5,-70)
t.goto(5,-100)
t.goto(-5,-100)
t.goto(-5,-70)
t.end_fill()
t.penup()

t.goto(-40,10)
t.circle(3)
t.end_fill()


#house
t.goto(100,-100)


t.pendown()



t.goto(270,-100)
t.goto(270,50)
t.goto(100,50)
t.goto (100,-100)
t.goto(100,50)
t.goto(185,150)
t.goto(270,50)



#door
t.penup()
t.goto(170,-100)
t.pendown()
t.fillcolor("brown")
t.begin_fill
t.goto(170,0)
t.goto(210,0)
t.goto(210,-100)
t.end_fill
t.penup()

#wreath
t.goto(205,-25)
t.pendown()
t.setheading(90)
t.pencolor("green")
t.begin_fill()
t.circle(15)
t.end_fill()
t.penup()
t.goto(198,-25)
t.pendown()
t.fillcolor("lightsteelblue")
t.begin_fill()
t.circle(7)
t.end_fill()
t.penup()
#door nob
t.goto(207,-50)
t.pendown()
t.setheading(90)
t.fillcolor("black")
t.begin_fill()
t.circle(5)
t.end_fill()

#snowman
t.penup()
t.goto(-135,-120)
t.fillcolor("white")
t.pendown()
t.begin_fill()
t.setheading(90)
t.circle(45)
t.end_fill()

t.penup()

#second circle
t.goto(-140,-60)
t.fillcolor("white")
t.pendown()
t.begin_fill()
t.setheading(90)
t.circle(38)
t.end_fill()

t.penup()

#snowman head
t.goto(-147,0)
t.fillcolor("white")
t.pendown()
t.begin_fill()
t.setheading(90)
t.circle(28)
t.end_fill()
t.penup()

#writing
t.goto(0,150)
t.pendown()
t.write("Merry Christmas!",font=("arial",30,"bold"),align="center")
t.penup()


#left arm
t.goto(-216,-60)
t.pendown()
t.goto(-236,-40)




#right arm
t.penup()
t.goto(-140,-60)
t.pendown()
t.goto(-120,-40)
t.penup()

#presents
t.goto(10,-100)
t.fillcolor("red")
t.begin_fill()
t.forward(25)
t.right(90)
t.forward(25)
t.right(90)
t.forward(25)
t.right(90)
t.forward(25)
t.right(25)
t.end_fill()

t.penup()
t.goto(22,-100)
t.pendown()
t.goto(22,-75)

#present details
t.penup()
t.goto(10,-87)
t.pencolor("green")
t.pendown()
t.begin_fill()
t.goto(34,-87)
t.end_fill()

t.penup()
t.goto(10,-87)
t.pencolor("green")
t.pendown()
t.begin_fill()
t.goto(34,-87)
t.end_fill()




t.hideturtle()






#LAST LINE OF CODE
turtle.done()





