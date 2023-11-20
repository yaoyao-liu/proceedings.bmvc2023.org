import xlrd
import pdb
import os

book = xlrd.open_workbook("CameraReadyPapers_1.xls")

sh = book.sheet_by_index(0)


if os.path.exists("sitemap.xml"):
    os.system("rm " + "sitemap.xml")
f = open('sitemap.xml', "a")

f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<urlset\n')
f.write('    xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n')
f.write('    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n')
f.write('    xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9\n')
f.write('       http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd"\n')
f.write('>\n')

for rx in range(sh.nrows):
    if rx >= 3:
        this_row = sh.row(rx)
        paper_id = int(sh.cell_value(rowx=rx, colx=0))
        paper_id_str_short = sh.cell_value(rowx=rx, colx=0)
        paper_title = sh.cell_value(rowx=rx, colx=1)
        paper_abstract = sh.cell_value(rowx=rx, colx=2)
        paper_authors = sh.cell_value(rowx=rx, colx=3)
        paper_emails = sh.cell_value(rowx=rx, colx=4)
        paper_github = sh.cell_value(rowx=rx, colx=11)

        paper_id_str = "%04d" % paper_id

        f.write('\n')
        f.write('<url>\n')
        f.write(' <loc>' + 'https://bmvc2022.mpi-inf.mpg.de/' + paper_id_str_short +'/' + '</loc>\n')
        f.write(' <priority>1.0</priority>\n')
        f.write(' <lastmod>2022-11-25</lastmod>\n')
        f.write(' <changefreq>weekly</changefreq>\n')
        f.write('</url>\n')        
        f.write('\n')

        f.write('\n')
        f.write('<url>\n')
        f.write(' <loc>' + 'https://bmvc2022.mpi-inf.mpg.de/' + paper_id_str + '.pdf' + '</loc>\n')
        f.write(' <priority>1.0</priority>\n')
        f.write(' <lastmod>2022-11-25</lastmod>\n')
        f.write(' <changefreq>weekly</changefreq>\n')
        f.write('</url>\n')        
        f.write('\n')

f.write('</urlset>')
        
f.close()


#pdb.set_trace()