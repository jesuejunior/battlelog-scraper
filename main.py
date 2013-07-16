__author__ = 'jesuejunior'

from splinter import Browser
from lxml import etree

url_profile = 'http://battlelog.battlefield.com/bf3/soldier/Juninn3k6/stats/327539077/ps3/'
html = ""

parser = etree.HTMLParser(remove_comments=True, encoding='utf-8')

def catch_metadata(xpath, tree):
    go_return = None

    go_return= ''
    elements = tree.xpath(xpath)
    for el in elements:
        for text in el.itertext(with_tail=True):
            clean_text = str(text)
            if clean_text:
                go_return += ' ' + clean_text

    return go_return


with Browser() as browser:
     # Visit URL
     browser.visit(url_profile)

     # Pagina pronta
     html = browser.html


tree = etree.fromstring(html, parser)

print catch_metadata('//table[contains(@class, "boxwideclean-table")][1]/tbody/tr[1]/td[2]', tree)