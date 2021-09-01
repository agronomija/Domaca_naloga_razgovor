import xml.etree.ElementTree as ET
import requests

def pretvorba(datum):
    return datum[:4]

print(pretvorba('2007-06-9'))
url = 'https://bsi.si/_data/tecajnice/dtecbs-l.xml'

resp = requests.get(url) #posljemo rek+quest in dobimo vsebino strani, v tem primeru xml

root = ET.fromstring(resp.content)  #preberemo iz stringa

#DtecBS xmlns="http://www.bsi.si" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

ns = {'tecajnica': "http://www.bsi.si"}

print(root.tag, root.attrib)


EUR = dict()
GBP = dict()
USD = dict()


st = 0
for tecajnica in root:
    cel_datum = tecajnica.attrib['datum']  #dobimo datum iz tecajnice
    datum = pretvorba(cel_datum)  # tukaj bomo preverili ali je datum pravi
    print(pretvorba(datum))
    print(cel_datum)

    print(tecajnica.tag, cel_datum)
    st += 1
    if st == 1000:
        break

    if int(datum) < 2010:
        continue

    elif int(datum) == 2010:
        for tecaj in tecajnica:
            if tecaj.get('oznaka') == 'USD':
                print('USD: ', tecaj.text)
                USD[datum] = tecaj.text

            if tecaj.get('oznaka') == 'GBP':
                print('GBP: ', tecaj.text)
                GBP[datum] = tecaj.text
    else:
        break

print(len(USD))


for datum, tecaj in USD.items():
    print(datum, tecaj)

print('--------TUKEJ SE ZACNE FUNKCIJA----------')

def get_tecaji(year):

    leto = pretvorba(year)
    url = 'https://bsi.si/_data/tecajnice/dtecbs-l.xml'

    resp = requests.get(url)  # posljemo request in dobimo vsebino strani, v tem primeru xml

    root = ET.fromstring(resp.content)

    EUR = dict()
    GBP = dict()
    USD = dict()

    for tecajnica in root:
        cel_datum = tecajnica.attrib['datum']
        datum = pretvorba(cel_datum)  # tukaj bomo preverili ali je datum pravi
        #print(pretvorba(datum))
        #print(cel_datum)#

        #print(tecajnica.tag, datum)


        #if int(datum) < 2010:
         #   continue

        if int(datum) == 2010:
            for tecaj in tecajnica:
                if tecaj.get('oznaka') == 'USD':
                    print('USD: ', tecaj.text)
                    USD[cel_datum] = tecaj.text

                if tecaj.get('oznaka') == 'GBP':
                    print('GBP: ', tecaj.text)
                    GBP[cel_datum] = tecaj.text
        #else:
         #   break

    return GBP, USD

"""
    st = 0
    for tecajnica in root:
        datum = tecajnica.attrib['datum']  # tukaj bomo preverili ali je datum pravi

        #print(tecajnica.tag, datum) teg vrne ime taga, attrib pa vrne vse attribute, ki jih ima tag. vrne jih v obliki slovarja
        st += 1
        if st == 20:
            break
        for tecaj in tecajnica:
            if tecaj.get('oznaka') == 'USD':
                #print('USD: ', tecaj.text)
                USD[datum] = tecaj.text

            if tecaj.get('oznaka') == 'GBP':
                #print('GBP: ', tecaj.text)
                GBP[datum] = tecaj.text
"""

gbp, usd = get_tecaji('2011')
for datum, tecaj in gbp.items():
    print(datum, tecaj)

print(len(gbp))
print(len(usd))