
# oul finder

if __name__ == '__main__':
    f = open('wordlist.txt')
    lst = f.readlines()
    for line in lst:
        word = line[:-1]
        if 'oul' in word:
            print(word)

