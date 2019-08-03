#!/usr/bin/python
# Author: Andrew Barrett
# Date: 8/3/19
# Takes an integer as input and outputs the integer in English. Maximum unit is the centillion.

import sys
import re

scales = ['nil', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion', 'decillion', 'undecillion', 'duodecillion', 'tredecillion', 'quattuordecillion', 'quindecillion', 'sexdecillion', 'septendecillion', 'octodecillion', 'novemdecillion', 'vigintillion', 'centillion']

def number_reader(input):
	o = ''
	l = len(input)
	if l == 1:
		digit = int(input[0])
		if digit == 1:
			o = 'one'
		elif digit == 2:
			o = 'two'
		elif digit == 3:
			o = 'three'
		elif digit == 4:
			o = 'four'
		elif digit == 5:
			o = 'five'
		elif digit == 6:
			o = 'six'
		elif digit == 7:
			o = 'seven'
		elif digit == 8:
			o = 'eight'
		elif digit == 9:
			o = 'nine'
	elif l == 2:
		digit1 = int(input[0])
		digit2 = int(input[1])
		if digit1 == 1:
			if digit2 == 0:
				o = 'ten'
			elif digit2 == 1:
				o = 'eleven'
			elif digit2 == 2:
				o = 'twelve'
			elif digit2 == 3:
				o = 'thirteen'
			elif digit2 == 4:
				o = 'fourteen'
			elif digit2 == 5:
				o = 'fifteen'
			elif digit2 == 6:
				o = 'sixteen'
			elif digit2 == 7:
				o = 'seventeen'
			elif digit2 == 8:
				o = 'eighteen'
			elif digit2 == 9:
				o = 'nineteen'
			return o

		elif digit1 == 2:
			o = 'twenty'
		elif digit1 == 3:
			o = 'thirty'
		elif digit1 == 4:
			o = 'forty'
		elif digit1 == 5:
			o = 'fifty'
		elif digit1 == 6:
			o = 'sixty'
		elif digit1 == 7:
			o = 'seventy'
		elif digit1 == 8:
			o = 'eighty'
		elif digit1 == 9:
			o = 'ninety'
		dash = '' if input[0] == '0' or input[1] == '0' else '-'
		o += dash + number_reader(input[1])

	elif l == 3:
		digit1 = int(input[0])
		if digit1 > 0:
			o = number_reader(input[0]) + ' hundred ' + number_reader(input[1:])
		else:
			o = number_reader(input[1:])
	return o

def print_number(argument):
	#print '\nargu: ', argument
 	l = len(argument)
 	if l <= 3:
 		print number_reader(argument)
 		return
 	i = 1
 	s = 4
 	while s+3 <= l:
 		s += 3
 		i += 1

 	diff = l-s+1
 	#print 'l is ', l, ' s is ', s, ' diff is ', diff
 	number = number_reader(argument[:diff])
 	if number != '':
 		sys.stdout.write(number + ' ' + scales[i])
 		for i in range(diff, len(argument)):
 			if argument[i] != '0':
 				sys.stdout.write(', ')
 				break
 	#print ''
 	print_number(argument[diff:])


play = True
regex = re.compile('^-?\d+')

while play:
 	argument = raw_input("Enter a number: ")
 	# Numbers-only check
 	if regex.match(argument) == None:
 		exit()
 	 	# Negative number check
 	if (argument[0] == '-'):
 		sys.stdout.write('negative ')
 		argument = argument[1:]

 	# Small number check, if so just print
	if len(argument) < 4:
		if argument == '0':
			print 'zero'
		else:
 			print number_reader(argument)
 	else:
 	 	print_number(argument)