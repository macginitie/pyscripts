import urllib.request

if __name__ == '__main__':

    url = 'http://wiki.puzzlers.org/pub/wordlists/unixdict.txt'
    words = urllib.request.urlopen(url).read().decode().split()
    for word in words:
        print(word)
    print()
    print('{0} words'.format(len(words)))
