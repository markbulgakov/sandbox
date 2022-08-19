"""
least recently used
https://www.interviewcake.com/concept/java/lru-cache#:~:text=A%20Least%20Recently%20Used%20(LRU,other%20end%20of%20the%20rack.
"""
from typing import List


def lru(capacity: int, process_list: List[int]) -> None:
    capacity = capacity
    slots = process_list[:capacity]
    print('Init slots value: %s' % slots)

    for item in process_list[capacity:]:
        if item in slots:
            slots.remove(item)
        else:
            slots.pop(0)

        slots.append(item)
        print('Updated slots value: %s' % slots)


if __name__ == '__main__':
    lru(capacity=4, process_list=[7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2])
