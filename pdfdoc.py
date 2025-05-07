from pdf2docx import Converter


nome='C:\\Users\\edupo\\Desktop\\Mark of the Fool 01\\Mark of the Fool 01'
arquivo_pdf=nome +'.pdf'
arquivo_docx=nome +'.docx'


converter=Converter(arquivo_pdf)
converter.convert(arquivo_docx)
converter.close()

print('Fim!')