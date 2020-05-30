
"""
strips all non-alpha chars
"""
def caps2camel(instr):
    outstr = ''
    cap = False
    for ch in instr:
        if ch >= 'A' and ch <= 'Z':
            if cap:
                outstr += ch
                cap = False
            else:
                outstr += ch.lower()
        if ch == '_':
            cap = True
    return outstr
    
    
if __name__ == '__main__':
    print(caps2camel('THIS_IS_A_TEST'))
    print(caps2camel('TEST_THIS_MUTHU_KUMAR'))