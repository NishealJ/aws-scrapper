from django.shortcuts import render

import requests
import re
from bs4 import BeautifulSoup
import json
session = requests.Session()
session.headers = {"",""}

    
def books_all_scrap():
    url ="https://catalog.roundrocktexas.gov/cgi-bin/koha/opac-search.pl"
    content = session.get(url).content
    soup = BeautifulSoup(content, "html5lib")
    sp3 = soup.findAll('div',{"class":"span3"})
    book_list_tag=["mc-ccode:2X2LUO","mc-ccode:ABKF", "mc-ccode:AGN", "mc-ccode:LP", "mc-ccode:ABKMYS", "mc-ccode:ABKNF", "mc-ccode:ABKOS", "mc-ccode:REF", "mc-ccode:ABKROM", "mc-ccode:ABKSF", "mc-ccode:ABKW", "mc-ccode:ACDF", "mc-ccode:ACDMUS", "mc-ccode:ACDMYS", "mc-ccode:ACDNF", "mc-ccode:ACDROM", "mc-ccode:ACDSF", "mc-ccode:ACDW", "mc-ccode:ACP", "mc-ccode:ADVD", "mc-ccode:ADVDNF", "mc-ccode:ADVDR", "mc-ccode:AMAG", "mc-ccode:ASMPF", "mc-ccode:ASMPMYS", "mc-ccode:ASMPNF", "mc-ccode:ASMPROM", "mc-ccode:ASMPSF", "mc-ccode:ASMPW", "mc-ccode:ARCH", "mc-ccode:REFDESK", "mc-ccode:ATLAS", "mc-ccode:BLBK", "mc-ccode:EBB", "mc-ccode:CMAG", "mc-ccode:CHI", "mc-ccode:CHINF", "mc-ccode:COMP", "mc-ccode:DB", "mc-ccode:DICT", "mc-ccode:DLAUDBK", "mc-ccode:DLBK", "mc-ccode:DLCOM", "mc-ccode:DLMAG", "mc-ccode:EBKNF", "mc-ccode:ECD", "mc-ccode:EDVD", "mc-ccode:ESMP", "mc-ccode:ER", "mc-ccode:EBK", "mc-ccode:ECP", "mc-ccode:GENCD", "mc-ccode:GENMAG", "mc-ccode:GENMICRO", "mc-ccode:GEN", "mc-ccode:GENCIR", "mc-ccode:INDIC", "mc-ccode:INDICNF", "mc-ccode:DVDHIN", "mc-ccode:JBKF", "mc-ccode:JGN", "mc-ccode:JBKMYS", "mc-ccode:JBKNF", "mc-ccode:JBKSF", "mc-ccode:JCD", "mc-ccode:JCP", "mc-ccode:JDVD", "mc-ccode:JSMP", "mc-ccode:KTG", "mc-ccode:ALOC", "mc-ccode:CLOC", "mc-ccode:HIST", "mc-ccode:LUCKYBOOK", "mc-ccode:LUCKYDVD", "mc-ccode:ANBKMYS", "mc-ccode:ANBKROM", "mc-ccode:ANBKSF", "mc-ccode:ANBKW", "mc-ccode:ANBKF", "mc-ccode:ANBKNF", "mc-ccode:YANBK", "mc-ccode:YANBKNF", "mc-ccode:OR", "mc-ccode:PARENT", "mc-ccode:PUP", "mc-ccode:DVDSPA", "mc-ccode:ACDSPA", "mc-ccode:ACDNFSPA", "mc-ccode:ABKSPA", "mc-ccode:ALPSPA", "mc-ccode:ACDMUSSPA", "mc-ccode:ABKNFSPA", "mc-ccode:ASMPSPA", "mc-ccode:EBBSPA", "mc-ccode:EBKNFSPA", "mc-ccode:EDVDSPA", "mc-ccode:ERBKSPA", "mc-ccode:EBKSPA", "mc-ccode:JBKSPA", "mc-ccode:JBKNFSPA", "mc-ccode:JDVDSPA", "mc-ccode:YASPA", "mc-ccode:PROF", "mc-ccode:TTG", "mc-ccode:WEB", "mc-ccode:YABKF", "mc-ccode:YAGN", "mc-ccode:YABKNF", "mc-ccode:YAREF", "mc-ccode:YACD", "mc-ccode:YADVD", "mc-ccode:YAMAG", "mc-ccode:YASMP", "mc-loc:Main", "mc-loc:ADULT", "mc-loc:ADULTAV", "mc-loc:ADULTNEWFC", "mc-loc:ADULTNEWNF", "mc-loc:ADULTOVR", "mc-loc:CHILDDESK", "mc-loc:REFDESK", "mc-loc:ATLASTND", "mc-loc:JUNIOR", "mc-loc:BBTOWER1", "mc-loc:CIRC2", "mc-loc:DT2FLR", "mc-loc:DTSP", "mc-loc:DT1FLR", "mc-loc:EASYAV", "mc-loc:JUNAV", "mc-loc:LOCALAUTHJ", "mc-loc:LOCALAUTH", "mc-loc:ONLINE", "mc-loc:OVD", "mc-loc:PARENT", "mc-loc:PUPPETS", "mc-loc:RBD", "mc-loc:CART", "mc-loc:SWMAIN", "mc-loc:SWRED", "mc-loc:SWBKDRP", "mc-loc:EASY", "mc-loc:NEWYABK", "mc-loc:YACOLL", "mc-itype,phr:14DAYS", "mc-itype,phr:2HOURS", "mc-itype,phr:ARCHIVE", "mc-itype,phr:BINDERY", "mc-itype,phr:BOOK", "mc-itype,phr:CD", "mc-itype,phr:TECH", "mc-itype,phr:CURBKIT", "mc-itype,phr:DVD", "mc-itype,phr:ERPAM", "mc-itype,phr:HOTSPOT", "mc-itype,phr:MAG", "mc-itype,phr:MICRO", "mc-itype,phr:KIT", "mc-itype,phr:CDMUSIC", "mc-itype,phr:MAGNEW", "mc-itype,phr:ONORDER", "mc-itype,phr:ONLINE", "mc-itype,phr:SMP", "mc-itype,phr:PUPPETS", "mc-itype,phr:RASPBERRY", "mc-itype,phr:REF", "mc-itype,phr:DASHDOT", "mc-itype,phr:90MIN", "mc-itype,phr:ONLINEAUD", "mc-itype,phr:ONLINEBK", "mc-itype,phr:ONLINEMAG", "available"]
    book_list_name=["2x2 - Library Use Only    ", "Adult - Fiction    ", "Adult - Graphic novels    ", "Adult - Large Print    ", "Adult - Mystery    ", "Adult - Nonfiction    ", "Adult - Oversized books    ", "Adult - Reference    ", "Adult - Romance    ", "Adult - Science fiction/Fantasy    ", "Adult - Western    ", "Adult CDs - Fiction    ", "Adult CDs - Music    ", "Adult CDs - Mystery    ", "Adult CDs - Nonfiction     ", "Adult CDs - Romance    ", "Adult CDs - Science fiction/Fantasy    ", "Adult CDs - Western    ", "Adult Combo Pack    ", "Adult DVDs    ", "Adult DVDs - Nonfiction    ", "Adult DVDs - Rated R    ", "Adult magazines    ", "Adult Playaways - Fiction    ", "Adult Playaways - Mystery    ", "Adult Playaways - Nonfiction    ", "Adult Playaways - Romance    ", "Adult Playaways - Science fiction/Fantasy    ", "Adult Playaways - Western    ", "Archival Material    ", "Ask at reference    ", "Atlas    ", "Bluebonnet Books    ", "Board Books    ", "Childrens magazines    ", "Chinese - Adult - Fiction    ", "Chinese - Adult - Nonfiction    ", "Computer    ", "Database    ", "Dictionary    ", "Downloadable Audiobook    ", "Downloadable Book    ", "Downloadable Comic    ", "Downloadable Magazine    ", "Easy - Nonfiction    ", "Easy CDs    ", "Easy DVDs    ", "Easy Playaways    ", "Easy Readers    ", "Everybody Books    ", "Everybody Combo Pack    ", "Genealogy - CDs    ", "Genealogy - Magazines    ", "Genealogy - Microforms    ", "Genealogy - Reference books    ", "Genealogy for checkout    ", "Hindi - Adult - Fiction    ", "Hindi - Adult - Nonfiction    ", "Hindi - DVDs     ", "Junior - Fiction    ", "Junior - Graphic novels    ", "Junior - Mystery    ", "Junior - Nonfiction    ", "Junior - Science fiction/Fantasy    ", "Junior CDs    ", "Junior Combo Pack    ", "Junior DVDs    ", "Junior Playaways    ", "Kits To Go    ", "Local Authors - Adult    ", "Local Authors - Childrens     ", "Local History Documents    ", "Lucky Day Book    ", "Lucky Day DVD    ", "New books - Adult fiction    ", "New books - Adult fiction    ", "New books - Adult fiction    ", "New books - Adult fiction    ", "New books - Adult fiction    ", "New books - Adult nonfiction    ", "New books - Young adult fiction    ", "New books - Young Adult non-fiction    ", "On Order    ", "Parenting Collection    ", "Puppets    ", "Spanish - Adult -  DVDs     ", "Spanish - Adult - CDs Fiction     ", "Spanish - Adult - CDs Nonfiction    ", "Spanish - Adult - Fiction     ", "Spanish - Adult - Large Print    ", "Spanish - Adult - Music CDs     ", "Spanish - Adult - Nonfiction    ", "Spanish - Adult - Playaways    ", "Spanish - Board Books    ", "Spanish - Easy - Nonfiction    ", "Spanish - Easy DVDs    ", "Spanish - Easy Readers    ", "Spanish - Everybody Books    ", "Spanish - Junior - Fiction    ", "Spanish - Junior - Nonfiction    ", "Spanish - Junior DVDs    ", "Spanish - Young Adult - Fiction    ", "Staff reference    ", "Tech To Go    ", "Website    ", "Young Adult - Fiction    ", "Young Adult - Graphic novels    ", "Young Adult - Nonfiction    ", "Young Adult - Reference    ", "Young Adult CDs    ", "Young Adult DVDs    ", "Young Adult magazines    ", "Young Adult Playaways    ", "   ", "Adult (2nd floor)    ", "Adult Audio/Video (1st floor)    ", "Adult New Fiction (2nd floor)    ", "Adult New Non-fiction (2nd floor)    ", "Adult Oversized Books(2nd floor)    ", "Ask at Children's Desk (1st floor)    ", "Ask at Reference Desk (2nd floor)    ", "Atlas Stand (2nd floor)    ", "Blue shelves (1st floor)    ", "Board Book Display Tower (1st floor)    ", "Circulation Desk (2nd floor)    ", "Display Tower - 2nd floor    ", "Display Tower - Staff Picks    ", "Display Towers - 1st floor    ", "Easy Audio/Video (1st floor)    ", "Junior Audio/Video (1st floor)    ", "Local Author (1st floor)    ", "Local Author (2nd floor)    ", "Online Resource    ", "Overdrive    ", "Parenting Resources (1st floor)    ", "Puppets (1st floor)    ", "RBdigital    ", "Shelving cart - Ask staff for assistance    ", "Slat Wall - near Main St. entrance    ", "Slat Wall - Red Wall near AV    ", "Slat Walls - near book drop/elevator    ", "Yellow shelves (1st floor)    ", "Young Adult Collections - New Books    ", "Young Adult Collections (1st floor)    ", "14 Day Checkout - Book    ", "4 Hour Checkout    ", "Archival Material    ", "Bindery    ", "Book    ", "CD    ", "Chromebook    ", "Curb Kit    ", "DVD    ", "Easy Reader Pamphlets    ", "Hotspot    ", "Magazine    ", "Microform    ", "Mixed Media    ", "Music on CD    ", "New Magazine    ", "On Order    ", "Online    ", "Playaway    ", "Puppets    ", "Raspberry Pi    ", "Reference     ", "Robot    ", "Use 2HOURS instead    ", "eAudioBook    ", "eBook    ", "eMagazine    ", " Only items currently available for loan or reference"]
    error_url=0
    total=0
    index=0
    book_details=[]
    ttls =0
    for t in book_list_tag:
        general = ''
        url2 ='https://catalog.roundrocktexas.gov/cgi-bin/koha/opac-search.pl?advsearch=1&idx=kw&op=and&idx=kw&op=and&idx=kw&limit=mc-ccode%3A&limit='+str(t)+'&limit=mc-itype%2Cphr%3A14DAYS&limit=mc-itype%2Cphr%3ABOOK&limit=mc-itype%2Cphr%3AONORDER&limit=mc-itype%2Cphr%3AONLINE&limit=mc-itype%2Cphr%3AREF&limit=mc-itype%2Cphr%3AONLINEAUD&limit=mc-itype%2Cphr%3AONLINEBK&sort_by=relevance&do=Search'
        content = session.get(url2).content
        soup = BeautifulSoup(content, "html5lib")
        sn1 = soup.find('p',{"id":"numresults"})
        sn2 = sn1.find('strong').text
        sn2=sn2.replace('Your search returned ','')
        sn2=sn2.replace(' results.','')
        sn2=int(sn2)
        i = 0 
        curl=0
        while i<=sn2:
            if i==0:
                url3 = url2
            else:
                url3 = url2+'&offset='+str(i) 
                
            content3 = session.get(url3).content
            soup3 = BeautifulSoup(content3, "html5lib")
            sn3 = soup3.findAll('td',{"class":"bibliocol"})
            for tds in sn3:
                a = tds.find('a',{"class":"title"})['href']
                mo =books_all_scrap_one('https://catalog.roundrocktexas.gov/'+str(a))
                curl=curl+1
                ttls=ttls+1
                s_t1 = "Currently extracting "+book_list_name[index]+" total books in this categroy is "+str(sn2)+" we got "+str(curl)+" Total books we scraped "+str(ttls)
                print(s_t1)
                general=general+'('+str(curl)+')'+mo
                # print('Extracted : ',mo)
                
            i=i+20
        # error_url=error_url+1
        # print('UPPER ERROR: ',url3)
        # /home/user88/Desktop/Iwyno/scrap_outputs/
        print ('books saved',curl)
        f= open("/home/user88/Desktop/Iwyno/scrap_outputs/"+str(t)+"_"+book_list_name[index]+".json","w+")
        f.write(json.dumps(general))
        f.close() 
        index=index+1
    return general

    
