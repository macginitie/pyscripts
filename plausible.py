import urllib.request
import re
 

def considered_plausible(clause, words, ratio):
    good, bad = 0,0
    good_re, bad_re = clause
    print('- good_re: {0}, -- bad_re: {1}'.format(good_re, bad_re))
    for w in words:
        if 'ie' in w or 'ei' in w:
            if re.match(good_re, w):
                print('good: {0}'.format(w))
                good += 1
            if re.match(bad_re, w):
                print('bad: {0}'.format(w))
                bad += 1
    # safety valve
    if bad == 0:
        return good > 0
    print(good/bad)
    return (good / bad) > ratio


if __name__ == '__main__':

    PLAUSIBILITY_RATIO = 2
    url = 'http://wiki.puzzlers.org/pub/wordlists/unixdict.txt'
    words = urllib.request.urlopen(url).read().decode().lower().split()
    
    # look for ie NOT after c, and ie after c
    regex_clause1 = ('.*[^c]ie.*', '.*cie.*')
    
    # look for ei after c, and ei NOT after c
    regex_clause2 = ('.*cei.*', '.*[^c]ei.*')
    
    if considered_plausible(regex_clause1, words, PLAUSIBILITY_RATIO):
        if considered_plausible(regex_clause2, words, PLAUSIBILITY_RATIO):
            print('the plausibility test passed')
        else:
            print('clause 2 failed the plausibility test')
    else:
        print('clause 1 failed the plausibility test')
    
    