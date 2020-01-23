import urllib
from bs4 import BeautifulSoup

def ScrapeWebsite(URL, TAG, HTML_ELEMENT):
    Recv = BeautifulSoup(urllib.request.urlopen(URL), "html.parser").find(TAG, {HTML_ELEMENT}).get_text()
    return str(Recv)

def POST(URL, Headers, Data):
    _Data = str(Data)
    Recv = urllib.request.urlopen(URL, data=_Data).read()
    return Recv

def GET(URL, Headers, Data):
    _Data = str(Data)
    Recv = urllib.request.urlopen(URL, data=_Data).read()
    return Recv