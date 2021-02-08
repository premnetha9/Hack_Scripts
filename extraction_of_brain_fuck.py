#!/usr/bin/python

brainfuck_characters = [
	"[", "]", "+", "-", ".", ",", "<", ">"
	]

content = open('filename.txt').read()	# Change the file name
bf = []

for c in content:
	if c in brainfuck_characters:
		bf.append(c)

print("".join(bf))
