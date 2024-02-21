# https://HackerRank.com/challenges/find-a-string

def init():
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)


def count_substring(s: str, sub: str):
    idx = count = 0
    end = len(s) - len(sub)

    if end < 0: return 0

    while idx <= end:
        if ( idx := s.find(sub, idx) + 1 ) < 1: break
        count += 1

    return count


init()

def count_substring(s: str, sub: str):
    return len([ i for i in range(len(s)) if s.startswith(sub,i) ])


init()
