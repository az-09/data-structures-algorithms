# FB interview quesiton2:
words = ["bat", "cat", "tab"]
words2 = ["cat", "bat", "tab"]
alphabet = ['c', 'b', 'a', 't']

def find_index(chr):
    for idx, c in enumerate(alphabet):
        if c == chr:
            return idx

def is_sorted(words):
    word_idx = 0
    len_words = len(words) -1

    while word_idx < len_words:
        first_word = words[word_idx]
        len_first_word = len(first_word)
        first_word_idx = 0

        second_word = words[word_idx + 1]

        while first_word_idx < len_first_word:

            if find_index(first_word[first_word_idx]) < find_index(second_word[first_word_idx]):
                return True
            elif find_index(first_word[first_word_idx]) == find_index(second_word[first_word_idx]):
                first_word_idx += 1
                continue
            else:
                return False
        word_idx += 1

print(is_sorted(words))
print(is_sorted(words2))




