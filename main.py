#-*- encoding:UTF-8 -*-
#! /usr/bin/puthon
from include.Pdf import PDF
import pyfiglet
import colored
import subprocess
def main():
    subprocess.run("clear",shell=True)
    title = pyfiglet.figlet_format("PDF AUDIOBOOK")
    print(f"{colored.fg(37)} {title}".center(20))
    filename = input(f"{colored.fg(6)}Entrez le fichier pdf: ")
    voice = int(input('Veuillez choisir le genre de voi que vous voulez [masculine (0) | feminine (1)]: '))
    PDF.main(fileName=filename,voice=voice)

if __name__ == "__main__":
    main()