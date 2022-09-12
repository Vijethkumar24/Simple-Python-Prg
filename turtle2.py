import turtle
wn = turtle.Screen()       
wn.setup(540,508)           

alex = turtle.Turtle()     
alex.shape("turtle")       
alex.color("blue")         
vdestination="south"
alex.right(60)
alex.forward(50);
destination="north"
alex.left(60)
alex.forward(60);
destination="east"
alex.forward(60);
destination="west"
alex.backward(60);
destination="invalid"
alex.write("invalid distination")

                        