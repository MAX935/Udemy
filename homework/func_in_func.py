from random import choice
def make_color():
    def get_color():
        colors = ('red','green', 'blue')
        color = choice(colors)
        return color
    return get_color


x = make_color()
print(x)