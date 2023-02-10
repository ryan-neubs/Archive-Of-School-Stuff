Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
lambda p1,p2,p3: abs((p1[0] * (p3[1]-p2[1]) + p3[0] * (p2[1]-p1[1]) + p2[0] * (p1[1]-p3[1]))/2)

area = lambda p1,p2,p3: abs((p1[0] * (p3[1]-p2[1]) + p3[0] * (p2[1]-p1[1]) + p2[0] * (p1[1]-p3[1]))/2)

p1 = tuple([0,2])
p2 = tuple([2, 4])
p3 = tuple([6,5])
for i in range(n):
        p = tuple([randint(150,350), randint(150,350)])
        points.append(p)
        point = Point(p[0], p[1])
        point.draw(win)

from graphics import *
for i in range(n):
        p = tuple([randint(150,350), randint(150,350)])
        points.append(p)
        point = Point(p[0], p[1])
        point.draw(win)

n = 40

from random import randint
for i in range(n):
        p = tuple([randint(150,350), randint(150,350)])
        points.append(p)
        point = Point(p[0], p[1])
        point.draw(win)

        
Traceback (most recent call last):
  File "<pyshell#17>", line 3, in <module>
    points.append(p)

>>> points = []
>>> for i in range(n):
        p = tuple([randint(150,350), randint(150,350)])
        points.append(p)
        point = Point(p[0], p[1])
        point.draw(win)

        
Traceback (most recent call last):
  File "<pyshell#20>", line 5, in <module>
    point.draw(win)
NameError: name 'win' is not defined
>>> win = GraphWin("Quickhull", 520, 520)
    win.setCoords(-10, -10, 510, 510)
    
SyntaxError: multiple statements found while compiling a single statement
>>> win = GraphWin("Quickhull", 520, 520)
>>> win.setCoords(-10, -10, 510, 510)
>>> for i in range(n):
        p = tuple([randint(150,350), randint(150,350)])
        points.append(p)
        point = Point(p[0], p[1])
        point.draw(win)

        
Point(284.0, 236.0)
Point(285.0, 227.0)
Point(325.0, 276.0)
Point(243.0, 265.0)
Point(209.0, 345.0)
Point(215.0, 208.0)
Point(253.0, 214.0)
Point(336.0, 222.0)
Point(321.0, 311.0)
Point(185.0, 239.0)
Point(202.0, 197.0)
Point(231.0, 329.0)
Point(166.0, 154.0)
Point(222.0, 294.0)
Point(193.0, 170.0)
Point(309.0, 224.0)
Point(150.0, 171.0)
Point(262.0, 227.0)
Point(170.0, 339.0)
Point(287.0, 342.0)
Point(318.0, 347.0)
Point(241.0, 201.0)
Point(298.0, 200.0)
Point(250.0, 195.0)
Point(183.0, 187.0)
Point(276.0, 221.0)
Point(152.0, 281.0)
Point(237.0, 324.0)
Point(320.0, 336.0)
Point(252.0, 215.0)
Point(225.0, 323.0)
Point(310.0, 209.0)
Point(316.0, 320.0)
Point(163.0, 317.0)
Point(172.0, 298.0)
Point(340.0, 154.0)
Point(208.0, 203.0)
Point(294.0, 186.0)
Point(321.0, 172.0)
Point(251.0, 242.0)
>>> points.sort()
>>> points
[(150, 171), (152, 281), (163, 317), (166, 154), (170, 339), (172, 298), (183, 187), (185, 239), (193, 170), (202, 197), (208, 203), (209, 345), (215, 208), (222, 294), (225, 323), (231, 329), (237, 324), (241, 201), (242, 212), (243, 265), (250, 195), (251, 242), (252, 215), (253, 214), (262, 227), (276, 221), (284, 236), (285, 227), (287, 342), (294, 186), (298, 200), (309, 224), (310, 209), (316, 320), (318, 347), (320, 336), (321, 172), (321, 311), (325, 276), (336, 222), (340, 154)]
>>> p1 = min(points)
>>> pn = max(points)
>>> line = Line(Point(p1[0], p1[1]), Point(pn[0], pn[1]))
>>> line.draw(win)
Line(Point(150.0, 171.0), Point(340.0, 154.0))
>>> half = [p for p in s if determ(p1, pn, p) > 0]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    half = [p for p in s if determ(p1, pn, p) > 0]
NameError: name 's' is not defined
>>> half = [p for p in points if determ(p1, pn, p) > 0]
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    half = [p for p in points if determ(p1, pn, p) > 0]
  File "<pyshell#33>", line 1, in <listcomp>
    half = [p for p in points if determ(p1, pn, p) > 0]
