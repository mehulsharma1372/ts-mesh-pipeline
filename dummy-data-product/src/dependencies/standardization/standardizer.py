"""This Module takes raw data from scraper.py and modify it to the required csv format."""

import constants
import sys
import pandas as pd

sys.path.insert(0, constants.PATH)
import pandas as pd
from scraper import Scraping


class CsvOperations:
    def __init__(self):
        self.scraping = Scraping()
        self.final_dict = {}

    def data_frame(self):
        """This makes a dict that is to be added as dataframe."""
        self.scraping.get_blogs()
        self.final_dict[constants.TITLE] = self.scraping.titles
        self.final_dict[constants.LINKS] = self.scraping.links
        self.final_dict[constants.DATE] = self.scraping.dates
        return self.final_dict

    def to_csv(self):
        """Adds that data frame to the csv file."""
        self.data_frame()
        dataframe = pd.DataFrame(self.final_dict)
        with open(constants.CSV_FILE_NAME, constants.WRITE) as csv:
            dataframe.to_csv(constants.CSV_FILE_NAME, index=False)
