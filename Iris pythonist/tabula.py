import tabula
#test 1test  


# Read pdf into a list of DataFrame
dfs = tabula.read_pdf("C:/Users/Iris/Desktop/test.pdf ", pages='all')

tabula.convert_into("C:/Users/Iris/Desktop/test.pdf", "output.csv", output_format="csv", pages='all')

# convert all PDFs in a directory
tabula.convert_into_by_batch("C:/Users/Iris/Desktop/", output_format='csv', pages='all')