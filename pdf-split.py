# 拆分后的pdf文件大小没变，需要wps等打开文件打印或者另存为，之后的文件明显变小
from  PyPDF2 import PdfReader,PdfWriter

# # pdf 文档
pdf_path = "all.pdf"
save_path = './'

# Split Pages of PDF
pdf_reader = PdfReader(pdf_path)
start = 0
for i in range(0, len(pdf_reader.pages)):
    if i != 0 and (i % 100 == 0 or i == len(pdf_reader.pages) - 1):
        pdf_writer = PdfWriter()
        for j in range(start, i + 1):
            pdf_writer.add_page(pdf_reader.pages[j])
        # Every page write to a path
        with open(save_path+'{}.pdf'.format(str(i)), 'wb') as fh:
            pdf_writer.write(fh)
            print('{} Save Sucessfully !\n'.format(str(i)))
        start = i + 1
