#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 23:32:42 2021

@author: yadavrupeshmohanlal
"""
import spacy_streamlit

#from flasgger import Swagger
import streamlit as st 

import wikipedia
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import conlltags2tree, tree2conlltags
import spacy
from spacy import displacy
import en_core_web_sm



#app=Flask(__name__)
#Swagger(app)



#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(data2):
    
    """Using Nltk , Spacy ,Streamlit to Perform 
    Named Entity Recognition on scrapped data 
    and extract entities like city, person, 
    organisation, Date, Geographical Entity, Product etc.  
    
    data2= page name of wikipedia to extract data
    
    """
    
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger') 
    data=(wikipedia.summary(data2))
    
    #Then we apply word tokenization and part-of-speech tagging to the sentence.
    
    def preprocess(sentence):
        sentence = nltk.word_tokenize(sentence)
        sentence = nltk.pos_tag(sentence)
        return sentence
    sentence = preprocess(data)
    
    #Creating Chunk rule for text phrasing
    #Our chunk pattern consists of one rule, 
    #that a noun phrase, NP, should be formed whenever the chunker 
    #finds an optional determiner, DT, followed by any 
    #number of adjectives, JJ, and then a noun, NN.
    
    pattern = 'NP: {<DT>?<JJ>*<NN>}'
    
    #create a chunk parser and test it on our sentence
    cp = nltk.RegexpParser(pattern)
    cs = cp.parse(sentence)
    
    
    #IOB tags  to represent chunk structures in files, and we will also be using this format.
    
    iob_tagged = tree2conlltags(cs)
    
    #Use of Spacy
    
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
    
    #Use of spacy_streamlit
    #The package includes building blocks that call 
    #into Streamlit and set up all the required elements for you. 
    default_text = data
    models = ["en_core_web_sm"]
    spacy_streamlit.visualize(models,default_text,sentence)
    



def main():
    #Html for styling
    st.title("Scraper")
    html_temp = """
    <div style="background-color:red;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Scraper </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    data2 = st.text_input("Only wikipedia page allowed,Type page name from wikipedia to do scrapping and Perform Named Entity Recognition on scrapped data and extract entities like city, person, organisation, Date, Geographical Entity, Product etc.","Type Here")
    
    #Creating the predict button
    if st.button("Scrap"):
        predict_note_authentication(data2)
        
    #Creating about section
    if st.button("About"):
        st.text("Yadav RupeshKumar Mohanlal")
        st.text("Built with Streamlit and python")

if __name__=='__main__':
    main()
