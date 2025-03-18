###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("brickwall")

q1=codesters.Square(100,100,200,'white')
q2=codesters.Square(-100,100,200,'black')
q3=codesters.Square(-100,-100,200,'red')
q4=codesters.Square(100,-100,200,'blue')

s1=codesters.Sprite("super_timber",100,100)
s1.set_size(.15)
s2=codesters.Sprite("swim",-100,-100)
s2.set_size(.1)
s3=codesters.Sprite("Turkey-Bacon",100,-100)
s3.set_size(.1)
s4=codesters.Sprite("air_65",-100,100)
s4.set_size(.25)

codesters.Text("Roan McNae",100,180,"black")
codesters.Text("I like Robotics",-100,-180,"black")