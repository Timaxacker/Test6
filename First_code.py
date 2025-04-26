tim = 'Tim'
ale = 'Ale'
print(f"{tim} & {ale}")

tim2 = 10
ale2 = 20

print(f'{tim2 + ale2 = }\n{tim2 - ale2 = }\n{tim2 / ale2 = }\n{tim2 * ale2 = }')

import turtle as t
from math import log

for i in range(100):
    t.forward(log(i))
    t.right(log(i))

t.mainloop()
