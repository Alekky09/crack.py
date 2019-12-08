from sys import argv
import crypt
from string import ascii_letters, ascii_uppercase, ascii_lowercase
from itertools import product

if len(argv) != 2:
    exit("Usage: python crack.py hash")

hsh = argv[1]
salt = hsh[:2]

def compare(word):

    new_hsh = crypt.crypt(word, salt)

    if new_hsh == hsh:
        print(word)
        quit()

for i in range(1,6):

    for j in ascii_letters:

        for k in product(j, repeat = i):

            word = "".join(k)
            compare(word)


exit("Couldn't crack!")
