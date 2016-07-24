#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  chapter_08_04_fucks_given.py
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

message = "Fuck \n"
times = int(raw_input("How many fucks would you like to give? "))

def fucksGiven(message, times):
	running = True
	while running:
		if times < 3:
			print "\n" + message * times
			print "I'm sorry, you have to give at least three fucks, mate. \n"
			times = int(raw_input("Let's try this again.  How many fucks would you like to give? "))
		elif times > 3:
			print "\n" + message * times
			print "Good, you have given enough fucks."
			running = False
		else:
			print "\n" +  message * times
			print "You have given exactly the requisite number of fucks."
			running = False

fucksGiven(message, times)

print "Have a good one, ya cunt."
