#!/usr/bin/python3
"""
problem:
You have n number of locked boxes in front of you.
 Each box is numbered sequentially from 0 to n - 1 and each
   box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """
    functionn that determines if all rooms can be unlocked
    """
    boxkeys = {0: 1}

    def visitbox(box):
        """
        recursive function to visit every box
        with a key
        """
        for key in box:
            if key not in boxkeys:
                try:
                    boxkeys[key] = 1
                    visitbox(boxes[key])
                except IndexError:
                    del boxkeys[key]
    visitbox(boxes[0])
    return len(boxkeys) == len(boxes)
