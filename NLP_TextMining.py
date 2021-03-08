# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 11:47:16 2021
#Reference
#https://towardsdatascience.com/gentle-start-to-natural-language-processing-using-python-6e46c07addf3
@author: jmathew
"""

import nltk
#nltk.download()

#First, we will grab a webpage and analyze the text to see what the page is about.
import urllib.request
response =  urllib.request.urlopen('https://en.wikipedia.org/wiki/Natural_language_processing')
html = response.read()
print(html)

#We will use Beautiful Soup which is a Python library for pulling data out of HTML and XML files. We will use beautiful soup to clean our webpage text of HTML tags.
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'html5lib')
text = soup.get_text(strip = True)
print(text)

#Now we have clean text from the crawled web page, let’s convert the text into tokens.
tokens = [t for t in text.split()]
print(tokens)

#Count word Frequency
from nltk.corpus import stopwords
sr= stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('english'):
        
        clean_tokens.remove(token)
freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print(str(key) + ':' + str(val))
freq.plot(20, cumulative=False)