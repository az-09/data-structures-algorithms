sentence1 = "Hi all, my name is Tom...I am originally from Australia."
sentence2="I need to work very hard to learn more about algorithms in Python!"

def solution(sentence):

    clean_sentence = sentence.replace(",", "").replace(".", "").replace("!", "").split()
    print(clean_sentence)
    return round(sum([len(sentence) for sentence in clean_sentence])/len(clean_sentence), 2)

print(solution(sentence1))
print(solution(sentence2))