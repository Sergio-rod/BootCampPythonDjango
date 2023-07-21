"""import colorgram
colors = colorgram.extract('paint.jpg', 15)


rgb_colors = []

for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b

    new_color = (r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)"""
import turtle
import turtle as t
import random
color_list = [(250, 247, 244), (248, 245, 246), (213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99), (122, 175, 156), (229, 236, 239), (226, 198, 131), (242, 247, 244), (192, 87, 108), (11, 50, 64), (55, 38, 19)]


def convert_rgb(colors_list):
    new_colors = []
    for color_tuple in color_list:
        r = color_tuple[0]/255
        g = color_tuple[1] / 255
        b = color_tuple[2] / 255

        new_color = (r, g, b)
        new_colors.append(new_color)
    return new_colors


sergio = t.Turtle()
colors = convert_rgb(color_list)
y_cor = 300
x_cor = -250
sergio.hideturtle()

for i in range(10):
    sergio.penup()
    sergio.sety(y_cor)
    sergio.setx(x_cor)
    sergio.pendown()
    for j in range(10):
        sergio.dot(20, random.choice(colors))
        sergio.penup()
        sergio.fd(50)
        sergio.pendown()
        sergio.dot(20, random.choice(colors))
    y_cor -= 50


screen = t.Screen()
screen.exitonclick()