#!/usr/bin/python3
"""
This module contains a function that returns a lists
of lits representing pascal's triangle
"""


def pascal_triangle(n):
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    temp_tg = [[1], [1, 1]]
    for i in range(2, n):
        tempa = []
        preva = temp_tg[i - 1]
        i = 0
        while i < len(preva) - 1:
            if i == 0:
                tempa.append(1)
                tempa.append(preva[i] + preva[i + 1])
            else:
                tempa.append(preva[i] + preva[i + 1])
            if i == len(preva) - 2:
                tempa.append(1)
            i += 1
        temp_tg.append(tempa)
    return temp_tg


# memory intensive solution
# first try
def pascal(n):

    if n <= 0:
        return []

    temp_tg = [[0, 1, 0]]
    new_tg = [[1]]
    for i in range(1, n):
        tempa = []
        preva = temp_tg[i - 1]
        i = 0
        while i < len(preva) - 1:
            tempa.append(preva[i] + preva[i + 1])
            i += 1
        new_tg.append(tempa)
        tempa = [0] + tempa + [0]
        temp_tg.append(tempa)
    return new_tg
