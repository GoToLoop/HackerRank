# https://HackerRank.com/challenges/python-lists

# tasks = *( # Pypy 3.7
#     { cmd: ( *map(int, args), ) }
#     for _ in range( int(input()) )
#     for cmd, *args in ( input().split(), )
# ),

tasks = *( # Python 3.8+
    { ( args := input().split() )[0]: ( *map(int, args[1:]), ) }
    for _ in range( int(input()) )
),

ints: list[int] = []

for task in tasks:
    for cmd, args in task.items():
        print(ints) if cmd == 'print' else getattr(ints, cmd)(*args)
