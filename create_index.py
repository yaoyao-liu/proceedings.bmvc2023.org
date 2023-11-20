import xlrd
import pdb
import os

book = xlrd.open_workbook("CameraReadyPapers.xls")

sh = book.sheet_by_index(0)

if os.path.exists("index.html"):
    os.system("rm index.html")
f = open('index.html', "a")

f.write('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"><meta name="description" content="The website for the 34th British Machine Vision Conference."><script src="/cdn-cgi/apps/head/VB9iiBJCCF8qrI8c3zDlJCb25P8.js"></script><link rel="stylesheet" href="./assets/css/bootstrap.min.css"><link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css" integrity="sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf" crossorigin="anonymous"><link rel="stylesheet" href="./assets/css/ndfc.css"><link rel="apple-touch-icon" sizes="180x180" href="./assets/favicon/apple-touch-icon.png"><link rel="icon" type="image/png" sizes="32x32" href="./assets/favicon/favicon-32x32.png"><link rel="icon" type="image/png" sizes="16x16" href="./assets/favicon/favicon-16x16.png"><link rel="manifest" href="./assets/favicon/site.webmanifest"><link rel="mask-icon" href="./assets/favicon/safari-pinned-tab.svg" color="#5bbad5"><meta name="msapplication-TileColor" content="#da532c"><meta name="theme-color" content="#ffffff"><title>The 33rd British Machine Vision Conference 2023: Papers</title></head><header></header><body>')

f.write('<nav class="navbar sticky-top navbar-expand-md navbar-dark bg-primary"><div class="container"><a class="navbar-brand" href="https://bmvc2023.org/"><b class="ndfc-brand-light">BMVC&thinsp;2023</b></a><button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button><div class="collapse navbar-collapse" id="navbarNavDropdown"><ul class="navbar-nav mr-auto"></ul><ul class="navbar-nav"></ul></div> </div></nav>')


f.write('<div class="container m-t-2"><div class="page-header" style="padding-bottom: 9px; margin: 20px 0 20px; border-bottom: 1px solid #eee;"><div class="row align-items-center"><div class="col-xs-12 mx-auto"><h1 style="text-align: center;">The 34<sup>th</sup> British Machine Vision Conference Proceedings</h1></div></div></div></div><main role="main" class="container"><div class="row pl-2 pr-2 pt-2 pb-2 mx-auto justify-content-left"><table class="table table-striped table-bordered" style=""><tbody><a style="visibility: hidden;">-1</a>')

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

        f.write('<tr id="paper"><td class="text-center"><strong> </strong><br /><span style="opacity: 0.5;"><strong>' + paper_id_str_short + '</strong></span></td><td><strong><a href="' + 'https://bmvc2023.mpi-inf.mpg.de/' + paper_id_str_short +'/">' + paper_title + '</a></strong><br />' + paper_authors + '<br />')

        if os.path.exists('./' + paper_id_str + '.pdf'):
            f.write('<a class="btn btn-primary btn-sm mt-1" href="' + 'https://bmvc2023.mpi-inf.mpg.de/BMVC2023/' + paper_id_str + '.pdf' + '" role="button">PDF</a>&nbsp;')
        if os.path.exists('./' + paper_id_str + '_poster.pdf'):
            f.write('<a class="btn btn-primary btn-sm mt-1" href="' + 'https://bmvc2023.mpi-inf.mpg.de/BMVC2023/' + paper_id_str + '_poster.pdf' + '" role="button">Poster</a>&nbsp;')
        if os.path.exists('./' + paper_id_str + '_video.mp4'):
            f.write('<a class="btn btn-primary btn-sm mt-1" href="' + 'https://bmvc2023.mpi-inf.mpg.de/BMVC2023/' + paper_id_str + '_video.mp4' + '" role="button">Video</a>&nbsp;')
        if os.path.exists('./' + paper_id_str + '_supp.zip'):
            f.write('<a class="btn btn-primary btn-sm mt-1" href="' + 'https://bmvc2023.mpi-inf.mpg.de/BMVC2023/' + paper_id_str + '_supp.zip' + '" role="button">Supplementary</a>&nbsp;')
        if os.path.exists('./' + paper_id_str + '_supp.pdf'):
            f.write('<a class="btn btn-primary btn-sm mt-1" href="' + 'https://bmvc2023.mpi-inf.mpg.de/BMVC2023/' + paper_id_str + '_supp.pdf' + '" role="button">Supplementary</a>&nbsp;')
        if paper_github != '[Not Answered]':
            f.write('<a class="btn btn-primary btn-sm mt-1" href="' + paper_github + '" role="button">Code</a>&nbsp;')
        f.write('</td></tr>\n')

f.write('</tbody></table></div></main><footer class="footer bg-light"><div class="container"><div class="row align-items-center footer-row"><div class="col-xs-12 col-sm-12 col-lg-5 col-xl-5 pb-2 pt-2"><b>© 2023 The <a href="https://britishmachinevisionassociation.github.io/">BMVA</a></b><br><a href="https://imprint.mpi-klsb.mpg.de/inf/bmvc2022.mpi-inf.mpg.de">Imprint</a> &nbsp; <a href="https://data-protection.mpi-klsb.mpg.de/inf/bmvc2022.mpi-inf.mpg.de?lang=en">Data Protection</a></div><div class="col-xs-12 col-sm-12 col-lg-5 col-xl-7 pb-2 pt-2" style="font-size:10px;">The British Machine Vision Conference is organised by <a href="https://britishmachinevisionassociation.github.io/">The British Machine Vision Association and Society for Pattern Recognition</a>. The Association is a Company limited by guarantee, No.2543446, and a non-profit-making body, registered in England and Wales as Charity No.1002307 (Registered Office: Dept. of Computer Science, Durham University, South Road, Durham, DH1 3LE, UK).<br><p hidden><script type="text/javascript" id="clstr_globe" src="//clustrmaps.com/globe.js?d=wzUkN24cyDxLTiWGAKIGs6eT1DdKPGAZctgXfZX1Qxs"></script></p></div></div></footer><script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script src="/assets/js/jquery-3.5.1.slim.min.js"></script><script src="/assets/js/popper.min.js"></script><script src="/assets/js/bootstrap.min.js"></script><script src="/assets/js/jquery.date-filter.min.js"></script><script>$(document).ready(function(){/*console.log("Hello");*//*console.log($(".date-filter"));*/$(".date-filter").dateFilter();$(".date-older-filter").dateOlderFilter();});</script></body></html>')     
        
f.close()
