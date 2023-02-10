# house1scene.py

from ren3d.scenedef import *

camera.set_perspective(30, 1.3333, 5)
camera.set_view((-4, 3, 5), (-3, 0, -20))

scene.background = (.05, .05, .2)
scene.set_light(pos=(-30, 50, 5), color=(.8, .8, .8))
scene.add_light(pos=(0, 5, 5), color=(.4, .4, .4))
scene.ambient = (.5, .5, .5)
scene.shadows = True