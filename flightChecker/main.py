'''
Created on 20.06.2017

@author: user
'''
# import urllib.request
from gmail import Gmail


def main():
    gm = Gmail('krzysieks1526@gmail.com', 'klucze1526')
    gm.send_message('Kotek', 'Kocham Cie!! Kiedy SEX??')
    

if __name__ == '__main__':
    main()