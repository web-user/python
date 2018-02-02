import Tkinter
from PIL import ImageTk
from time import time
import json
import sys
import getopt

from fractal import FractalBuilder


WIDTH = 800
HEIGHT = 600


def get_options(argv):
    try:
        opts, args = getopt.getopt(argv, '', [
            'import=', 'export=', 'seed=', 'points=', 'iterations='
        ])
        return opts
    except getopt.GetoptError:
        print 'Bad parameterss passed.'
        print 'Use: main.py [--import=<importfile>] [--export=<exportfile>]' \
              '[--seed=<seed>] [--points=<points>] [--iterations=<iterations>]'
        sys.exit(2)


def serialize(filename, builder):
    obj = builder.serialize()
    with open(filename, 'w+') as file:
        json.dump(obj, file)


def deserialize(filename):
    with open(filename) as file:
        read_obj = json.load(file)
        return FractalBuilder.deserialize(read_obj)

def main(argv):
    opts = get_options(argv)

    import_file = None
    export_file = None
    seed = time()
    points = 1000
    iterations = 5000

    for opt, arg in opts:
        if opt == '--import':
            import_file = arg
        elif opt == '--export':
            export_file = arg
        elif opt == '--seed':
            seed = arg
        elif opt == '--points':
            points = int(arg)
        elif opt == '--iterations':
            iterations = int(arg)

    if import_file is not None:
        builder = deserialize(import_file)
    else:
        builder = FractalBuilder(WIDTH, HEIGHT, seed, points, iterations)

    builder.build()

    master = Tkinter.Tk()
    pane = Tkinter.Canvas(master, width=WIDTH, height=HEIGHT)

    img = builder.get_image()
    img.save(str(time()) + '.png', 'png')
    imgtk = ImageTk.PhotoImage(img)

    pane.create_image(0, 0, anchor=Tkinter.NW, image=imgtk)
    pane.pack()

    if export_file is not None:
        serialize(export_file, builder)

    Tkinter.mainloop()


if __name__ == '__main__':
    main(sys.argv[1:])
