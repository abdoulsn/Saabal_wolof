# For jupyter loader et warnings

from tqdm import tqdm
import warnings 
warnings.filterwarnings("ignore")

#Python numpy et pandas respctivement pout Lin Algebra et dataframe
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 1000)
pd.set_option('display.max_rows', 10000)
pd.set_option('display.width', 1000)

# url spiders 
from urllib.parse import urlencode, urlparse, parse_qs
from lxml.html import fromstring
from requests import get
import urllib3
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen 
from lxml.html import fromstring
import requests
from itertools import cycle
import traceback

import nltk
