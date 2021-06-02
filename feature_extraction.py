from urllib.parse import urlparse, urlsplit, unquote
from urllib import parse
import os
import re
import pandas as pd
from os.path import splitext
from utils import shannon
from utils import char_continuity_rate
from utils import count_symbols
from utils import conseq_digits


class URL:
    def __init__(self, str):
        self.url = str
        self.domain = urlparse(self.url).netloc
        self.path = urlparse(self.url).path
        self.params = urlparse(self.url).params
        self.query = urlparse(self.url).query
        self.fragment = urlparse(self.url).fragment
        self.filename = os.path.splitext(self.path)[0]
        self.extension = os.path.splitext(self.path)[1]

    def feature_extraction(self):
        domainlength = len(self.domain)
        domain_tokens = re.split('\W+', self.domain)
        domain_token_count = len(domain_tokens)
        avgdomaintokenlen = -1 if domain_token_count == 0 else len(''.join(domain_tokens)) / domain_token_count
        NumberofDotsinURL = self.url.count('\.')
        Entropy_Domain = shannon(self.domain)
        URLQueries_variable = len(self.query)
        ArgUrlRatio = -1 if len(self.url) == 0 else len(self.query) / len(self.url)
        CharacterContinuityRate = -1 if domainlength == 0 else char_continuity_rate(self.domain, domainlength)
        delimeter_path = self.path.count('-') + self.path.count('.') + self.path.count('_') + self.path.count('/')
        SymbolCount_URL = count_symbols(self.url)
        SymbolCount_FileName = count_symbols(self.filename)
        NumberRate_Extension = -1 if len(self.extension) == 0 else conseq_digits(self.extension) / len(self.url)
        Entropy_Extension = shannon(self.extension)
        NumberRate_AfterPath = -1 if len(self.query) == 0 else conseq_digits(self.query) / len(self.url)

        return {
            'domainlength': [domainlength], 'domain_token_count': [domain_token_count],
            'avgdomaintokenlen': [avgdomaintokenlen], 'Entropy_Domain': [Entropy_Domain],
            'NumberofDotsinURL': [NumberofDotsinURL], 'URLQueries_variable': [URLQueries_variable],
            'ArgUrlRatio': [ArgUrlRatio], 'delimeter_path': [delimeter_path], 'SymbolCount_URL': [SymbolCount_URL],
            'SymbolCount_FileName': [SymbolCount_FileName], 'CharacterContinuityRate': [CharacterContinuityRate],
            'NumberRate_Extension': [NumberRate_Extension], 'Entropy_Extension': [Entropy_Extension],
            'NumberRate_AfterPath': [NumberRate_AfterPath]}
