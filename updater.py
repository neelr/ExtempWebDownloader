#!/usr/bin/env python2.7
#Import Modules
import urllib2
import re
from BeautifulSoup import BeautifulSoup
import time
import datetime
import os
#define Variables

#to count how many links it has downloaded
x=0

#To count how many websites it has gone to
longf=0

#All the websites to grab links off of(add some here)
websites= ["https://www.independent.ie/world-news/","https://www.reuters.com/news/world","https://abcnews.go.com/",
"https://www.aljazeera.com/news/","https://www.theatlantic.com/","https://www.theatlantic.com/politics/",
"https://www.theguardian.com/world","https://www.bbc.com/news/world",
'https://www.washingtonpost.com/world/?utm_term=.e6e878c71a42',"https://www.nbcnews.com/world"]
#A loop of what websites to download
os.mkdir(str(datetime.datetime.now().date()))
os.chdir(str(datetime.datetime.now().date()))
while len(websites)>0:
        #connect to a URL
        website = urllib2.urlopen(websites[0])

        #read html code
        html = website.read()
        #use re.findall to get all the links
        links = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', html)
        #Open Websites.txt
        file = open("Websites.txt", "w")
        #Writes all the links in the file
        file.write(str(links))
        #Close the File
        file.close()

        #Download file function
        def download_file(download_url):
                #response = urllib2.urlopen(download_url)
                #soup = BeautifulSoup(urllib2.urlopen(download_url))
                #file = open(soup.title.string+".html", 'w')
                #file.write(response.read())
                #file.close()
                print("Completed")
        #Loop to download links
        while len(links)>0:
                try:
                        download_file(links[0])
                        print "Completed",links[0]
                except:
                        print "ERROR"
                links.pop(0)
        print "---------------------------------------------------------------------------------------------------------------------------------------"
        websites.pop(0)
        if len(websites)==0:
                print "Ended! Thank you for using this tool and make sure to visit https://www.tecton.tk"
                print "---------------------------------------------------------------------------------------------------------------------------------------"
os.chdir("/home/pi/ExtempOffline")


