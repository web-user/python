import turtle
import random
import math
import argparse
import json


# parse args for run program
parser = argparse.ArgumentParser(description="For this you can use only this arguments")
parser.add_argument('-t', '--type', help='Type of nonlinear transformation.Available types:\n'
                                         'sinus, heart, spherical, polar, disk', required=True)
parser.add_argument('-i', '--iter_num', type=int, help='Number of iterations. Default value is: 7')
parser.add_argument('-p', '--points_count', type=int,
                    help="Number of points for 1 iteration. More points - best picture. Default value is: 150")
parser.add_argument('-j', '--json', type=bool,
                    help='Display json parameters for run this program. Default value is: False\n'
                         'For enable this use True')


# draw points
def draw(my_turtle, x1, y1):
    my_turtle.penup()
    my_turtle.goto(x1, y1)
    my_turtle.pendown()
    my_turtle.dot(5)


# print json
def print_json(i, a, b, d, e, c, f, rr, gg, bb, xmin, xmax, ymin, ymax):
    print(json.dumps(
        {"affine transformation coefficients": i,
         'a': a,
         "d": d,
         "b": b,
         "e": e,
         "c": c,
         "f": f},
        sort_keys=True, indent=4
        ))
    print(json.dumps(
        {"RGB set": i,
         'r': rr,
         "g": gg,
         "b": bb
         },
        sort_keys=True, indent=4
        ))
    print(json.dumps(
        {"Point limits": i,
         'xmin': xmin,
         "xmax": xmax,
         "ymin": ymin,
         "ymax": ymax
         },
        sort_keys=True, indent=4
        ))


# calculations for drawing
def calculate(my_turtle, f_type, iter_num, points_count, json_display):
    for i in range(iter_num):
        amp = 167  # scaling factor
        # generate coefficients for affine transformation
        a = random.random()
        d = random.uniform(a * a, 1.0)
        b = random.random()
        e = random.uniform(b * b, 1.0)
        c = random.uniform(-1.5, 1.5)
        f = random.uniform(-1.5, 1.5)
        # generate random color



        
        rr = random.randint(0, 150)
        gg = random.randint(0, 150)
        bb = random.randint(0, 150)
        xmin = -1.25
        xmax = 1.25
        ymin = -0.35
        ymax = 0.35

        # display json parameters
        if json_display is True:
            print_json(i, a, b, d, e, c, f, rr, gg, bb, xmin, xmax, ymin, ymax)

        # run calculations and drawing
        for j in range(points_count):
            # generate x & y for nonlinear transformation
            newx = random.uniform(xmin, xmax)
            newy = random.uniform(ymin, ymax)
            x = a * newx + b * newy + c
            y = d * newx + e * newy + f
            # apply random color
            my_turtle.pencolor(rr, gg, bb)
            if f_type == "sinus":
                x1 = math.sin(x) * amp
                y1 = math.sin(y) * amp
                draw(my_turtle, x1, y1)
            if f_type == "heart":
                x1 = (math.sqrt(x * x + y * y) * math.sin(math.sqrt(x * x + y * y) * math.atan(y/x))) * amp
                y1 = (-math.sqrt(x * x + y * y) * math.cos(math.sqrt(x * x + y * y) * math.atan(y/x))) * amp
                draw(my_turtle, x1, y1)
            if f_type == "spherical":
                x1 = (x / (x*x + y*y)) * amp
                y1 = (y / (x*x + y*y)) * amp
                draw(my_turtle, x1, y1)
            if f_type == "polar":
                x1 = (math.atan(y/x)/math.pi) * amp
                y1 = (math.sqrt(x*x + y*y) - 1) * amp
                draw(my_turtle, x1, y1)
            if f_type == "disk":
                x1 = ((1/math.pi) * math.atan(y/x) * math.sin(math.pi * math.sqrt(x*x + y*y))) * amp
                y1 = ((1/math.pi) * math.atan(y/x) * math.cos(math.pi * math.sqrt(x*x + y*y))) * amp
                draw(my_turtle, x1, y1)


def main():
    # parse arguments and set values for vars
    args = parser.parse_args()
    f_type = args.type  # set type of nonlinear transformation

    # set number of iterations
    if args.iter_num is not None:
        iter_num = args.iter_num
    else:
        iter_num = 7

    # set points count for 1 iteration
    if args.points_count is not None:
        points_count = args.points_count
    else:
        points_count = 150

    # display json parameters?
    if args.json is not None:
        json_display = args.json
    else:
        json_display = False

    # check type of nonlinear transformation
    if f_type in ("sinus", "heart", "spherical", "polar", "disk"):
        win = turtle.Screen()
        my_turtle = turtle.Turtle()
        my_turtle.screen.colormode(255)
        my_turtle.speed(0)

        # call function for draw fractal flame
        calculate(my_turtle, f_type, iter_num, points_count, json_display)
        win.exitonclick()
    else:
        print("Please set correct type of nonlinear transformation\nFor get help run this scripts with parameter -h")


if __name__ == "__main__":
    main()