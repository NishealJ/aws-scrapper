from django.shortcuts import render

import requests
import re
from bs4 import BeautifulSoup

session = requests.Session()
session.headers = {"",""}

def books_all_scrap():

    book_list_all=[]

    for x in range(0,1):

        url = "https://www.amazon.in/s?i=stripbooks&bbn=1318073031&rh=n%3A976389031%2Cn%3A976390031%2Cn%3A1318073031%2Cp_n_age_range%3A1318385031&dc&page="+str(x)+"&fst=as%3Aoff&qid=1577256423&rnid=1318383031&ref=sr_pg_1"

        content = session.get(url, verify=False).content

        soup = BeautifulSoup(content, "html5lib")
        book_list_temp = soup.findAll('a',{'class':'a-link-normal a-text-normal'})

        for book in book_list_temp:
            book_list_all.append(books_all_scrap_one("https://www.amazon.com"+book.get('href')))

    return book_list_all 

def books_all_scrap_one(turl):

    url = turl
    book_list_all=[]
    content = session.get(url, verify=False).content
    x = re.search("/dp/+", url)

    if (x):
        try:
            soup = BeautifulSoup(content, "html5lib")
            name = soup.find('span',{'class':'a-size-large'}).text
            try:
                image_url = soup.find('img',{'id':'imgBlkFront'}).get('data-a-dynamic-image')
            except :
                image_url = soup.find('img',{'id':'ebooksImgBlkFront'}).get('data-a-dynamic-image')

            book_list_all.append("Book Name: " +name)
            book_list_all.append("Image_url: "+image_url)


            cc = soup.find('div',{'class':'content'})
            t2 = cc.findAll('li')

            for x in range(0,7):
                book_list_all.append(t2[x].text)
            
            ccs =  soup.select('noscript')[1].get_text(strip=True)
            book_list_all.append("Desc: "+ccs)

        except :
            book_list_all.append("REDACTED ERROR : "+url)

        return book_list_all 

    else:
        return 'Redacted'

