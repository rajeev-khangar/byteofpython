#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  chapter_08_05_keyword_arguments.py
#  
#  Copyright 2016 alexandergarber <alexandergarber@clockworkpc-Latitude-E6220>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

import math
import sys

def pythagoreanTheorem():
	global length, halfBase, height
	length = int(raw_input("Give a value for one side of an equilateral triangle : "))
	halfBase = length/2
	height = halfBase * math.sqrt(3)
	print "Length is {}".format(length)
	print "halfBase is {}".format(halfBase)
	print "height is {}".format(height)

running = True
while running:
	for length in range(0,1000):
		halfBase = length/2
		height = halfBase * math.sqrt(3)
		#~ print "Length is {}".format(length)
		#~ print "halfBase is {}".format(halfBase)
		print "height is {}".format(height)
		if isinstance (height, int):
			running = False
		elif length == 1000:
			running = False
	running = False




#~ def func(a, b=5, c=10):
	#~ print "a is {}, b is {}, c is {}".format(a,b,c)
#~ 
#~ func(3, 7)
#~ func(25, c = 24)
#~ func(c = 50, a = 100)
