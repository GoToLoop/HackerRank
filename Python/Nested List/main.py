# https://HackerRank.com/challenges/nested-list

zipped: tuple[tuple[str, ...], tuple[float, ...]] = zip(*(
    ( input(), float(input()) ) for _ in range( int(input()) )
))

names, scores = zipped

low2nd = sorted( set(scores) )[1]
names2nd = [ names[i] for i,s in enumerate(scores) if s == low2nd ]
names2nd.sort()

print(*names2nd, sep = '\n')
