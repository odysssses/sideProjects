#Just a bunch of cool stuff :) Have fun :D
from os import system
from time import sleep
from re import *
import ssl
import urllib.request, urllib.parse, urllib.error 
from bs4 import BeautifulSoup as bs
import json
import xml.etree.ElementTree as ET 

def clear():
    system("cls")

def askcontinue():
    str(input("insert anything to continue: "))

def exceptionExit():
    print("Something went wrong. quitting...")
    sleep(1)
    clear()
    print("Something went wrong. quitting..")
    sleep(1)
    clear()
    print("Something went wrong. quitting.")
    sleep(1)
    clear()
    exit()

def rmvPunct(string):
    string = string.replace('.', '')
    string = string.replace(',', '')
    string = string.replace(':', '')
    string = string.replace(';', '')
    string = string.replace('"', '')
    string = string.replace('-', '')
    string = string.replace('?', '')
    string = string.replace('!', '')
    string = string.replace('\\', '')
    string = string.replace('/', '')
    string = string.replace('*', '')
    string = string.replace('$', '')
    string = string.replace('@', '')
    string = string.replace('(', '')
    string = string.replace(')', '')
    string = string.replace('ç', 'c')
    string = string.replace('ã', 'a')
    string = string.replace('õ', 'o')

    return string

clear()
while True: 
    #hub-------------------------------------------
    ex = int(input("""Which exercise do you want to see?
    [1] ex1 - hourly pay
    [2] ex2 - read files
    [3] ex3 - web scrape
    [4] ex4 - json test
    [5] ex5 - xml test
    Insert the ex: """))
    clear()

    #ex1-------------------------------------------
    if ex == 1:

        print("-"*20)
        try:
            hours = int(input("Insert the amount of hours worked: "))
            rate = float(input("Insert the rate: "))
        except ValueError:
            exceptionExit()

        def computePay(hours, rate):
            if hours > 40:
                bonus = (hours - 40) * 15 
                pay = 40 * rate + bonus
            else:
                pay = hours * rate
            return pay

        pay = computePay(hours, rate)

        print(f"Pay is {pay}")

        askcontinue()
        clear()

    #ex2-------------------------------------------
    elif ex == 2:
        print("-"*20)
        (freq, words) = ({}, [])

        fileInp = str(input("""Insert the directory of the file desired: 
"""))   
        try: 
            file = open(fileInp)
        except:
            exceptionExit()
        
        for line in file:
            line = line.rstrip()
            line = rmvPunct(line)
            words = line.split()
            for word in words:
                freq[word] = freq.get(word, 0) + 1
        words = []

        words = sorted(freq.items(), key=lambda x:x[1], reverse=True)
        words = dict(words)
        
        prevv = 0
        for k, v in words.items():
            if v == prevv:
                continue
            print(f"{k} : {v}")
            prevv = v

        askcontinue()
        clear()
    
    #ex3-------------------------------------------
    elif ex == 3:
        urls = []
        url = str(input("Enter the url: "))

        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        html = urllib.request.urlopen(url, context=ctx).read()
        soup = bs(html, "html.parser")
        tags = soup('a')

        for tag in tags:
            print(tag.get('href', None))
            urls.append(tag.get('href', None))

        for link in urls:
            html = urllib.request.urlopen(link, context=ctx).read()
            soup = bs(html, "html.parser")
            tags = soup('a')
            for tag in tags:
                print(tag.get('href', None))
        
        askcontinue()
        clear()
    
    #ex4-------------------------------------------
    elif ex == 4:
        fish = '''{
    "pufferfish" : "3",
    "cod" : "15",
    "salmon" : "7"
}'''
        jsonFish = json.loads(fish)
        desired = str(input("What fish do you want? We have cod, salmon, and pufferfish. Choose one and we can tell our stock: "))
        print(f"{desired}: {jsonFish[desired]}")

        askcontinue()
        clear()

    #ex5-------------------------------------------
    elif ex == 5:
        fish = '''<fish>
            <pufferfish>3</pufferfish>
            <cod>15</cod>
            <salmon>7</salmon>
        </fish>'''

        xmlFish = ET.fromstring(fish)
        desired = str(input("What fish do you want? We have cod, salmon, and pufferfish. Choose one and we can tell our stock: "))
        print(f"{desired}: {xmlFish.find(desired).text}")

        askcontinue()
        clear()

    #quit------------------------------------------
    ex = str(input("Quit? [Y/N]: ")).upper()[0]
    accptvals = ['Y','N']
    if ex == 'Y':
        exit()
    elif ex == 'N':
        pass
    else: 
        while ex not in accptvals:
            ex = str(input("Quit? [Y/N]: ")).upper()[0]
    
    clear()
