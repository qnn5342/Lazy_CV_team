import pdfcrowd
import sys

try:
    # create the API client instance
    client = pdfcrowd.HtmlToPdfClient('quangnn', 'ca74aa6580bd6ab6c1e80b0954cab851')

    # run the conversion and write the result to a file
    client.convertUrlToFile('https://lazy-cv-test.herokuapp.com/', 'test.pdf')
except pdfcrowd.Error as why:
    # report the error to the standard error stream
    sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))

#
#
# import pdfcrowd
# import sys
#
# try:
#     # create the API client instance
#     client = pdfcrowd.HtmlToPdfClient('quangnn', 'ca74aa6580bd6ab6c1e80b0954cab851')
#
#     # run the conversion and write the result to a file
#     client.convertFileToFile('girl.html', 'mygirls.pdf')
# except pdfcrowd.Error as why:
#     # report the error to the standard error stream
#     sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))
