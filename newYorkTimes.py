#Fuck you imports go up here
import requests
from bs4 import BeautifulSoup

#asks if they want to see the source code
def showCode(sourceCode):
    while True:
        show = input("show source code? y/n: ").lower()
        print(show)
        if show == 'y':
            print(sourceCode) #debug reasons
            break
        elif show == 'n':
            break
        else:
            print("Please input y or n")

#Deals with what tag you're looking for
def whatYourLookingFor(sourceCode):
    soup = BeautifulSoup(sourceCode, features="html.parser")
    print("\nType none if none else p is a good tag (It's case sensitive)")
    tag = input('Input tag looking for: ')
    if tag == 'p':
        for para in soup.find_all("p"):
            print(para.get_text())
    elif tag == 'none':
        exit
    else:
        for para in soup.find_all(tag):
            print(para)
        #page = soup.find_all(tag)
        #print(page)

#main
def main():
    url = input("input url: ")
    r=requests.get(url)
    sourceCode=r.text

    showCode(sourceCode)
    whatYourLookingFor(sourceCode)

main()
