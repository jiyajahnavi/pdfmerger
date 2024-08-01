import PyPDF2

pdFiles = ["1.pdf","2.pdf"]
merger = PyPDF2.PdfMerger()
for filename in pdFiles:
    pdfFiles = open(filename,'rb')
    pdfReader = PyPDF2.PdfReader(pdfFiles)
    merger.append(pdfReader)
pdfFiles.close()
merger.write('merged pdf')
