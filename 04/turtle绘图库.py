#!/usr/bin/python3
# @Author: WLP
# @name: turtle绘图库.py
# @date 2020-04-30 10:21


import turtle


turtle.color('red', 'yellow')
turtle.pensize(3)
turtle.begin_fill()
for _ in range(50):
    turtle.forward(200)
    turtle.right(144)
turtle.end_fill()
turtle.mainloop()



