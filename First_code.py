tim = 'Tim'
ale = 'Ale'
print(f"{tim} & {ale}")

tim2 = 10
ale2 = 20

print(f'{tim2 + ale2 = }\n{tim2 - ale2 = }\n{tim2 / ale2 = }\n{tim2 * ale2 = }')

import turtle as t
from math import log

t.speed(100)

for i in range(1000000):
    t.forward(40)
    t.right(i)

t.mainloop()
