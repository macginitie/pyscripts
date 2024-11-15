# yellow journalism word puzzle game helper

import sys

line_len = 5 # words per line of output


def three_pointer(letters, word):
    for letter in letters:
        if letter not in word:
            return False
    return True


def find_words(letters):
    print(letters)
    must = letters[0]
    print('must have', must, '!')
    # f = open('wordlist.txt')
    f = open('/usr/share/dict/words')
    lst = f.readlines()
    print('checking', len(lst), 'words')
    count = 0
    for line in lst:
        word = line[:-1]
        # print(word, len(word))
        if must in word and len(word) > 4:
            # print('.')
            couldbe = True
            for char in word:
                if char not in letters:
                    couldbe = False
                    break
            if couldbe:
                count += 1
                if three_pointer(letters, word):
                    print(word, '(3)', end=', ')
                else:
                    print(word, end=', ')
                if count % line_len == 0:
                    print()
    print()
    print(count, 'words found')

if __name__ == '__main__':
    print(len(sys.argv))
    letter_list = []
    for ch in sys.argv[1:]:
        letter_list.append(ch)
    find_words(letter_list)
