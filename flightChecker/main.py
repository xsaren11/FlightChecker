'''
Created on 20.06.2017

@author: user
'''
import urllib.request

def main():
    with urllib.request.urlopen('https://online.turkishairlines.com/internet-booking/start.tk?multi=1&lang=en') as f:
        print(f.read())




if __name__ == '__main__':
    main()