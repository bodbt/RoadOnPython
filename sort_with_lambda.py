"""
doc string
"""

PAIRS = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
PAIRS.sort(key=lambda pair: pair[1])
print(PAIRS)