def books_all_scrap_one(turl):
    content = session.get(turl).content
    soup = BeautifulSoup(content, "html5lib")
    sni1 = soup.find('div',{"id":"bookcover"})
    one_book=[]
    img_url=sni1.find('img')['src']
    
    try:
        title = soup.find('title').text
        title=title.replace('Round Rock Public Library System catalog','')
        title=title.replace('Details for: ','')
        title=title.replace('/','')
        title=title.replace(',','')
    except:
        title='NOT-FOUND'
    
    try:
        by1 = soup.find('span',{"class":"title_resp_stmt"}).text
    except:
        print len(soup.findAll('span',{"property":"name"}))
        by1 = soup.findAll('span',{"property":"name"})[0].text

    try:
        pub = soup.find('span',{"class":"results_summary"})
        pub = pub.find('a').text
    except:
        pub='NOT-FOUND'

    try:
        desc = soup.find('span',{"property":"description"}).text
    except:
        desc='NOT-FOUND'
    
    try:
        coll = soup.find('td',{"class":"collection"}).text
    except:
        coll='NOT-FOUND'   
    
    try:
        barcode = soup.find('td',{"property":"serialNumber"}).text
    except:
        barcode='NOT-FOUND' 
        
    try:
        isbn = soup.find('span',{"class":"results_summary isbn"}).text
    except:
        isbn='NOT-FOUND' 
    
    title=title.replace(',','')
    by1=by1.replace(',','')
    pub=pub.replace(',','')
    desc=desc.replace(',','')
    coll=coll.replace(',','')
    coll=coll.replace(',','')
    barcode=barcode.replace(',','')
    
    mko = "["+img_url+","+title+","+by1+","+pub+","+desc+","+coll+","+coll+","+barcode+"]"
    print (title)
    
    return mko
