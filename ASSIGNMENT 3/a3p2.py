#!/usr/bin/python3

#---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2025 <<Insert your name here>>
#
# Redistribution is forbidden in all circumstances. Use of this software
# without explicit authorization from the author is prohibited.
#
# This software was produced as a solution for an assignment in the course
# CMPUT 331 - Computational Cryptography at the University of
# Alberta, Canada. This solution is confidential and remains confidential 
# after it is submitted for grading.
#
# Copying any part of this solution without including this copyright notice
# is illegal.
#
# If any portion of this software is included in a solution submitted for
# grading at an educational institution, the submitter will be subject to
# the sanctions for plagiarism at that institution.
#
# If this software is found in any public website or public repository, the
# person finding it is kindly requested to immediately report, including 
# the URL or other repository locating information, to the following email
# address:
#
#          gkondrak <at> ualberta.ca
#
#---------------------------------------------------------------

"""
CMPUT 331 Assignment 3 Student Solution
January 2025
Author: <Your name here>
"""

def random_generator(a, b, c, m, r0, r1, n):
    sequence = []
    for i in range(n):
        value = (a*r1 + b*r0 + c) % m
        sequence.append(value)
        r0, r1 = r1, value
    return sequence




    




def test():
    assert random_generator(3, 5, 9, 17, 11, 6, 3) == [14, 13, 16]
    assert random_generator(22695477, 77557187, 259336153, 9672485827, 42, 51, 8) == [4674207334, 3722211255, 3589660660, 1628254817, 8758883504, 7165043537, 4950370481, 2261710858]
    assert random_generator(2**31-5, 743, 549, 1559861749, 97, 101, 8) == [75137452, 935657016, 1474108152, 1106636826, 405962062, 778970349, 1377654917, 1174493038]
    assert random_generator(1128889, 1023, 511, 222334565193649, 65535, 329, 8) == [438447297, 50289200612813, 17962583104439, 47361932650166, 159841610077391, 19587857129781, 111993173627854, 7567964632208]
    
from sys import flags

if __name__ == "__main__" and not flags.interactive:
    test()