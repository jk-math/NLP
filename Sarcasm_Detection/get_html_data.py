import os
import re
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import html5lib

def deEmojify(text): # thank you https://stackoverflow.com/users/6579239/abdul-razak-adam
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)

def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = ''
    for x in raw_html:
        cx = re.sub(cleanr, '', str(x))
        cx = cx.replace(u'\xa0', u' ')
        cx = cx.lstrip()
        cleantext += deEmojify(cx) + ' '
    return cleantext.lower() # the tokenizer converts to lowercase as a default

def get_html_data(url):
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        stream = urlopen(req,timeout = 5)
        html = stream.read()
        stream.close()
        html = html.decode('utf-8')
        soup = BeautifulSoup(html, 'html5lib')
        contents = clean_html(soup.find_all('h1') + soup.find_all('p'))
        return contents
    except:
        return None
