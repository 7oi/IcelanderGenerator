# -*- coding: utf-8 -*-
import json
import os
import random
import requests

from lxml import html


class NameScraper(object):
    WIKI_FORMAT = u'https://is.wikipedia.org/{}'
    WIKI_FEMALES = u'wiki/Listi_yfir_%C3%ADslensk_eiginn%C3%B6fn_kvenmanna'
    WIKI_MALES = u'wiki/Listi_yfir_íslensk_eiginnöfn_karlmanna'
    WIKI_NAME_XPATH = u'//div[@id="mw-content-text"]/div/ul/li/a'
    WIKI_GENETIVE_XPATH = u'//*[contains(text(), "Eignarfall")]'
    FILE_NAME = 'icelandic_names.json'
    names = {
        'female': [],
        'male': []
    }
    non_genetive_names = {
        'female': [],
        'male': []
    }

    def get_name(self, item):
        """Get name for xpath item

        Arguments:
            item {object} -- Xpath object for name

        Returns:
            tuple | None -- Returns tuple with (name, genetive name) or None if genetive name is not found
        """

        url = item.attrib.get('href')
        name = item.text
        genetive_name = name
        name_page = requests.get(self.WIKI_FORMAT.format(url))
        name_page_tree = html.fromstring(name_page.content)
        try:
            neighbour = name_page_tree.xpath(self.WIKI_GENETIVE_XPATH)[0]
            genetive_name = neighbour.getparent().getparent().getchildren()[1].text
        except IndexError:
            return None
        return (name, genetive_name)

    def scrape_wiki_for_names(self):
        """Scrape icelandic wikipedia page for names.
        """

        for gender, path in [('female', self.WIKI_FEMALES), ('male', self.WIKI_MALES)]:
            page = requests.get(self.WIKI_FORMAT.format(path))
            tree = html.fromstring(page.content)
            items_in_name_xpath = tree.xpath(self.WIKI_NAME_XPATH)[0:-2]
            for item in items_in_name_xpath:
                name = self.get_name(item)
                if name is None:
                    name = item.text
                    print(u'No genetive version found. Not adding {}'.format(name))
                    self.non_genetive_names[gender].append(name)
                    continue
                print(u"Adding: ({}, {}) to {} names".format(name[0], name[1], gender))
                self.names[gender].append(name)

    def save_names_to_file(self):
        """Saves names to a json file
        """

        file_path = os.path.dirname(__file__)
        with open(os.path.join(file_path, self.FILE_NAME), 'w') as outfile:
            json.dump(self.names, outfile, indent=2)

        with open(os.path.join(file_path, 'rejects.json'), 'w') as outfile:
            json.dump(self.non_genetive_names, outfile, indent=2)

    def update_names(self):
        self.scrape_wiki_for_names()
        self.save_names_to_file()
