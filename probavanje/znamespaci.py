import xml.etree.ElementTree as ET
import requests




url = 'https://bsi.si/_data/tecajnice/dtecbs-l.xml'

resp = requests.get(url) #posljemo rek+quest in dobimo vsebino strani, v tem primeru xml

root = ET.fromstring(resp.content)  #preberemo iz stringa

#xmlfile = 'sample.xml'
#secondfile = 'topnewsfeed.xml'


#tree = ET.parse(xmlfile)  # najprej odpremo xml, razclenimo
#root = tree.getroot() #



count = 0
for elm in root:#.findall("./"):
    print('elm: tag ', elm.tag,'elm.attrb: ',  elm.attrib)

    #print()
    count += 1
    if count == 200:
        break