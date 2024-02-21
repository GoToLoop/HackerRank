# https://HackerRank.com/challenges/find-second-maximum-number-in-a-list

#----------------------------------------------------------------------#
input()

scores = *map( int, input().split() ),

max_score = max(scores)
no_max_score = filter(max_score.__ne__, scores)
runner_up = max(no_max_score)

print(runner_up)
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
input()
runner_up = sorted(set( map(int, input().split()) ))[-2]
print(runner_up)
#----------------------------------------------------------------------#
