from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

import nltk
#nltk.download()

import spacy
nlp = spacy.load("en_core_web_sm") # 토크나이징을 위한 spacy 라이브러리 로드

import konlpy
from konlpy.tag import Okt
#okt = Okt()  # 한국어 토크나이징을 위한 konlpy 라이브러리 로드

from konlpy.corpus import kolaw
from konlpy.corpus import kobill

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from bs4 import BeautifulSoup