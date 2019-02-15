# ExtempWebDownloader


## A downloader of news articles to help with the speech even Extemp, specifically IX and can edit to support NX too if requested


### All credit for the Dropbox connector goes to andreafabrizi right [here](https://github.com/andreafabrizi/Dropbox-Uploader)


## About:
Hello! This is a resource where you can mass download and update articles for extemp. All you need to do is run the updater.py file and it will downlaod all the html files on many websites. This will take some time so be able to wait. you just have to run it again to update all the articles! This is good if you like to read the news of if you are in Extemp and need to mass download articles for a competition!


## How to:
1. Make sure you have the dependencies,(`sudo apt-get install at`),(`sudo pip install BeautifulSoup`)

2.Add your username to all places in upload.sh and update.py with +=USERNAME=+

3) Run `./dropbox-uploader.sh` and enter access key to your account w/ full access

4) Trust all the scripts

5) Run `./uploader.sh` at a time with root privileges and it will download all files and upload them to Dropbox in a folder called ExtempWebDownloader. This will start everyday at the time you ran it.


## Websites
All websites downloaded from:`"https://www.aljazeera.com/xml/rss/all.xml","https://abcnews.go.com/abcnews/internationalheadlines",
"https://www.cnbc.com/id/100727362/device/rss/rss.html","http://feeds.reuters.com/Reuters/worldNews",
"https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US:en",
"https://www.reddit.com/r/worldnews/.rss","http://feeds.bbci.co.uk/news/world/rss.xml","https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/world/rss.xml",
"https://www.buzzfeed.com/world.xml","https://defence-blog.com/feed","https://www.e-ir.info/category/blogs/feed/",
'http://www.globalissues.org/news/feed',"http://rss.cnn.com/rss/edition_world.rss","http://feeds.washingtonpost.com/rss/world",
"http://feeds.feedburner.com/time/world","https://www.cbsnews.com/latest/rss/world","https://www.vox.com/rss/world/index.xml",
"https://www.brookings.edu/topic/international-affairs/feed/","https://www.dailytelegraph.com.au/news/world/rss"`


### Copyright Tecton February 2,2019 All rights Reserved

### Please visit [my website](http://www.tecton.tk) or http://www.tecton.tk


### For Issues/bugs/Concerns Contact tectonroot@gmail.com or leave it at Issues
