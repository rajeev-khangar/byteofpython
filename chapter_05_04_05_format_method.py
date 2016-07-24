#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  chapter_05_04_05_format_method.py
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
#  
#  

age = 20
name = "Alexander"

print "{0} was {1} years old when he wrote this book".format(name, age)
print "Why is {0} playing with that python?".format(name)

print name + " is " + str(age) + " years old"

print "{} was {} years old when he wrote this book".format(name, age)
print "Why is {} playing with that python?".format(name)

#~ decimal (.) precision of 3 for float '0.333'
print "{0:.3f}".format(1.0/3)
#~ fill with underscores (_) with the text centered
# (^) to 11 width "____hello____"
print "{0:^11}".format('hello')
#~ keyword-based "Alexander wrote The Odessia"
print "{name} wrote \"{book}\" when he was {age} years old".format(name="Alexander", book="The Odessia", age=20)

print "a",
print "b"

print "This is the first sentence. \ This is the second sentence"

print r"Newlines are indicated by \n"


