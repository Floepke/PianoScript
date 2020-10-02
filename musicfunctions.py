'''This file contains functions about music'''
from logicfunctions import difference

## logic ##
def quartersFitInMeasure(numerator, denominator):
    w = 0
    n = numerator
    d = denominator
    if d < 4:
        w = (n * d) / (d / 2)
    if d == 4:
        w = (n * d) / d
    if d > 4:
        w = (n * d) / (d * 2)
    return w



def midiInterval(midix, midiy):
    intervals = ['unison', 'minor second', 'major second', 'minor third', 
    'major third', 'fourth', 'diminished fifth/augmented fourth', 'fifth',
    'minor sixth', 'major sixth', 'minor seventh', 'major seventh', 'octave']
    try:
        return intervals[difference(midix, midiy)]
    except IndexError:
        return 'interval bigger than octave.'


### noteheads ###
def black_key(x, y, widget):  # center coordinates, radius
    x0 = x - 5
    y0 = y - 5
    x1 = x + 5
    y1 = y + 5
    widget.create_oval(x0, y0, x1, y1, outline='black', fill='black')
    widget.create_line(x0+1,y, x0+1,y-40, width=2)


def black_key_left(x, y, widget):  # center coordinates, radius
    x0 = x - 5
    y0 = y - 5
    x1 = x + 5
    y1 = y + 5
    widget.create_oval(x0, y0, x1, y1, outline='black', fill='black')
    widget.create_oval(x0+4, y0+4, x1-4, y1-4, outline='white', fill='white')
    widget.create_line(x0+1,y, x0+1,y+40, width=2)


def white_key(x, y, widget):  # center coordinates, radius
    x0 = x - 5
    y0 = y - 5
    x1 = x + 5
    y1 = y + 5
    widget.create_oval(x0, y0, x1, y1, outline="black", width=2, fill='white')
    widget.create_line(x0+1,y, x0+1,y-40, width=2)


def white_key_left(x, y, widget):  # center coordinates, radius
    x0 = x - 5
    y0 = y - 5
    x1 = x + 5
    y1 = y + 5
    widget.create_oval(x0, y0, x1, y1, outline="black", width=2, fill='white')
    widget.create_oval(x0+4, y0+4, x1-4, y1-4, outline="black")
    widget.create_line(x0+1,y, x0+1,y+40, width=2)


def noteStop(x, y, widget):
    widget.create_line(x-5,y-5, x, y, x,y, x-5,y+5, width=2) # orginal klavarscribo design
    #widget.create_line(x,y, x,y+5, x,y+5, x,y-5, x,y-5, x,y, x,y, x-5,y+5, x-5,y+5, x,y, x,y, x-5,y-5, fill='black', width=2) # maybe the pianoscript design