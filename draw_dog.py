import turtle as t
#Colors
red = 'red'
blue='blue'
brown = 'maroon'
green ='green'
yellow= 'yellow'
black ='black'
white ='white'
orange='orange'

# function that does something
def rectangle(horizontal, vertical, colour):
  t.pendown
  t.pensize(1)
  t.color(colour)
  t.begin_fill()
  for counter in range(1, 3):
    t.forward(horizontal)
    t.right(90)
    t.forward(vertical)
    t.right(90)
  t.end_fill()
# start of main drawing program
t.penup()
t.speed('slowest')
t.shape('turtle')
t.setheading(0)
dog_elements = [
    # Head
    {'position': (-120, 120), 'size': (70, 80), 'color': red},
    {'position': (-70, 130), 'size': (50, 30), 'color': red},
    {'position': (-140, 40), 'size': (50, -50), 'color': red},

    # Eyes
    {'position': (-100, 80), 'size': (20, -20), 'color': yellow},
    {'position': (-85, 85), 'size': (-10, -10), 'color': black},
    # Mouse
    {'position': (-140, 50), 'size': (30, -20), 'color': white},
    # Feet
    {'position': (-100, -100), 'size': (40, 20), 'color': brown},
    {'position': (-50, -100), 'size': (40, 20), 'color': brown},
    {'position': (50, -100), 'size': (40, 20), 'color': brown},
    {'position': (100, -100), 'size': (40, 20), 'color': brown},
    # Body
    {'position': (-80, 0), 'size': (200, -70), 'color': green},

    # Legs
    {'position': (-80, -100), 'size': (20, -100), 'color': blue},
    {'position': (-50, -100), 'size': (20, -100), 'color': blue},
    {'position': (70, -100), 'size': (20, -100), 'color': blue},
    {'position': (100, -100), 'size': (20, -100), 'color': blue},

    # Tail
    {'position': (120, 30), 'size': (20, -70), 'color': orange},
]

def draw_dog():
    for element in dog_elements:
        position = element['position']
        size = element['size']
        color = element['color']

        t.penup()
        t.goto(position)
        rectangle(size[0], size[1], color)





t.speed('slowest')
t.shape('turtle')
t.setheading(0)

draw_dog()




# Keep the window open until closed manually
t.mainloop()