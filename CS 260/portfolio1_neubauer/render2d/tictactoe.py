# tictactoe.py

# drawing tic tac toe with only a unit square and circle with transformations


from render2d import Render2d


def unit_square(r):
    r.filled_polygon([(-.5, -.5), (.5, -.5), (.5, .5), (-.5, .5)])


def unit_circle(r):
    r.filled_circle((0, 0), 1)


def line(r, length, width, angle, pos):
    r.push_matrix()
    r.translate(*pos)
    r.rotate(angle)
    r.scale(length, width)
    unit_square(r)
    r.pop_matrix()


def ex(r, length, width, pos):
    line(r, length, width, 45, pos)
    line(r, length, width, -45, pos)


def oh(r, radius, thickness, pos):
    r.push_matrix()
    r.translate(*pos)
    r.push_matrix()
    r.scale(radius, radius)
    unit_circle(r)
    r.pop_matrix()
    save_color = r.color
    r.color = r.background
    r.scale(radius-thickness, radius-thickness)
    unit_circle(r)
    r.color = save_color
    r.pop_matrix()


def draw_game(r):
    width = .1
    line(r, 3, width, 0, (1.5, 1))
    line(r, 3, width, 0, (1.5, 2))
    line(r, 3, width, 90, (1, 1.5))
    line(r, 3, width, 90, (2, 1.5))
    ex(r, .75, .1, (1.5, 1.5))
    oh(r, .4, .1, (.5, 2.5))


def clear(r):
    color = r.color
    r.color = r.background
    le, b, re, t = r.window
    r.filled_polygon([(le, b), (le, t), (re, t), (re, b)])
    r.color = color


def main():
    r = Render2d((400, 400))

    print("Drawing game into entire image")
    r.loadview((0, 0, 3, 3))
    draw_game(r)
    r.image.show()
    input("press <Enter>")

    print("Drawing game into lower-left  corner of image")
    r.loadview((0, 0, 3, 3), (0, 0, 200, 200))
    clear(r)
    draw_game(r)
    r.image.show()
    input("press <Enter>")

    print("Drawing game into upper-right corner of image")
    r.loadview((0, 0, 3, 3), (0, 200, 200, 400))
    clear(r)
    draw_game(r)
    r.image.show()
    input("press <Enter>")

    print("Drawing just the center square into the left half of the image")
    r.loadview((1, 1, 2, 2), (200, 0, 400, 400))
    clear(r)
    draw_game(r)
    r.image.show()
    r.image.save("ttt.ppm")
    print("Image Saved --- Close Image window to quit")


if __name__ == "__main__":
    main()
