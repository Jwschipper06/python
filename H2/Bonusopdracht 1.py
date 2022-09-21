from tkinter import W
import numpy as np
alfabet1 = open("alfabet.txt")
tekst1 = open("genesis.txt")
tekst = tekst1.read()
alfabet = alfabet1.read()
tekst = tekst.replace(',', '')
tekst = tekst.replace(' ', '')
tekst = tekst.replace('.', '')
tekst = tekst.replace('?', '')
tekst = tekst.replace('!', '')
tekst = tekst.replace(':', '')
tekst = tekst.replace(';', '')
tekst = tekst.replace('\n', '')
tekst = tekst.replace('\t', '')
tekst = tekst.lower()

for x in alfabet:
    a = tekst.count(x)
    a = a/len(tekst)*100
    print (x, ":", a,"%")

