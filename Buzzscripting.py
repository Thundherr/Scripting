import os
import sys
import webbrowser 

# run python Buzzscripting.py url
# if no url is provided, 
# read about the honeybee, 
# while you decide where you need to go

def openurl(url):
    webbrowser.open(url)


if __name__ == '__main__':
    try:
        url = sys.argv[1]
    except:
        print("You didn't give me a link :(")
        print("Try again")
        print("read this article on Bees instead")
        url = "https://en.wikipedia.org/wiki/Bee"
        
    openurl(url)
        