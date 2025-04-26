tim = 'Tim'
ale = 'Ale'
print(f"{tim} & {ale}")

tim2 = 10
ale2 = 20

print(f'{tim2 + ale2 = }\n{tim2 - ale2 = }\n{tim2 / ale2 = }\n{tim2 * ale2 = }')

import turtle as t
from math import log
from colorsys import hsv_to_rgb

t.tracer(0, 0)
t.speed(1000)

i = 0

while True:
    t.color(hsv_to_rgb(i/1000, 1, 1))
    t.forward(40)
    t.right(i)
    t.up()
    t.down()
    if i % 10 == 0:
        t.update()

t.mainloop()
