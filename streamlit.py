#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 23:32:42 2021

@author: yadavrupeshmohanlal
"""
import spacy_streamlit

import numpy as np
#from flasgger import Swagger
import streamlit as st 

from IPython.core.display import display, HTML
import streamlit as st
import wikipedia
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import conlltags2tree, tree2conlltags
from pprint import pprint
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
from bs4 import BeautifulSoup
import requests
import re


from PIL import Image

#app=Flask(__name__)
#Swagger(app)



#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(data2):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    data=(wikipedia.summary(data2))
    def preprocess(sentence):
        sentence = nltk.word_tokenize(sentence)
        sentence = nltk.pos_tag(sentence)
        return sentence
    sentence = preprocess(data)
    pattern = 'NP: {<DT>?<JJ>*<NN>}'
    cp = nltk.RegexpParser(pattern)
    cs = cp.parse(sentence)

    iob_tagged = tree2conlltags(cs)
    nlp = en_core_web_sm.load()
    doc=nlp(data)
    #pprint([(X.text, X.label_) for X in doc.ents])
    ny_bb=data
    article = nlp(ny_bb)

    labels = [x.label_ for x in article.ents]
    #Counter(labels)
    items = [x.text for x in article.ents]
    #Counter(items).most_common(9)
    sentences = [x for x in article.sents]
    #print(sentence)
    
    default_text = data
    models = ["en_core_web_sm"]
    spacy_streamlit.visualize(models,default_text,sentence)
    



def main():
    st.title("Scraper")
    html_temp = """
    <div style="background-color:red;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Scraper </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    data2 = st.text_input("Type page to scrape of wikipedia example America","Type Here")
    
    #result=""
    if st.button("Scrap"):
        predict_note_authentication(data2)
    
    if st.button("About"):
        st.text("Yadav RupeshKumar Mohanlal")
        st.text("Built with Streamlit and python")

if __name__=='__main__':
    main()
