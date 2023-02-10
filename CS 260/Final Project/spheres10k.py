# manysphere.py

from random import random, seed
from ren3d.scenedef import *

n = 10000
maxrad = 4

seed(5)  # same random numbers for every run


def rfloat(low, high):
    return (high-low)*random()+low


for r in range(n):
    pos = [rfloat(-100, 100) for i in range(3)]
    radius = random()*maxrad
    mat = Material((random()*.4, random()*.4, random()*.4))
    mat.reflect = (.5, .5, .5)
    s = Sphere(pos=pos, radius=radius, color=mat)
    scene.add(s)

#scene.setLight((-200, 150, 150), (0,0,0))

camera.set_view((0, 0, 0), (0, 0, -1))
camera.set_perspective(45, 4./3., 5)

scene.set_light((0, 0, 0), (.5, .5, .5))
scene.add_light((0, 200, 0), (.5, .5, .5))
scene.add_light((200, 0, 0), (.5, .5, .5))

scene.reflections = 3
scene.shadows = True
scene.ambient = (.2, .2, .2)
# scene.setBackground((.4,0,0))
#scene.surface = scene.surface.getBVH()
