#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 12, 2016
# Last update :
#

# Imports
from io import BytesIO
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def gen_pdf():
    # there are 66 slides (1.jpg, 2.jpg, 3.jpg...)
    path = 'images/{0}.png'
    pdf = PdfFileWriter()

    for num in range(1, 3):  # for each slide
        # Using ReportLab Canvas to insert image into PDF
        imgTemp = BytesIO()
        imgDoc = canvas.Canvas(imgTemp, pagesize=A4)
        # Draw image on Canvas and save PDF in buffer
        imgDoc.drawImage(path.format(num), -25, -45)
        # x, y - start position
        # in my case -25, -45 needed
        imgDoc.save()
        # Use PyPDF to merge the image-PDF into the template
        pdf.addPage(PdfFileReader(BytesIO(imgTemp.getvalue())).getPage(0))

    pdf.write(open("image.pdf","wb"))


if __name__ == '__main__':
    gen_pdf()