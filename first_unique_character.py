import collections

def solution(word):
    count = collections.Counter(word)

    for idx, w in enumerate(word):
        if count[w] == 1:
            return idx
    return -1


print(solution('alphabet'))