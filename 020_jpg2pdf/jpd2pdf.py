import fitz

doc = fitz.open()
imgdoc = fitz.open("2.jpeg")
pdfbytes = imgdoc.convertToPDF()
imgpdf = fitz.open("pdf", pdfbytes)
doc.insertPDF(imgpdf)
doc.save("2.pdf")
doc.close()