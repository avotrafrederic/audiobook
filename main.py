#-*- encoding:UTF-8 -*-
#! /usr/bin/python
from include.Pdf import PDF
import pyfiglet
import colored
import subprocess

def main():
    subprocess.run("clear",shell=True)
    title = pyfiglet.figlet_format("PDF AUDIOBOOK")
    print(f"{colored.fg(37)} {title}".center(20))
    user_input = input(f"{colored.fg(6)}Entrez le fichier pdf: ")
    filename = f"{user_input}.pdf"
    try:
        voice = int(input('Veuillez choisir le genre de voix que vous voulez [masculine (0) | feminine (1)]: '))
    except ValueError as e:
        print("Merci de saisir entre 0 ou 1")
    else:
        PDF.main(fileName=filename,voice=voice)
if __name__ == "__main__":
    main()