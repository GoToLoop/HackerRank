# https://HackerRank.com/challenges/designer-door-mat

N, M = map( int, input().split() )
NN = N >> 1
MSG, PATTERN, FILL = 'WELCOME', '.|.', '-'

print(*(
    ( i and PATTERN * ( (NN - abs(i) << 1) + 1 ) or MSG )
    .center(M, FILL) for i in range(-NN, NN + 1)
), sep='\n')
