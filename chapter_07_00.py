#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  chapter_07.py
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

#~ number = 23
#~ guess = int(raw_input('Enter an integer : '))
#~ 
#~ if guess == number:
	#~ print "Congratulations, you guessed it."
	#~ print "(But no prizes for you)"
#~ elif guess < number:
	#~ print "No, it is a little higher than that."
#~ else:
	#~ print "No, it is a little lower than that"
	#~ 
#~ print 'Done'

number = 23
running = True

while running:
	guess = int(raw_input("Enter an integer : "))
	if guess == number:
		print "Congratulations!"
		running = False
	elif guess < number:
		print "No, higher"
	else:
		print "No, lower"
else:
	print "The while loop is over"

print "Done!"

