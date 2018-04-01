# import pdfcrowd

# # def create_pdf(url):
#
# try:
#     # create the API client instance
#     client = pdfcrowd.HtmlToPdfClient('quangnn', 'ca74aa6580bd6ab6c1e80b0954cab851')
#     # run the conversion and write the result to a file
#     client.convertUrlToFile('https://lazy-cv-test.herokuapp.com/preview', 'test.pdf')
#     # pdfcrowd-> setPageHeight("-1")
#
# except pdfcrowd.Error as why:
# #    report the error to the standard error stream
#    sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))

#
#
import pdfcrowd
import sys

try:
    # create the API client instance
    client = pdfcrowd.HtmlToPdfClient('quangnn', 'ca74aa6580bd6ab6c1e80b0954cab851')

    # run the conversion and write the result to a file
    client.convertFileToFile('templates\CV_detail_page3\CV_form_edit.html', 'mycv.pdf')
except pdfcrowd.Error as why:
    # report the error to the standard error stream
    sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))