NameError: name 'determ' is not defined
>>> def determ(p1, p2, p3):
    p1x, p1y = p1 #A
    p2x, p2y = p2 #C
    p3x, p3y = p3 #B

    #area = abs((p1x * (p3y-p2y) + p3x * (p2y-p1y) + p2x * (p1y-p3y))/2) - Will give pmax (not sure where to use yet)
    return (p1x * p2y) + (p3x * p1y) + (p2x * p3y) - (p3x * p2y) - (p2x * p1y) - (p1x * p3y)

>>> half = [p for p in points if determ(p1, pn, p) > 0]
>>> half
[(152, 281), (163, 317), (170, 339), (172, 298), (183, 187), (185, 239), (193, 170), (202, 197), (208, 203), (209, 345), (215, 208), (222, 294), (225, 323), (231, 329), (237, 324), (241, 201), (242, 212), (243, 265), (250, 195), (251, 242), (252, 215), (253, 214), (262, 227), (276, 221), (284, 236), (285, 227), (287, 342), (294, 186), (298, 200), (309, 224), (310, 209), (316, 320), (318, 347), (320, 336), (321, 172), (321, 311), (325, 276), (336, 222)]
>>> for point in half:
	p = Point(p[0],p[1])
	p.setFill("blue")

	
Traceback (most recent call last):
  File "<pyshell#41>", line 2, in <module>
    p = Point(p[0],p[1])
TypeError: 'Point' object is not subscriptable
>>> for x in half:
	p = Point(x[0], x[1])
	p.setFill('blue')

	
>>> for x in half:
	p = Point(x[0], x[1])
	p.draw(win)
	p.setFill('blue')

	
Point(152.0, 281.0)
Point(163.0, 317.0)
Point(170.0, 339.0)
Point(172.0, 298.0)
Point(183.0, 187.0)
Point(185.0, 239.0)
Point(193.0, 170.0)
Point(202.0, 197.0)
Point(208.0, 203.0)
Point(209.0, 345.0)
Point(215.0, 208.0)
Point(222.0, 294.0)
Point(225.0, 323.0)
Point(231.0, 329.0)
Point(237.0, 324.0)
Point(241.0, 201.0)
Point(242.0, 212.0)
Point(243.0, 265.0)
Point(250.0, 195.0)
Point(251.0, 242.0)
Point(252.0, 215.0)
Point(253.0, 214.0)
Point(262.0, 227.0)
Point(276.0, 221.0)
Point(284.0, 236.0)
Point(285.0, 227.0)
Point(287.0, 342.0)
Point(294.0, 186.0)
Point(298.0, 200.0)
Point(309.0, 224.0)
Point(310.0, 209.0)
Point(316.0, 320.0)
Point(318.0, 347.0)
Point(320.0, 336.0)
Point(321.0, 172.0)
Point(321.0, 311.0)
Point(325.0, 276.0)
Point(336.0, 222.0)
>>> furthest = left[0]
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    furthest = left[0]
NameError: name 'left' is not defined
>>> furthest = half[0]
>>> area
<function <lambda> at 0x000001C8848815E0>
>>> for p in half:
	if area(p1,pn,p) > area(p1,pn,furthest):
		furthest = point

		
>>> point
(163, 317)
>>> furthest
(163, 317)
>>> for p in half:
	if area(p1,pn,p) > area(p1,pn,furthest):
		furthest = p

		
