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
def mod_inv(x, m):
    return pow(x, -1, m)

def crack_rng(m, sequence):
    r2, r3, r4, r5, r6 = tuple(sequence)
    X1, Y1, Z1 = (r4 - r3) % m, (r3 - r2) % m, (r5 - r4) % m
    X2, Y2, Z2 = (r5 - r4) % m, (r4 - r3) % m, (r6 - r5) % m

    # Compute determinant
    det = (X1 * Y2 - X2 * Y1) % m  
    if det == 0:
        raise ValueError("No unique solution exists")
    
    # Compute modular inverse of determinant
    det_inv = mod_inv(det, m)
    
    # Solve for 'a' and 'b' using modular arithmetic
    a = ((Z1 * Y2 - Z2 * Y1) * det_inv) % m
    b = ((X1 * Z2 - X2 * Z1) * det_inv) % m
    
    # Solve for 'c'
    c = (r4 - a * r3 - b * r2) % m
    
    
    return [a, b, c]
  
    

    

def test():
    assert crack_rng(17, [14, 13, 16, 3, 13]) == [3, 5, 9]
    assert crack_rng(9672485827, [4674207334, 3722211255, 3589660660, 1628254817, 8758883504]) == [22695477, 77557187, 259336153]
    assert crack_rng(101, [0, 91, 84, 16, 7]) == [29, 37, 71]
    assert crack_rng(222334565193649,[438447297,50289200612813,17962583104439,47361932650166,159841610077391]) == [1128889, 1023, 511]
    crack_rng(467, [28, 137, 41, 118, 105])
from sys import flags

if __name__ == "__main__" and not flags.interactive:
    test()