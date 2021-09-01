import requests
import xml.dom.minidom

url = 'https://bsi.si/_data/tecajnice/dtecbs-l.xml'

resp = requests.request('GET', url)


r = resp.text

xmlparse = xml.dom.minidom.parseString(r)
print(xmlparse)

xml = xmlparse.toprettyxml()
print(xml)