>>> furthest
(318, 347)
>>> line1 = Line(Point(p1[0], p1[1]), Point(furthest[0], furthest[1]))
>>> line1.draw(win)
Line(Point(150.0, 171.0), Point(318.0, 347.0))
>>> line2 = Line(Point(pn[0], pn[1]), Point(furthest[0], furthest[1]))
>>> 
KeyboardInterrupt
>>> line2.draw(win)
Line(Point(340.0, 154.0), Point(318.0, 347.0))
>>> line2.undraw(win)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    line2.undraw(win)
TypeError: undraw() takes 1 positional argument but 2 were given
>>> line2.undraw(win)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    line2.undraw(win)
TypeError: undraw() takes 1 positional argument but 2 were given
>>> line2.undraw
<bound method GraphicsObject.undraw of Line(Point(340.0, 154.0), Point(318.0, 347.0))>
>>> line2.undraw()
>>> 
KeyboardInterrupt
>>> line2.draw(win)
Line(Point(340.0, 154.0), Point(318.0, 347.0))
>>> half2 = [p for p in half if determ(pn, furthest, p) > 0]
>>> half2
[(152, 281), (163, 317), (170, 339), (172, 298), (183, 187), (185, 239), (193, 170), (202, 197), (208, 203), (209, 345), (215, 208), (222, 294), (225, 323), (231, 329), (237, 324), (241, 201), (242, 212), (243, 265), (250, 195), (251, 242), (252, 215), (253, 214), (262, 227), (276, 221), (284, 236), (285, 227), (287, 342), (294, 186), (298, 200), (309, 224), (310, 209), (316, 320), (321, 172), (321, 311), (325, 276)]
>>> half2 = [p for p in half if determ(pn, furthest, p) < 0]
>>> half2
[(320, 336), (336, 222)]
>>> test1 = Point(half2[0][0], half2[0][1])
>>> test1.draw()
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    test1.draw()
TypeError: draw() missing 1 required positional argument: 'graphwin'
>>> test.draw(win)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    test.draw(win)
AttributeError: 'function' object has no attribute 'draw'
>>> test1.draw(win)
Point(320.0, 336.0)
>>> test1.setFill('red')
>>> half3 = [0 for p in half if determ(p1, furthest, p) < 0]
>>> half3
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> half3 = [p for p in half if determ(p1, furthest, p) < 0]
>>> 
>>> half3
[(183, 187), (193, 170), (202, 197), (208, 203), (215, 208), (241, 201), (242, 212), (243, 265), (250, 195), (251, 242), (252, 215), (253, 214), (262, 227), (276, 221), (284, 236), (285, 227), (294, 186), (298, 200), (309, 224), (310, 209), (316, 320), (320, 336), (321, 172), (321, 311), (325, 276), (336, 222)]
>>> len(half3)
26
>>> half3 = [p for p in half if determ(p1, furthest, p) > 0]
>>> half3
[(152, 281), (163, 317), (170, 339), (172, 298), (185, 239), (209, 345), (222, 294), (225, 323), (231, 329), (237, 324), (287, 342)]
>>> len(half3)
11
>>> for p in half3:
	l = Point(p[0], p[1])
	l.draw(win)
	l.setFill('red')

	
Point(152.0, 281.0)
Point(163.0, 317.0)
Point(170.0, 339.0)
Point(172.0, 298.0)
Point(185.0, 239.0)
Point(209.0, 345.0)
Point(222.0, 294.0)
Point(225.0, 323.0)
Point(231.0, 329.0)
Point(237.0, 324.0)
Point(287.0, 342.0)
>>> p12 = min(half2)
>>> pn2 = max(half2)
>>> furthest = half2[0]
>>> for point in half2:
        if area(p1,pn,point) > area(p1,pn,furthest):
            furthest = point

            
>>> furthest
(320, 336)
>>> point3 = Point(320,336)
>>> line2.undraw()
>>> line4 = Line(Point(p12[0], p12[1]), point3)
>>> line4.draw()
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    line4.draw()
TypeError: draw() missing 1 required positional argument: 'graphwin'
>>> line4.draw(win)
Line(Point(320.0, 336.0), Point(320.0, 336.0))
>>> p12
(320, 336)
>>> half2
[(320, 336), (336, 222)]
>>> line4 = Line(Point(p12[0], p12[1]), Point(336,222))
>>> line4.draw(win)
Line(Point(320.0, 336.0), Point(336.0, 222.0))
>>> line4.undraw()
>>> line2.draw(win)
Line(Point(340.0, 154.0), Point(318.0, 347.0))
>>> half3
[(152, 281), (163, 317), (170, 339), (172, 298), (185, 239), (209, 345), (222, 294), (225, 323), (231, 329), (237, 324), (287, 342)]
>>> p1
(150, 171)
>>> for point in half3:
	p = Point(point[0], point[1])
	p.draw(win)
	p.setFill('green')

	
