import requests
from bs4 import BeautifulSoup
url = input("input url: ")

r=requests.get(url)
sourceCode=r.text

#asks if they want to see the source code
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

#soup code
soup = BeautifulSoup(sourceCode)
page = soup.find_all(input('Input tag looking for (just do P if nothing else):'))
print(page)

