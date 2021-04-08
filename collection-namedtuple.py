from collections import namedtuple



point = namedtuple('point', ('x', 'y', 'z'))

abc = point(1, 2, 3)
print(abc)