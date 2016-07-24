#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  chapter_08_05_default_values.py
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

def say(message, times = 3):
	print message * times

def demoSay1():
	running = True
	while running:
		messag = raw_input("What do you want to say? ")
		times = int(raw_input("How many times do you want to say it?" ))
		say(message, times)
		if message == "quit":
			print "This demonstrates that the default values can be overridden."
			running = False

def demoSay2():
	running = True
	while running:
		message = raw_input("What do you want to say? ")
		times = int(raw_input("How many times do you want to say it? "))
		if times < 5:
			times = 5
			print "The minimum number is 5 times. Let me fix that for you."
			say(message, times)
			print "Now let's try again, shall we?"
		else:
			say(message, times)
			running = False

demoSay2()
