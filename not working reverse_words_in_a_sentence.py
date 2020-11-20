def str_rev(str, start, end):
    if str == None or len(str) < 2:
        return
    while start < end:
        str[start], str[end] = str[end], str[start]
        start += 1
        end -= 1

def reverse_words(sentence):
    if sentence == None or len(sentence) == 0:
        return

    str_len = len(sentence)
    str_rev(sentence, 0, str_len-2)

    start = 0
    end = 0

    while True:
        while start < len(sentence) and sentence[start] == ' ':
            start += 1
        if start == str_len:
            break

        end = start + 1
        while end < str_len and sentence[end] != ' ':
            end += 1

        str_rev(sentence, start, end -1)
        start = end

def get_array(t):
    s = array('u', t)
    return s

def print_array(s):
    i = 0
    while i != len(s):
        stdout.write(s[i])
        i +=1
    print ()




s = get_array('Hello World!')
print_array(s)
reverse_words(s)
print_array(s)