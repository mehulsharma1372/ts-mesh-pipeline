"""This module is responsible for getting and processing meta data from the web."""
import requests
from bs4 import BeautifulSoup
import constants
import os


class Scraping:
    def __init__(self):
        self.dates = []
        self.titles = []
        self.links = []
        pass

    def get_raw_data(self, url):
        """This sends request to the web and get authentication."""
        S = requests.Session()
        meta_data = S.get(url)

        return meta_data.content

    def get_blogs(self):
        """Dig deep and get what we want, acts as a filter."""
        soup = BeautifulSoup(self.get_raw_data(constants.URL), constants.HTML_LIB)
        all_blogs = soup.find(constants.DIV_TAG, class_=constants.ALL_LINKS).find(
            constants.ANCHOR_TAG
        )[constants.HREF]
        blogs = self.get_raw_data(os.path.join(constants.URL + all_blogs))
        soup = BeautifulSoup(
            self.get_raw_data(os.path.join(constants.URL + all_blogs)),
            constants.HTML_LIB,
        )
        cont = soup.find(constants.DIV_TAG, class_=constants.VIEW_CONTENT)
        for div in cont:
            date = div.find(constants.DIV_TAG)
            if date == -1:
                pass
            else:
                self.dates.append(date.text)

            title = div.find(constants.ANCHOR_TAG)
            if title == -1:
                pass
            else:
                self.titles.append(title.text)
                self.links.append(os.path.join(constants.URL + title[constants.HREF]))
