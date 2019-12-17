import urlparse
import urllib
import random
import re
from BeautifulSoup import BeautifulSoup

url = "http://www.neoteo.com"
urls = [url]
visited = [url]
soup = None
toRead = False
numUrls = 0
numLinksFounded = 0

print "Urls: " + str(len(urls))


while numUrls < len(urls):
    #print "NumUrls: " + str(numUrls)
    htmlfile = urllib.urlopen(urls[numUrls])
    htmltext = htmlfile.read()    
    
    soup = BeautifulSoup(htmltext)
    #print urls[numUrls]
    
    if toRead == True:
        print soup.prettify()
    urls.pop(0)
       
    for link in soup.findAll('a', href=True):
        #raw = link['href']
        
        
        #print "http://" + str(domainWeb) + pathWeb
        urlWeb = urlparse.urljoin(url,link['href'])
        domainWeb = urlparse.urlparse(urlWeb).hostname
        pathWeb = urlparse.urlparse(urlWeb).path
        #newUrlWeb = "http://" + str(domainWeb) + str(pathWeb)
        #print url
        #print domainWeb
        if ("http://" + str(domainWeb)) == url:
            if urlWeb not in visited:
                urls.append(urlWeb)
                visited.append(urlWeb)
                numLinksFounded = numLinksFounded + 1  
                print numLinksFounded
        """
        if url in link['href'] and link['href'] not in visited:
            urls.append(link['href'])
            visited.append(link['href'])
            numLinksFounded = numLinksFounded + 1  
            print numLinksFounded
        """
        #print raw
        #print link['src']
        #print link.get('href')
        
       
    #print len(urls)
    
    
    #numUrls = numUrls + 1    
  
    
#extract_links_from_a()
#print visited
print numLinksFounded
print "End"


