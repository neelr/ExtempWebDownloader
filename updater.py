#!/usr/bin/env python2.7
#Import Modules
import urllib2
import re
import feedparser
import os
import datetime
#define Variables

#to count how many links it has downloaded
x=0

#To count how many websites it has gone to
longf=0

#All the websites to grab links off of(add some here)
websites= ["https://www.aljazeera.com/xml/rss/all.xml","https://abcnews.go.com/abcnews/internationalheadlines",
"https://www.cnbc.com/id/100727362/device/rss/rss.html","http://feeds.reuters.com/Reuters/worldNews",
"https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US:en",
"https://www.reddit.com/r/worldnews/.rss","http://feeds.bbci.co.uk/news/world/rss.xml","https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/world/rss.xml",
"https://www.buzzfeed.com/world.xml","https://defence-blog.com/feed","https://www.e-ir.info/category/blogs/feed/",
'http://www.globalissues.org/news/feed',"http://rss.cnn.com/rss/edition_world.rss","http://feeds.washingtonpost.com/rss/world",
"http://feeds.feedburner.com/time/world","https://www.cbsnews.com/latest/rss/world","https://www.vox.com/rss/world/index.xml",
"https://www.brookings.edu/topic/international-affairs/feed/","https://www.dailytelegraph.com.au/news/world/rss"]
os.mkdir(str(datetime.datetime.now().date()))
os.chdir(str(datetime.datetime.now().date()))
def download_file(download_url):
                        response = urllib2.urlopen(download_url)
                        file = open(d.entries[0]['title']+".html", 'w')
                        file.write(response.read())
                        file.close()
                        print("Completed")
while len(websites)>0:
        d = feedparser.parse(websites[0])
        #Loop to download links
        while len(d.entries)>0:
                try:
#                        download_file(d.entries[0]['link'])
                        print "Completed",d.entries[0]['link']
                except:
                        print "ERROR"
                d.entries.pop(0)
        print "---------------------------------------------------------------------------------------------------------------------------------------"
        websites.pop(0)
        if len(websites)==0:
                print "Ended! Thank you for using this tool and make sure to visit https://www.tecton.tk"
                print "---------------------------------------------------------------------------------------------------------------------------------------"
os.chdir("/home/neel_redkar/ExtempWebDownloader")