import PyPDF2

with open('COA_Problem_Statement(1).pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    
with open('pdf_content.txt', 'w', encoding='utf-8') as f:
    f.write(text)

print("PDF content extracted to pdf_content.txt")