Point(152.0, 281.0)
Point(163.0, 317.0)
Point(170.0, 339.0)
Point(172.0, 298.0)
Point(185.0, 239.0)
Point(209.0, 345.0)
Point(222.0, 294.0)
Point(225.0, 323.0)
Point(231.0, 329.0)
Point(237.0, 324.0)
Point(287.0, 342.0)
>>> p1 in half3
False
>>> half2
[(320, 336), (336, 222)]
>>> half
[(152, 281), (163, 317), (170, 339), (172, 298), (183, 187), (185, 239), (193, 170), (202, 197), (208, 203), (209, 345), (215, 208), (222, 294), (225, 323), (231, 329), (237, 324), (241, 201), (242, 212), (243, 265), (250, 195), (251, 242), (252, 215), (253, 214), (262, 227), (276, 221), (284, 236), (285, 227), (287, 342), (294, 186), (298, 200), (309, 224), (310, 209), (316, 320), (318, 347), (320, 336), (321, 172), (321, 311), (325, 276), (336, 222)]
>>> area
<function <lambda> at 0x000001C8848815E0>
>>> pmax
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    pmax
NameError: name 'pmax' is not defined
>>> line1.setFill('yellow')
>>> lin1.setFill('black')
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    lin1.setFill('black')
NameError: name 'lin1' is not defined
>>> line1.setFill('black')

>>> line1
Line(Point(150.0, 171.0), Point(318.0, 347.0))
>>> pmax = tuple([318, 347])
>>> pmax
(318, 347)
>>> point3
Point(320.0, 336.0)
>>> line5 = Line(Point(pmax[0], pmax[1]), point3)
>>> line5.draw()
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    line5.draw()
TypeError: draw() missing 1 required positional argument: 'graphwin'
>>> line5.draw(win)
Line(Point(318.0, 347.0), Point(320.0, 336.0))
>>> line5.undraw()
>>> furthest = half2[0]
>>> area(pmax, pn, furthest) > area(pmax, pn, half2[1])
False
>>> pmax2 = half2[1]
>>> line5 = Line(Point(pmax[0], pmax[1]), Point(pmax2[0], pmax2[1]))
>>> line5.draw(win)
Line(Point(318.0, 347.0), Point(336.0, 222.0))
>>> lst = [i for i in range(10)] + 40
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    lst = [i for i in range(10)] + 40
TypeError: can only concatenate list (not "int") to list
>>> lst = [i for i in range(10)] + [4]
>>> lst
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
>>> point2
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    point2
NameError: name 'point2' is not defined
>>> points
[(150, 171), (152, 281), (163, 317), (166, 154), (170, 339), (172, 298), (183, 187), (185, 239), (193, 170), (202, 197), (208, 203), (209, 345), (215, 208), (222, 294), (225, 323), (231, 329), (237, 324), (241, 201), (242, 212), (243, 265), (250, 195), (251, 242), (252, 215), (253, 214), (262, 227), (276, 221), (284, 236), (285, 227), (287, 342), (294, 186), (298, 200), (309, 224), (310, 209), (316, 320), (318, 347), (320, 336), (321, 172), (321, 311), (325, 276), (336, 222), (340, 154)]
>>> points
[(150, 171), (152, 281), (163, 317), (166, 154), (170, 339), (172, 298), (183, 187), (185, 239), (193, 170), (202, 197), (208, 203), (209, 345), (215, 208), (222, 294), (225, 323), (231, 329), (237, 324), (241, 201), (242, 212), (243, 265), (250, 195), (251, 242), (252, 215), (253, 214), (262, 227), (276, 221), (284, 236), (285, 227), (287, 342), (294, 186), (298, 200), (309, 224), (310, 209), (316, 320), (318, 347), (320, 336), (321, 172), (321, 311), (325, 276), (336, 222), (340, 154)]
>>> p1
(150, 171)
>>> lst = p1 + [p for p in points if determ(points[0], points[-1], p) > 0]
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    lst = p1 + [p for p in points if determ(points[0], points[-1], p) > 0]
TypeError: can only concatenate tuple (not "list") to tuple
>>> lst = [p1] + [p for p in points if determ(points[0], points[-1], p) > 0]
>>> lst
[(150, 171), (152, 281), (163, 317), (170, 339), (172, 298), (183, 187), (185, 239), (193, 170), (202, 197), (208, 203), (209, 345), (215, 208), (222, 294), (225, 323), (231, 329), (237, 324), (241, 201), (242, 212), (243, 265), (250, 195), (251, 242), (252, 215), (253, 214), (262, 227), (276, 221), (284, 236), (285, 227), (287, 342), (294, 186), (298, 200), (309, 224), (310, 209), (316, 320), (318, 347), (320, 336), (321, 172), (321, 311), (325, 276), (336, 222)]
>>> determ
<function determ at 0x000001C884897A60>
>>> 
