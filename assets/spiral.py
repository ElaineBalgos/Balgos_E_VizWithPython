# import packages from yhe third parties is the same as local files
# just import what you need and run the methods

from matplotlib import pyplot
from turtle import *
from random import randint

#these are fucntions that love in the turtle library
# just reference / use them
speed(0)
bgcolor('black')

x = 1

while x < 400:
	r = randint(0,255)
	g = randint(0,255)
	b = randint(0,255)

	colormode(255)

	pencolor(r, g, b)

	fd(200 + x)
	rt(90.911)

	x = x + 1
