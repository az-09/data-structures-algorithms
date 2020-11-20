# given a non-empty string s, you may delete at most one character, judge whether you can mke it palindrome

s = 'abcba'

def solution(word):
    for i in range(len(word)):
        t = word[:i]+word[i+1:]
        if t == t[::-1]: return True
    if s == s[::-1]: return True

print(solution(s))