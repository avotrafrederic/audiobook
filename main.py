#-*- encoding:UTF-8 -*-
#! env/Scripts/python
from include.Pdf import PDF
filename = input("Entrez le fichier pdf: ")
voice = int(input('Veuillez choisir le genre de voi que vous voulez [masculine (0) | feminine (1)]: '))
PDF.main(fileName=filename,voice=voice)