
# Code to the SAF Lock GORETIREMENTFUND
import string
lower = list(string.ascii_lowercase)
vock = "GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW"
flag = vock.split()
FLAG = ""

for i in flag:
	for ch in i :
		numb = 25-lower.index(ch.lower())
		FLAG += lower[numb].upper()
	FLAG += " "

print(FLAG)       