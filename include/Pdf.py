#-*- encoding:UTF-8 -*-
import pyttsx3
import PyPDF2                            
class PDF:
    @classmethod
    def openi_file(cls,file_name):
        pdf_file = open(r"{}".format(file_name),'rb')
        return pdf_file

    @classmethod
    def read_pdf(cls,file_name):
        reader = PyPDF2.PdfReader(cls.openi_file(file_name), strict=False)
        return reader

    @classmethod
    def page_number(cls,file_name):
        return cls.read_pdf(file_name).getNumPages()

    @classmethod
    def main(cls,fileName, voice):
        engine = pyttsx3.init()
        for i in range(0, 1):
            page = cls.read_pdf(file_name=fileName).pages[i]
            page_content =page.extract_text()
            newrate = newvolume = 200
            engine.setProperty('rate',newrate)
            engine.setProperty('volume',newvolume)
            voices = engine.getProperty('voices')
            engine.setProperty('voice',voices[voice].id)
            engine.say(page_content)
            engine.save_to_file(page_content,f"{fileName}.mp3")
            engine.runAndWait()
            engine.stop()

if __name__ == "__main__":
    print("Please run the main files !")
            