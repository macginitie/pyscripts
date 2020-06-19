#// Given a string, write a method which will return a string with the same characters, scrambled such that no two of the same character touch
#// e.g. "aaabcbcaa" -> ababacaca

# return True if no adjacent characters in s are equal
def no_two_in_a_row(s):
    if len(s) < 2:
        return True
    s2 = s
    for idx in range(len(s)-1):
        if s[idx] == s2[idx+1]:
            return False
    return True
    
    
def str_to_char_dict(s):
    dict = {}
    for ch in s:
        if ch in dict:
            dict[ch] += 1
        else:
            dict[ch] = 1
    return dict
    

# return a string with the same characters as s, 
# scrambled so that no two of the same character are adjacent;
# if such a scramble isn't possible, return the empty string
def scramble(s):

    # if no scrambling is necessary, return the input string
    if no_two_in_a_row(s):
        return s

    # count the characters in the input string
    dict = str_to_char_dict(s)
        
    # check whether scrambling is possible
    # if scrambling isn't possible, return the empty string
    mode = max(dict.values())   
    testlen = len(s)
    if len(s) % 2 == 1:
        testlen += 1
    if mode > testlen/2:
        return ""

    return make_scrambled_string_from_dict(dict, mode)
    

def make_scrambled_string_from_dict(dict, mode):

    outstr = ''
    greedy = True
    not_next = ''
    done = False
    while mode > 0:
        if greedy:
            for k in dict.keys():
                if dict[k] == mode and k != not_next:
                    not_next = k
                    outstr += k
                    dict[k] -= 1
                    break           
        else:
            for k in dict.keys():
                if k != not_next and dict[k] > 0:
                    not_next = k
                    outstr += k
                    dict[k] -= 1
                    break           
        mode = max(dict.values())
        greedy = not greedy
    return outstr
    
    
if __name__ == '__main__':

    #print(no_two_in_a_row('xyz'))
    #print(no_two_in_a_row('xzz'))

    print('aaabcbcaa ==> {0}'.format(scramble('aaabcbcaa')))
    print('aaab ==> {0}'.format(scramble('aaab')))
    print('ababacaca ==> {0}'.format(scramble('ababacaca')))
    print('ssstt ==> {0}'.format(scramble('ssstt')))
    print('sssssttt ==> {0}'.format(scramble('sssssttt')))
    print('done.')