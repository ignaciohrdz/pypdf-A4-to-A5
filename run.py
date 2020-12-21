from PyPDF2 import PdfFileReader, PdfFileWriter
import os

def prepare_A4toA5(path):
    pdf_in = PdfFileReader(path)
    pdf_out = PdfFileWriter()

    num_pages = pdf_in.getNumPages()
    pages = range(3,num_pages,4)
    for p in pages:
        pdf_out.addPage(pdf_in.getPage(p-3))
        pdf_out.addPage(pdf_in.getPage(p))
        pdf_out.addPage(pdf_in.getPage(p-1))
        pdf_out.addPage(pdf_in.getPage(p-2))
    
    # Dealing with the remaining pages
    remain_pages = pdf_in.getNumPages() % 4
    if remain_pages != 0:
        last_page = pdf_in.getNumPages() // 4
        pdf_out.addPage(pdf_in.getPage(last_page+1))
        
        if remain_pages == 4:
            pdf_out.addPage(pdf_in.getPage(last_page+4))
        else:
            pdf_out.addBlankPage()

        if remain_pages == 3:
            pdf_out.addPage(pdf_in.getPage(last_page+3))
        else:
            pdf_out.addBlankPage()

        if remain_pages == 2:
            pdf_out.addPage(pdf_in.getPage(last_page+2))
        else:
            pdf_out.addBlankPage()
        
    path_out = path.replace('.pdf','_preparedA5.pdf').replace('input','output')
    with open(path_out, 'wb') as out:
        print('Saving as ' + path_out + '...')
        pdf_out.write(out)
        print('Done.')



files = os.listdir("input")

print('-'*50)
print('Python PDF - Convert A4 to A5 book ready to print')
print('-'*50)
print('\nThese are the files I found: \n')
print(*files, sep="\n")
print('\nWhich one do you want to use? (0 to {})'.format(len(files)-1))
numdoc = int(input())

if numdoc >= 0 and numdoc <= len(files):
    numdoc = numdoc
else:
    print('[Error]: taking the first document (0)')
    numdoc = 0

doc_name = files[numdoc]
print('Preparing ' + doc_name + '...')
prepare_A4toA5(os.path.join('input',doc_name))



