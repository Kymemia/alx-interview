#!/usr/bin/python3
"""
Lockboxes function
"""


def canUnlockAll(boxes):
    """method definition
    """
    unlocked = {0}
    for box_id, box in enumerate(boxes):
        for key in box:
            if key < len(boxes) and key not in unlocked and key != box_id:
                unlocked.add(key)
    return len(unlocked) == len(boxes)
