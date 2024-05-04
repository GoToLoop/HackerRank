from os import chdir, path
chdir( path.dirname(__file__) )

from glob import glob
inputs2d: list[tuple[str, ...]] = []

for filename in glob('input*.txt'):
    with open(filename) as file:
        inputs2d.append( (*(line.strip() for line in file),) )

def custom_input(_=''):
    global row, idx

    inp = inputs2d[row][idx]

    idx = (idx + 1) % len(inputs2d[row])
    row = (row + (not idx)) % inp_len

    return inp


__builtins__.input = custom_input

inp_len = len(inputs2d)
row = idx = 0

from importlib import import_module
from collections.abc import Callable

module = import_module('main')
main: Callable[[None], None] = getattr(module, 'main', None)

if callable(main):
    for i in range(inp_len - 1, -1, -1): main(); i and print()
