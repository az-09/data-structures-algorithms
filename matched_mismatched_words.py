sentence1 = 'We are really pleased to meet you in our city'
sentence2= 'The city was hit by a really heavy storm'

def solution(sentence1, sentence2):
    words1 = set(sentence1.split())
    words2 = set(sentence2.split())

    return sorted(list(words1^words2)), sorted(list(words1&words2))




print(solution(sentence1, sentence2))