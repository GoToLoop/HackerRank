# https://HackerRank.com/challenges/string-validators

from typing import Callable

s = input()

tests = 'alnum', 'alpha', 'digit', 'lower', 'upper'

predicates: tuple[Callable[[str], bool], ...] = *(
  getattr(str, 'is' + test) for test in tests
),

for funct in predicates: print( any(map(funct, s)) )

# =============================================================

any_alpha = any( map(str.isalpha, s) )
any_digit = any( map(str.isdigit, s) )

print(any_alpha or any_digit)
print(any_alpha)
print(any_digit)

print(any( map(str.islower, s) ))
print(any( map(str.isupper, s) ))
