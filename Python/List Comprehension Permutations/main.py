# https://HackerRank.com/challenges/list-comprehensions

def permus_3sided_regular(x, y, z, n: int):
    x = range( abs(int(x)) + 1 )
    y = range( abs(int(y)) + 1 )
    z = range( abs(int(z)) + 1 )

    permus: list[list[int]] = []

    for i in x:
        for j in y:
            for k in z: i + j + k != n and permus.append( [i, j, k] )

    return permus


def permus_3sided_comprehension(x, y, z, n: int):
    x = range( abs(int(x)) + 1 )
    y = range( abs(int(y)) + 1 )
    z = range( abs(int(z)) + 1 )

    return [ [i, j, k] for i in x for j in y for k in z if i + j + k != n ]


def main():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print( permus_3sided_regular(x, y, z, n) )
    print( permus_3sided_comprehension(x, y, z, n) )


__name__ == '__main__' and main()
