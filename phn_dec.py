from itertools import product
import string
dictt = {
	'1':'_', '11':',', '111':'@',
	'2':'A', '22':'B', '222':'C',
	'3':'D', '33':'E', '333':'F',
	'4':'G', '44':'H', '444':'I',
	'5':'J', '55':'K', '555':'L',
	'6':'M', '66':'N', '666':'O',
	'7':'P', '77':'Q', '777':'R', '7777':'S',
	'8':'T', '88':'U', '888':'V',
	'9':'W', '99':'X', '999':'Y', '9999':'Z',
}

#text = '''444333 99966688 277733 7773323444664 84433 22244474433777 99966688 277733 #666552999 99966688777 777744277733 666333 84433 443344477778 4447777 44466 #99966688777 4466688777733 84433 5533999 8666 84433 55566622255 4447777 22335556669 #4666 8666 727774447777
#47777888 995559888 4555 47777888 44999988 666555997 #8555444888477744488866888648833369'''

text = '''2 33 1 4 3 4 7 8 3 7 11 9 2 3 4 3 1 7 6 7 3 7 2 33 111 77 1 4 11 3'''
text = text.split()

def get_word(numbers):
	word = numbers[0]
	plain_text = ""
	for i in range(1, len(numbers)):
		if numbers[i] == numbers[i-1]:
			word += numbers[i]
		else:
			plain_text += dictt[word]
			word = numbers[i]

	plain_text += dictt[word]
	return plain_text

plain_textt = ""
for j in text:
	plain_textt += get_word(j)
	plain_textt += " "

print(plain_textt)
