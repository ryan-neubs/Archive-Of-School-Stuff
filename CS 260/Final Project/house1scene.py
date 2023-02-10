# house1scene.py

from ren3d.scenedef import *

camera.set_perspective(30, 1.3333, 5)
camera.set_view((30, 10, 30), (0, 0, -10))

scene.background = (.05, .05, .2)
scene.set_light(pos=(-30, 50, 5), color=(.8, .8, .8))
scene.add_light(pos=(0, 5, 5), color=(.3, .4, .4))
scene.ambient = (.5, .5, .5)
scene.shadows = True

#wood color: 0.7,0.54,0.32
scene.add(Box(pos=(0, -3, -10), size=(18, 1, 18), color=(0.4, 1.0, 0.4))) # Grass Plate

scene.add(Box(pos=(0, -2, -10), size=(5, 1, 5), color=(0.5, 0.5, 0.5))) # Stone Base

scene.add(Box(pos=(-2, 0, -8), size=(1, 3, 1), color=(0.5,0.5,0.5))) # Stone Pillars
scene.add(Box(pos=(2, 0, -8), size=(1, 3, 1), color=(0.5,0.5,0.5)))
scene.add(Box(pos=(-2, 0, -12), size=(1, 3, 1), color=(0.5,0.5,0.5)))
scene.add(Box(pos=(2, 0, -12), size=(1, 3, 1), color=(0.5,0.5,0.5)))

scene.add(Box(pos=(0, 2, -10), size=(5, 1, 5), color=(0.23, 0.15, 0.05))) # Log Top

scene.add(Box(pos=(1, 0,-8), size=(1,4,1), color=(0.7,0.54,0.32))) # Front Door
scene.add(Box(pos=(-1, 0,-8), size=(1,4,1), color=(0.7,0.54,0.32)))
scene.add(Box(pos=(0, 1,-8), size=(1,1,1), color=(0.7,0.54,0.32)))

scene.add(Box(pos=(1, 0, -12), size=(1,4,1), color=(0.7,0.54,0.32))) # Back Window
scene.add(Box(pos=(-1, 0, -12), size=(1,4,1), color=(0.7,0.54,0.32)))
scene.add(Box(pos=(0, 1,-12), size=(1,1,1), color=(0.7,0.54,0.32)))
scene.add(Box(pos=(0, -1,-12), size=(1,1,1), color=(0.7,0.54,0.32)))

scene.add(Box(pos=(-2, 0, -9), size=(1, 4, 1), color=(0.7,0.54,0.32))) # Left Wall
scene.add(Box(pos=(-2, 0, -11), size=(1, 4, 1), color=(0.7,0.54,0.32)))
scene.add(Box(pos=(-2, 1,-10), size=(1,1,1), color=(0.7,0.54,0.32)))
scene.add(Box(pos=(-2, -1,-10), size=(1,1,1), color=(0.7,0.54,0.32)))

scene.add(Box(pos=(2, 0, -9), size=(1, 4, 1), color=(0.7,0.54,0.32))) # Right Wall
scene.add(Box(pos=(2, 0, -11), size=(1, 4, 1), color=(0.7,0.54,0.32)))
scene.add(Box(pos=(2, 1,-10), size=(1,1,1), color=(0.7,0.54,0.32)))
scene.add(Box(pos=(2, -1,-10), size=(1,1,1), color=(0.7,0.54,0.32)))

scene.add(Box(pos=(0, -2.25, -7), size=(1, 0.5, 1), color=(0.5, 0.5, 0.5))) # Stone Steps
scene.add(Box(pos=(0, -1.75, -7.25), size=(1, 0.5, 0.5), color=(0.5, 0.5, 0.5)))


