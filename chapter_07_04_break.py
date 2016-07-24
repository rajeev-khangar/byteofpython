#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  chapter_07_04_break.py
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

while True:
	s = raw_input("Enter something : ").lower()
	if s == "quit":
		print "You wrote a variation of 'quit'"
		break
	print "You wrote the following: {}".format(s)
	print "Length of the string is", len(s)
print "Done!"
