#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  chapter_08_07_return.py
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

def maximum(x, y):
	if x > y:
		return x
	elif x == y:
		return "The numbers are equal"
	else:
		return y

print maximum(500,500.5)

def some_function():
	pass

print some_function()


def main():
	
	return 0

if __name__ == '__main__':
	main()

