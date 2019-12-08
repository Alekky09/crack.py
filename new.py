from cs50 import get_string
from sys import argv
import crypt
from string import ascii_letters

word = argv[1]
salt = '50'

new = crypt.crypt(word, salt)
print (new)