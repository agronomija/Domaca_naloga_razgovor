import requests

url = 'https://bsi.si/_data/tecajnice/dtecbs-l.xml'

def loadRSS(url):
    # url of rss feed
    url = url
    # creating HTTP response object from given url
    resp = requests.get(url)

    # saving the xml file
    with open('topnewsfeed.xml', 'wb') as f:
        f.write(resp.content)


#if __name__ == '__main__':
# creating HTTP response object from given url
    #resp = requests.get(url)
    #print(resp.content) #resp.content kar je zapisano na netu v xml je potem tu dostopno


resp = requests.get(url)
#print(resp.content)
for row in resp.content:
    print(row)