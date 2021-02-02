"""
This is the docstring for the mc module.
We can show how to use the code in here.
This is like a comment, but it is available
for inspection

>>>m = Markov('ab')
>>>m.predict('a')
'b'
"""

import argparse
import random
import sys
import urllib.request as req

def fetch_file(url, fname):
    fin = req.urlopen(url)
    data = fin.read()
    fout = open(fname, mode = 'wb')
    fout.write(data)
    fout.close()

def from_file(fname, size):
    fin = open(fname, mode = 'r', encoding = 'utf8')
    txt = fin.read()
    m = Markov(txt, size)
    return m

class Markov:
    def __init__(self, txt, size=1):
        self.tables = []
        for i in range(size):
            self.tables.append(get_table(txt, size = i + 1))

    def predict(self, txt):
        table = self.tables[len(txt)-1]
        options = table.get(txt, {})
        if not options:
            raise KeyError(f'{txt} not found')
        possibles = []
        for key in options:
            count = options[key]
            for i in range(count):
                possibles.append(key)
        return random.choice(possibles)

def get_table(text, size = 1):
    """
    this is the docstring for get_table
    >>> get_table('abab')
    {'a':{'b':1}}
    """
    result = {}
    for i in range(len(text)):
        chars = text[i:i+size]
        try:
            out = text[i + size]
        except IndexError:
            break
        char_dict = result.get(chars, {})
        if out not in char_dict:
            char_dict[out] = 0
        char_dict[out] += 1
        result[chars] = char_dict
    return result

def repl(m):
    #read evaluate print loop
    print('Welcome to the REPL!')
    print('Hit ctrl-c to exit')
    while True:
        try:
            txt = input('>')
        except KeyboardInterrupt:
            print('Goodbye!')
            break
        try:
            res = m.predict(txt)
        except IndexError:
            print('Too long, try again')
        except KeyError:
            print('Not found, try again')
        else:
            print(res)
        
def main(args):
    ap = argparse.ArgumentParser()
    ap.add_argument('-f','--file',help = 'file to read')
    ap.add_argument('-s','--size',help='Size of chain (default 1)', default = 1, type = int)
    
    opts = ap.parse_args(args)
    if opts.file:
        m = from_file(opts.file, size = opts.size)
        repl(m)

if __name__ == '__main__':
    #m = from_file('pp.txt', 4)
    #repl(m)
    main(sys.argv[1:])
else:
    print('I\'m loading this as a library', __name__)
        
