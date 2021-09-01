import xml.etree.ElementTree as ET
import requests

def pretvorba(datum):
    return datum[:4]


def get_tecaji(year):
    leto = pretvorba(year)
    url = 'https://bsi.si/_data/tecajnice/dtecbs-l.xml'

    resp = requests.get(url)  # posljemo request in dobimo vsebino strani, v tem primeru xml
    root = ET.fromstring(resp.content) #resp.content je string, zato uporabimo ET.fromstring (preberemo, razclenimo xml)

    EUR = dict()
    GBP = dict()
    USD = dict()

    for tecajnica in root:
        cel_datum = tecajnica.attrib['datum'] #cel datum, ki ga dobimo iz attributa tecajnice v obliki '2007-09-01'
        datum = pretvorba(cel_datum)  # tukaj bomo preverili ali je datum pravi

        if int(datum) == 2010:
            for tecaj in tecajnica:
                if tecaj.get('oznaka') == 'USD':
                    print('USD: ', tecaj.text)
                    USD[cel_datum] = tecaj.text

                if tecaj.get('oznaka') == 'GBP':
                    print('GBP: ', tecaj.text)
                    GBP[cel_datum] = tecaj.text
    return GBP, USD #vrnemo dva slovarja, v vsakem pod kljuci shranjeni datumi, pod vrednostjo pa vrednost valute na tisti dan


def get_vse_valute():
    url = 'https://bsi.si/_data/tecajnice/dtecbs-l.xml'

    resp = requests.get(url)  # posljemo request in dobimo vsebino strani, v tem primeru xml
    root = ET.fromstring(resp.content)

    vsi_tecaji = set()

    for tecaj in root[0]: #gremo cez prvo tecajnico in iz atributa vzamemo valuto in jih shranjujemo v slovar.

        valuta = tecaj.get('oznaka') #iz attributa dobimo oznako valute.
        vsi_tecaji.add(valuta) #dodamo valuto v set
    return sorted(list(vsi_tecaji)) #funkcija vrne seznam vseh valut




def get_casovna_obdobja():
    url = 'https://bsi.si/_data/tecajnice/dtecbs-l.xml'

    resp = requests.get(url)  # posljemo request in dobimo vsebino strani, v tem primeru xml
    root = ET.fromstring(resp.content)

    vsi_datumi = set()
    for tecajnica in root:
        cel_datum = tecajnica.attrib['datum'] #cel datum, ki ga dobimo iz attributa tecajnice v obliki '2007-09-01'
        datum = pretvorba(cel_datum)
        vsi_datumi.add(datum)

    return sorted(list(vsi_datumi))




def get_tecaji_vsi(year, valuta):
    leto = pretvorba(year)
    url = 'https://bsi.si/_data/tecajnice/dtecbs-l.xml'

    resp = requests.get(url)  # posljemo request in dobimo vsebino strani, v tem primeru xml
    root = ET.fromstring(resp.content) #resp.content je string, zato uporabimo ET.fromstring (preberemo, razclenimo xml)

    EUR = dict()


    for tecajnica in root:
        cel_datum = tecajnica.attrib['datum'] #cel datum, ki ga dobimo iz attributa tecajnice v obliki '2007-09-01'
        datum = pretvorba(cel_datum)  # tukaj bomo preverili ali je datum pravi

        if int(datum) == 2010:
            for tecaj in tecajnica:
                if tecaj.get('oznaka') == valuta:
                    print(f'{valuta} ', tecaj.text)
                    EUR[cel_datum] = tecaj.text


    return EUR #vrnemo en slovar z datumi kot ključi in vrednostmi kot vrednosti valute

print(sorted(get_tecaji_vsi('2007', 'USD').keys()))
