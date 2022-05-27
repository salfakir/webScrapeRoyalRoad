import pyperclip
import requests
from bs4 import BeautifulSoup as bs





link=input ("Enter starting link : ")
session=requests.session()
copy=""
repeat = int(input("Enter number of repeats: "))


while(repeat !=0):
    while(repeat>0):
        r= session.get(link)
        s = bs(r.text, 'html.parser')
        for div in s.find_all("div", {'class':'ad_content'}): 
            div.decompose()
        title= s.find("h1", {"class": "font-white"}).get_text()
        text = s.find("div", {"class": "chapter-inner chapter-content"}).get_text(separator="\n")
        copy += title +"\n" + text
        nch= s.find_all("a", {"class": "btn btn-primary col-xs-12"})
        for x in nch :
            if(x.get_text().find("Next")!=-1):
                link=link="https://www.royalroad.com"+x.get("href")
        #link="https://www.royalroad.com"+str(nch)
        repeat -=1
    
    pyperclip.copy(copy)
    print("\nnext page: " + link)
    copy=""
    repeat = int(input("Enter number of repeats: "))
quit()