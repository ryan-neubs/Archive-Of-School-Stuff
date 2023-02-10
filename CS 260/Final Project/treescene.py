# house1scene.py

from ren3d.scenedef import *

camera.set_perspective(30, 1.3333, 5)
camera.set_view((30, 15, 30), (0, 0, -10))

scene.background = (.05, .05, .2)
scene.set_light(pos=(-30, 50, 5), color=(.8, .8, .8))
scene.add_light(pos=(0, 5, 5), color=(.3, .4, .4))
scene.ambient = (.5, .5, .5)
scene.shadows = True

scene.add(Box(pos=(0, -3, -10), size=(18, 1, 18), color=(0.4, 1.0, 0.4))) # Grass Plate

scene.add(Box(pos=(0, -2, -10), size=(1, 4, 1), color=(0.23, 0.15, 0.05))) # Log
scene.add(Box(pos=(0, 1, -10), size=(5, 2, 5), color=(0.13,0.54,0.13))) # Leaves
scene.add(Box(pos=(0, 3, -10), size=(1, 2, 1), color=(0.13,0.54,0.13)))
scene.add(Box(pos=(-1, 3, -10), size=(1, 2, 1), color=(0.13,0.54,0.13)))
scene.add(Box(pos=(1, 3, -10), size=(1, 2, 1), color=(0.13,0.54,0.13))) 
scene.add(Box(pos=(0, 3, -9), size=(1, 2, 1), color=(0.13,0.54,0.13))) 
scene.add(Box(pos=(0, 3, -11), size=(1, 2, 1), color=(0.13,0.54,0.13))) 



