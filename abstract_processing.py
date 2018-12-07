# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 18:02:45 2018

@author: Jacques

In this file, we pre-process the abstracts and titles

Bon tuto sur le text processing: https://towardsdatascience.com/introduction-to-natural-language-processing-for-text-df845750fb63
"""
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    from nltk.corpus import stopwords
    from nltk.stem import WordNetLemmatizer
    from nltk.corpus import wordnet

def tokenize(data):
    """transforms the title and abstract features into lists of words and returns the modified data object"""
    
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words("english")) # les mots que l'on retire
    for i in range(10):
        stop_words.add(str(i)) # il y a des chiffres qui trainent dans les titres des articles aussi
        
    i=0
    for item in data : 
        i+=1
        title_words=nltk.word_tokenize(item[2])
        title_words_=[lemmatizer.lemmatize(word) for word in title_words if not word in stop_words]
        
        item[2]=title_words_
        abstract_words=nltk.word_tokenize(item[5])
        abstract_words_=[word for word in abstract_words if not word in stop_words]
        item[5]=abstract_words_

    return data

def tok(string):
    """takes a string and returns a list of its tokens
    1 truc à changer : ce serait bien de sortir le lemmatizer et stop words pour ne pas les recréer à chaque fois..."""
    
    
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words("english")) # les mots que l'on retire
    for i in range(10):
        stop_words.add(str(i)) # il y a des chiffres qui trainent dans les titres des articles aussi
    
    title_words=nltk.word_tokenize(string)
    title_words_=[lemmatizer.lemmatize(word) for word in title_words if not word in stop_words]
        
    return title_words_

def titles_bow(data):
    """takes the preprocessed data as input and returns the bag of words matrix for titles"""
    titles=[item[2] for item in data]
    count_vectorizer = CountVectorizer( lowercase=False,
      preprocessor=lambda x: x,tokenizer=tok)
    bag_of_words = count_vectorizer.fit_transform(titles)
    feature_names = count_vectorizer.get_feature_names()
    
    print(feature_names)
    
    return bag_of_words