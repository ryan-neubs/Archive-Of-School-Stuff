# gradientscene.py

# draws 2 series of boxes with increments and decrements to rgb values creating color gradients

from random import random
from ren3d.scenedef import *

camera.set_perspective(30, 1.3333, 5)
scene.background = (.8, .8, .7)

# Red to blue gradient
redval = 1
xpos = 3.8
blueval = 0
for i in range(20):
    scene.add(Box(pos=(xpos, -2, -20), size=(2, 2, 2), color=(redval, 0, blueval)))
    xpos -= 0.4
    redval -= 0.05
    blueval += 0.05

# Red to green gradient
blueval = 0
redval = 1
xpos = 3.8
greenval = 0
for i in range(20):
    scene.add(Box(pos=(xpos, 2, -20), size=(2, 2, 2), color=(redval, greenval, 0)))
    xpos -= 0.4
    redval -= 0.05
    greenval += 0.05
