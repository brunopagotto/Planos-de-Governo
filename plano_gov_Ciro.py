# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 23:55:10 2022

@author: Usuario
"""

pip install pypdf2

# importa as bibliotecas necessárias
import PyPDF2
import re

# Abre o arquivo pdf 
# lembre-se que para o windows você deve usar essa barra -> / 
# lembre-se também que você precisa colocar o caminho absoluto
pdf_file = open('programa_Ciro.pdf', 'rb')

#Faz a leitura usando a biblioteca
read_pdf = PyPDF2.PdfFileReader(pdf_file)

# pega o numero de páginas
number_of_pages = read_pdf.getNumPages()

#lê a primeira página completa
page = read_pdf.getPage(0)

#extrai apenas o texto
page_content = page.extractText()

# faz a junção das linhas 
parsed = ''.join(page_content)

print("Sem eliminar as quebras")
print(parsed)

# remove as quebras de linha
parsed = re.sub('n', '', parsed)
print("Após eliminar as quebras")
print(parsed)

print("nPegando apenas as 20 primeiras posições")
novastring = parsed[0:20]
print(novastring)


pip install spacy
pip install WordCloud
pip install unidecode
pip install punctuation
pip install stopwords
pip install STOP_WORDS

import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')

import spacy

import matplotlib.pyplot as plt

from wordcloud import WordCloud

from unidecode import unidecode

from string import punctuation
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk import word_tokenize

from nltk.corpus import stopwords

from spacy.lang.pt.stop_words import STOP_WORDS


%matplotlib inline




def limpar_texto(text):
    
    # Colocando todas as letras do texto em caixa baixa:
    text = text.lower()
    # Excluindo citações com @:
    text = re.sub('@[^\s]+', '', text)
    # Excluindo acentuação das palavras:
    text = unidecode(text)
    # Excluindo html tags, como <strong></strong>:
    text = re.sub('<[^<]+?>','', text)
    # Excluindo os números:
    text = ''.join(c for c in text if not c.isdigit())
    # Excluindo URL's:
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+)|(http?://[^\s]+))', '', text)
    # Excluindo pontuação:
    text = ''.join(c for c in text if c not in punctuation)
    
    # Retornando o texto tratado tokenizado:
    
    return word_tokenize(text)


#lê todas as páginas completas
all_pages = ''
for i in range(number_of_pages):
    page_i = read_pdf.getPage(i)
    all_pages += page_i.extractText()
all_pages

texto_limpo = limpar_texto(all_pages)
print(texto_limpo)


# Removendo as stopwords utilizando a lista do nltk e do spacy:

sw = list(set(stopwords.words('portuguese') + list(STOP_WORDS)))

def remove_stop_words(texts, stopwords = sw):
      
    new_texts = list()
    
    for word in texts:
        if word not in stopwords:
            new_texts.append(''.join(word))

    return new_texts


texto_sem_stop_words = remove_stop_words(texto_limpo)
print(texto_sem_stop_words)

texto_sem_stop_words = remove_stop_words(texto_limpo, sw + ['programa','governo',
                                                            'politica','nao',
                                                            'publica','economica',
                                                            'brasil','pais',
                                                            'interesse','interesses',
                                                            'alem','sera','populacao',
                                                            'criacao','setores',
                                                            'pai','brasileira',
                                                            'brasileiro','politicas',
                                                            'vamos','d','publicas',
                                                            'plano','fi','hyphencase'])
print(texto_sem_stop_words)


!python -m spacy download pt

# Vamos criar uma função que mostra o texto original,
# a interpretação - da função - semântica dela e o lema

nlp = spacy.load("pt_core_news_sm")

def verificar_lemma(words):
    
    text = ""
    pos = ""
    lemma = ""
    for word in nlp(words):
        text += word.text + "\t"
        pos += word.pos_ + "\t"
        lemma += word.lemma_ + "\t"

    print(text)
    print(pos)
    print(lemma)
    
verificar_lemma('o sentido desta frase está errado')
verificar_lemma('você está se sentindo bem?')


# Vamos criar uma função que mostra o texto original e o stem de cada palavra

def verificar_radical(words):
    
    stemmer = nltk.stem.SnowballStemmer('portuguese')
    text = ""
    stem = ""
    
    for word in word_tokenize(words):

        text += word + "\t"
        stem += stemmer.stem(word) + "\t"
    
    print(text)
    print(stem)
    

verificar_radical('o sentido desta frase esta errado')
verificar_radical('você está se sentindo bem?')



def nuvem_palavras(textos):
    
    # Juntando todos os textos na mesma string
    todas_palavras = ' '.join([texto for texto in textos])
    # Gerando a nuvem de palavras
    nuvem_palvras = WordCloud(width= 800, height= 500,
                              max_font_size = 110,
                              collocations = False).generate(todas_palavras)
    # Plotando nuvem de palavras
    plt.figure(figsize=(24,12))
    plt.imshow(nuvem_palvras, interpolation='bilinear')
    plt.axis("off")
    plt.show()

print(' '.join(texto_sem_stop_words))
texto_pcb = ' '.join(texto_sem_stop_words)

# Construindo a nuvem de palavras:
nuvem_palavras(texto_sem_stop_words)
