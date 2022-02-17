# Create a python scripts that combines lot os pdf input into
import PyPDF2
import sys

#Take all the arguement
inputs = sys.argv[1:]


# create a function that merge all the pdfs
def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write("combined_Files.pdf")

pdf_combiner(inputs)

 # adding watermarks to the pdf

# the files will want tot add th water mark to
templaye = PyPDF2.PdfFileReader(open("combined_Files,", "rb"))

# open the watermark document
watermark = PyPDF2.PdfFileReader(open("wtr.pdf","rb"))

#output file
output = PyPDF2.PdfFileWriter()


# creating a function that loop through the file and watermark to be added
for i in range(template.getNumpages()):
    """
    looping through the doc to get number of pages
    """
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0)) # get the watermark form the first page
    output.addPage(page)

    with open('watermarked_output.pdf','wb') as file:
        output.write(file)




""""
with open("Pdfiles/dummy.pdf", "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)

"""
