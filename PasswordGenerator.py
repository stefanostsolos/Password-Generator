from passwordmeter import test
import requests
from os.path import isfile 
import secrets

if not isfile('words.txt'):
    print('Downloading words.txt . . .')
    url = 'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'
    r = requests.get(url)
    with open('words.txt', 'wt') as f:
        f.write(r.text)

words=open('words.txt', 'rt').read().split("\n")
special_chars=['!', '@', '#', '$', '%', '^', '&', '*']

def create_password(num_words,num_numbers,num_special):
    pass_str=''

    for _ in range(num_words):
        pass_str+=secrets.choice(words).lower().capitalize()
    for _ in range(num_numbers):
        pass_str+=str(secrets.randbelow(9))
    for _ in range(num_special):
        pass_str+=secrets.choice(special_chars)
    return pass_str

def main():
    print("How many words, numbers and special characters you want?")
    num_words, num_numbers, num_special = map(int, input().split())
    pass_str=create_password(num_words, num_numbers, num_special)
    strength,_=test(pass_str)
    print('Password: %s'%pass_str)
    print("\nPassword's Strength: %0.5f"%strength)
main()