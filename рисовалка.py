import turtle
t= turtle.Turtle()
t.shape("turtle")
def house():
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(20)
    t.left(135)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(135)
    t.forward(22)
def gres():
    t.speed(10)
    t.color("blue")
    t.width(300)
    t.goto(350,0)
    t.goto(350,300)
    t.goto(-350,300)
    t.goto(-350,0)
    t.goto(0,0)
    t.goto(0,-240)
    t.color("sienna")
    t.width(400)
    t.goto(350,-240)
    t.goto(-350,-240)
    t.up()
    t.width(10)
    t.color("black")
    t.goto(0,0)
    t.down()
    t.speed(10)
    house()
    t.up()
    t.goto(-200,0)
    t.down()
    house()
    t.up()
    t.goto(200,0)
    t.down()
    house()
    t.speed(10)
    t.width(40)
    t.color("green")
    t.up()
    t.goto(-550,-25)
    t.down()
    t.goto(550,-25)
    t.goto(0,-25)
    t.color("black")




#gres()#

def kvadrat():
    for i in range(4):
        t.forward(100)
        t.left(90)

#kvadrat()#


def figyra(n):
    for i in range(n):
        t.forward(30)
        t.left(360/n)





def yzor(d):
    t.speed (8)
    for i  in  range(d):
        figyra(7)
        t.left(360/d)

#yzor(45)#





def up1():
    t.forward(10)
def down2():
    t.backward(10)
def left3():
    t.left(10)
def right4():
    t.right(10)
def red5():
    t.color("red")






















t.screen.onkeypress(left3,"Left")
t.screen.onkeypress(right4,"Right")
t.screen.onkeypress(down2,"Down")
t.screen.onkeypress(up1,"Up")
t.screen.onkeypress(red5,"m")
t.screen.listen()




































    














t.screen.mainloop()








































