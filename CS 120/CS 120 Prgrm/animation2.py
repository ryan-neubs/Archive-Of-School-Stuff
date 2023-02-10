# animation2.py

# multiple-shot cannonball animation

from math import sqrt, sin, cos, radians, degrees
from graphics import *
from projectile import Projectile
from random import *

class Launcher:

    def __init__(self, win):
        """Create inital launcher with angle 45 degrees and velocity 40
        win is the GraphWin to draw the launcher in.
        """
        
        # draw the base shot of the launcher
        base = Circle(Point(0,0), 1.5)
        base.setFill("red")
        base.setOutline("red")
        base.draw(win)

        # save the window and create initial angle and velocity
        self.win = win
        self.angle = radians(45.0)
        self.vel = 40.0
        
        # create inital "dummy" arrow
        self.arrow = Line(Point(0,0), Point(0,0)).draw(win)
        # replace it with the correct arrow
        self.redraw()

        
    def redraw(self):
        """undraw the arrow and draw a new one for the
        current values of angle and velocity.
        """
        
        self.arrow.undraw()
        pt2 = Point(self.vel*cos(self.angle), self.vel*sin(self.angle))
        self.arrow = Line(Point(0,0), pt2).draw(self.win)
        self.arrow.setArrow("last")
        self.arrow.setWidth(3)

        
    def adjAngle(self, amt):
        """ change angle by amt degrees """
        
        self.angle = self.angle+radians(amt)
        self.redraw()

        
    def adjVel(self, amt):
        """ change velocity by amt"""
        
        self.vel = self.vel + amt
        self.redraw()

    def fire(self):
        return ShotTracker(self.win, degrees(self.angle), self.vel, 0.0)
  

class ShotTracker:

    """ Graphical depiction of a projectile flight using a Circle """

    def __init__(self, win, angle, velocity, height):
        """win is the GraphWin to display the shot, angle, velocity, and
        height are initial projectile parameters.
        """
        
        self.proj = Projectile(angle, velocity, height)
        self.marker = Circle(Point(0,height), 1.5)
        self.marker.setFill("red")
        self.marker.setOutline("red")
        self.marker.draw(win)

        
    def update(self, dt):
        """ Move the shot dt seconds farther along its flight """
        
        self.proj.update(dt)
        center = self.marker.getCenter()
        dx = self.proj.getX() - center.getX()
        dy = self.proj.getY() - center.getY()
        self.marker.move(dx,dy)

        
    def getX(self):
        """ return the current x coordinate of the shot's center """
        return self.proj.getX()

    def getY(self):
        """ return the current y coordinate of the shot's center """
        return self.proj.getY()

    def undraw(self):
        """ undraw the shot """
        self.marker.undraw()

class Target:

    def __init__(self, win):
        self.center = Point(randrange(-105, 105), randrange(90,150))
        self.hit1 = Circle(self.center, 8)
        self.hit2 = Circle(self.center, 5)
        self.hit3 = Circle(self.center, 2)
        self.hit1.draw(win)
        self.hit2.draw(win)
        self.hit3.draw(win)
        self.hit1.setFill("blue")
        self.hit2.setFill("red")
        self.hit3.setFill("yellow")
        self.vel = 1

    def hit_by(self, shot):
        #returns boolean if shot hits boolean
        shotx = shot.getX()
        shoty = shot.getY()
        centerx = self.center.getX()
        centery = self.center.getY()
        return 64 >= ((centerx - shotx) ** 2 + (centery - shoty) ** 2)
        
    def destroy(self):
        self.hit1.undraw()
        self.hit2.undraw()
        self.hit3.undraw()

    def update(self):
        if self.center.getX() == 110:
            self.vel = -(self.vel)
       
        elif self.center.getX() == -110:
            self.vel = -(self.vel)
        
        self.center.move(self.vel, 0)
        self.hit1.move(self.vel,0)
        self.hit2.move(self.vel,0)
        self.hit3.move(self.vel,0)
            

        
class ProjectileApp:

    def __init__(self):
        self.win = GraphWin("Projectile Animation", 640, 480)
        self.win.setCoords(-110, -10, 110, 155)

        self.launcher = Launcher(self.win)
        self.shots = []

        self.target = Target(self.win)

    def updateShots(self, dt):
        alive = []
        for shot in self.shots:
            shot.update(dt)
            if shot.getY() >= 0 and shot.getX() < 210:
                alive.append(shot)
            else:
                shot.undraw()
        self.shots = alive

    def checkForHit(self):
        alive = []
        for shot in self.shots:
            if self.target.hit_by(shot):
                shot.undraw()
                self.target.destroy()
                self.target = Target(self.win)
            else:
                alive.append(shot)
            self.shots = alive

    def run(self):
        
        # main event/animation lopp
        while True:
            self.updateShots(1/10)
            self.checkForHit()
            self.target.update()
            key = self.win.checkKey()
            if key in ["q", "Q"]:
                break

            if key == "Left":
                self.launcher.adjAngle(5)
            elif key == "Right":
                self.launcher.adjAngle(-5)
            elif key == "Up":
                self.launcher.adjVel(5)
            elif key == "Down":
                self.launcher.adjVel(-5)
            elif key == "f":
                self.shots.append(self.launcher.fire())
           
            update(30)
            
        self.win.close()
           

if __name__ == "__main__":
    ProjectileApp().run()
