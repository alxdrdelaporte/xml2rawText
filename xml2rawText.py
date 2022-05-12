#!/usr/lib/python3.9
# -*-coding:utf-8 -*
"""
Alexander DELAPORTE - CRLAO
https://tekipaki.hypotheses.org/
https://github.com/alxdrdelaporte/
https://gitlab.com/alxdrdelaporte/

Extraire le texte brut d'éléments XML avec ElementTree et BeautifulSoup
"""

import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup as soup

# Fichier d'entrée
input_path = "./data.xml"

with open(input_path, "r", encoding="utf-8") as data:
    # Parsing XML avec ElementTree
    tree = ET.parse(data)
    root = tree.getroot()
    print("***Extraction du texte avec xml.etree.ElementTree***\n")
    print("Tous les descendants :\n")
    print(" ".join([child.text for child in root.iter()]))
    print("Descendants 'w' uniquement :\n")
    print(" ".join([child.text for child in root.iter("w")]))
    # Parsing XML avec bs4.BeautifulSoup
    print("***Extraction du texte avec bs4.BeautifulSoup***\n")
    ma_soupe = soup(data, "lxml")
    print("Toute l'arborescence :\n")
    print(ma_soupe.text)
    print("Descendants 'w' uniquement :\n")
    print(" ".join([w.contents[0] for w in ma_soupe.find_all("w")]))
