import random
import datetime
import requests
import json

from lxml import html


class NameScraper(object):
    WIKI_FORMAT = 'https://is.wikipedia.org/{}'
    WIKI_FEMALES = 'wiki/Listi_yfir_%C3%ADslensk_eiginn%C3%B6fn_kvenmanna'
    WIKI_MALES = 'wiki/Listi_yfir_íslensk_eiginnöfn_karlmanna'
    WIKI_NAME_XPATH = '//div[@id="mw-content-text"]/div/ul/li/a'
    WIKI_GENETIVE_XPATH = '//*[contains(text(), "Eignarfall")]'
    FILE_NAME = 'icelandic_names.json'
    names = {
        'female': [],
        'male': []
    }

    def update_names(self):
        for gender, path in [('female', self.WIKI_FEMALES), ('male', self.WIKI_MALES)]:
            page = requests.get(self.WIKI_FORMAT.format(path))
            tree = html.fromstring(page.content)
            names = tree.xpath(self.WIKI_NAME_XPATH)[0:-2]
            for item in names[0:20]:
                url = item.attrib.get('href')
                name = item.text
                genetive_name = name
                name_page = requests.get(self.WIKI_FORMAT.format(url))
                name_page_tree = html.fromstring(name_page.content)
                try:
                    neighbour = name_page_tree.xpath(self.WIKI_GENETIVE_XPATH)[0]
                    genetive_name = neighbour.getparent().getparent().getchildren()[1].text
                except IndexError:
                    print('No genetive version found. Not adding {}'.format(name))
                    continue
                print("Added: ({}, {}) to {} names".format(name, genetive_name, gender))
                self.names[gender].append((name, genetive_name))

    def save_names_to_file(self):
        with open(self.FILE_NAME, 'w') as outfile:
            json.dump(self.names, outfile)
