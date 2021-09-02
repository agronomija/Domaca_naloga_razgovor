import xml.etree.ElementTree as ET
import requests

def pretvorba(date):
    """
    Funkcija sprejme datum kot argument in vrne letnico
    :param datum: string, v obliki '2007-09-01
    :return: vrne letnico v stringu
    """
    return date[:4]


def get_tecaji(year):
    """

    :param datum: string npr. 2007
    :return: vrne dva slovarja (GBP, USD), datum (v obliki: '2007-09-09') kot ključe in tečaj na tisti dan kot vrednost
    """
    url = 'https://bsi.si/_data/tecajnice/dtecbs-l.xml'

    resp = requests.get(url)  # posljemo request in dobimo vsebino strani, v tem primeru xml
    root = ET.fromstring(resp.content) #resp.content je string, zato uporabimo ET.fromstring (preberemo, razclenimo xml)

    GBP = dict()
    USD = dict()

    for tecajnica in root:
        cel_datum = tecajnica.attrib['datum'] #cel datum, ki ga dobimo iz attributa tecajnice v obliki '2007-09-01'
        datum = pretvorba(cel_datum)  # tukaj bomo preverili ali je datum pravi

        if int(year) == int(datum): #ce sta si letnica, ki je vnesena kot atribut v funkcijo
            # in letnica vsake posamezne tecajnice enaki, potem zapisemo v slovarja naslednje vrednosti in kljuce
            for tecaj in tecajnica:
                if tecaj.get('oznaka') == 'USD':
                    #print('USD: ', tecaj.text)
                    USD[cel_datum] = tecaj.text

                if tecaj.get('oznaka') == 'GBP':
                    #print('GBP: ', tecaj.text)
                    GBP[cel_datum] = tecaj.text
    return GBP, USD #vrnemo dva slovarja, v vsakem pod kljuci shranjeni datumi, pod vrednostjo pa vrednost valute na tisti dan

#print(get_tecaji('2009'))

def get_vse_valute():
    """

    :return: po abecedi urejen seznam vseh valut (oznak: USD), ki so objavljene v tecajnici na banki slovenije
    """
    url = 'https://bsi.si/_data/tecajnice/dtecbs-l.xml'

    resp = requests.get(url)  # posljemo request in dobimo vsebino strani, v tem primeru xml
    root = ET.fromstring(resp.content)

    vsi_tecaji = set()

    for tecaj in root[0]: #gremo cez prvo tecajnico in iz atributa vzamemo valuto in jih shranjujemo v slovar.

        valuta = tecaj.get('oznaka') #iz attributa dobimo oznako valute.
        vsi_tecaji.add(valuta) #dodamo valuto v set
    return sorted(list(vsi_tecaji)) #funkcija vrne seznam vseh valut, sortiranih po abecedi




def get_casovna_obdobja():
    """

    :return: vrne vse letnice, po katerih je banka slovenije beležila tečaje. urejen seznam po velikosti
    """
    url = 'https://bsi.si/_data/tecajnice/dtecbs-l.xml'

    resp = requests.get(url)  # posljemo request in dobimo vsebino strani, v tem primeru xml
    root = ET.fromstring(resp.content)

    vsi_datumi = set()
    for tecajnica in root:
        cel_datum = tecajnica.attrib['datum'] #cel datum, ki ga dobimo iz attributa tecajnice v obliki '2007-09-01'
        datum = pretvorba(cel_datum)
        vsi_datumi.add(datum)

    return sorted(list(vsi_datumi)) #vrne seznam vseh datumov, sortiranih od najzgodnejsega do zadnjega




def get_tecaji_vsi(year, valuta):
    """
    Uporabimo, če nas zanima letno nihanje vrednosti tečaja za določeno valuto. izberemo leto in valuto
    :param datum: string 2007-09-01
    :param valuta: string kratice neke valute
    :return: vrne slovar z datumi ('2007-09-09') kot ključi in vrednostjo tečaja kot vrednostjo,
    za določeno leto, ki smo ga določili v atributu year
    """
    leto = pretvorba(year) #iz attributa datum izluščimo letnico
    url = 'https://bsi.si/_data/tecajnice/dtecbs-l.xml'

    resp = requests.get(url)  # posljemo request in dobimo vsebino strani, v tem primeru xml
    root = ET.fromstring(resp.content) #resp.content je string, zato uporabimo ET.fromstring (preberemo, razclenimo xml)

    EUR = dict()


    for tecajnica in root:
        cel_datum = tecajnica.attrib['datum'] #cel datum, ki ga dobimo iz attributa tecajnice v obliki '2007-09-01'
        datum = pretvorba(cel_datum)  # tukaj bomo preverili ali je datum pravi

        if int(datum) == int(year):
            for tecaj in tecajnica:
                if tecaj.get('oznaka') == valuta:
                    #print(f'{valuta} ', tecaj.text)
                    EUR[cel_datum] = tecaj.text


    return EUR #vrnemo en slovar z datumi kot ključi in vrednostmi kot vrednosti valute

#print(sorted(get_tecaji_vsi('2007', 'HRK').keys()))

x = get_tecaji_vsi('2007', 'HRK')
print(x)

print('HRK za datum 2007-04-04: ', x.get('2007-04-04'))


def spremeni_letnico_datuma(year, seznam_datumov):
    """

    :param year: npr string '2007'
    :param seznam_datumov: seznam datumov v taki obliki: '2007-10-10'
    :return: vrne nov seznam istih datumov samo da imajo letnico tako kot smo si jo izbrali (year)
    """
    nov_seznam = []
    for datum in seznam_datumov:
        datum = year + datum[4:]
        nov_seznam.append(datum)
    return nov_seznam

"""
x = '2000-10-10'
x = '1999' + x[4:]
print(x)
"""