import PyPDF2,regex
file_handle = open("SenseandSensibility.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(file_handle)

book = "".join([ regex.sub(r'[^[[:alpha:]|\s]', "", pdfReader.getPage(i).extractText().replace("\n"," ").replace("Full Text Archive https://www.fulltextarchive.com","").replace("CHAPTER","").lower()) for i in range(pdfReader.numPages) ]).split()[6:-4]
hist = {}

for i in book:
	if i in hist:
		hist[i] += 1
	else:
		hist[i] = 1
print(hist)
