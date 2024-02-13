import os 
import PyPDF2

#add base file path
base_path = ''

#add file names from path
file_names = []

# add file names to base path
pdfFiles = [base_path + name for name in file_names]
            
# Sorting the files by forcing everything to lower case.
pdfFiles.sort(key=str.lower)

# Assigning the pdfWriter() function to pdfWriter.
pdfWriter = PyPDF2.PdfWriter()

for filename in pdfFiles:
  # Opens each of the file paths in filename variable.
  pdfFileObj = open(filename, 'rb') 
  # Read and store each of the files
  pdfReader = PyPDF2.PdfReader(pdfFileObj) 
  for pageNum in range(0, len(pdfReader.pages)):
    pageObj = pdfReader.pages[pageNum]
    # Add current PDF to a new page.
    pdfWriter.add_page(pageObj) 

# Name of the PDF file can be written here.
pdfOutput = open('Paul Bodner Application.pdf', 'wb') 

# Writing the output file using the pdfWriter function.
pdfWriter.write(pdfOutput)
pdfOutput.close()