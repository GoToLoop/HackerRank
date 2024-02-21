# https://HackerRank.com/challenges/python-string-formatting

def print_formatted(n):
    bits = n.bit_length()

    print(*(
        f'{i:{bits}} {i:{bits}o} {i:{bits}X} {i:{bits}b}'
        for i in range(1, n + 1)
    ), sep='\n')


def print_formatted2(n):
    pattern = '{0:{1}} {0:{1}o} {0:{1}X} {0:{1}b}'
    bits = n.bit_length()

    print('\n'.join(
        pattern.format(i, bits) for i in range(1, n + 1)
    ))


print_formatted( int(input()) )
print()
print_formatted( 20 )
print()
print_formatted2( 20 )
