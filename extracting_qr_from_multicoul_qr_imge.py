#!/usr/bin/python3

from PIL import Image
from itertools import combinations
import string
import random

img = Image.open("prism.png")

size = w, h = img.size

white = (255,255,255)
black = (0,0,0)

newimg = Image. new(img.mode,img.size)
new = newimg.load()

data = img.load()

seen_colors = [ (255,0,0),(0,0,255),(0,255,255),(0,255,0),(255,0,255),(255,255,0) ]

for i in range(len(seen_colors)):
	potential = combinations(seen_colors, i+1)

	for good in potential:
		for x in range(w):
			for y in range(h):
				color = data[x,y]

				if color == black or color == white:
					new[x,y] = color

				elif color in good:
					new[x,y] = black
				else:
					new[x,y] = white

		newimg.save("".join([random.chice(string.ascii_lowercase) for _ in range(5) ]) + ".png")
