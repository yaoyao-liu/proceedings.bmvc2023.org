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

        paper_authors = paper_authors.replace(");", "),");
        paper_authors = paper_authors.replace(")*;", "),*");

        f.write('<tr id="paper"><td class="text-center"><strong> </strong><br /><span style="opacity: 0.5;"><strong>' + paper_id_str_short + '</strong></span></td><td><strong><a href="' + 'http://proceedings.bmvc2023.org/' + paper_id_str_short +'/">' + paper_title + '</a></strong><br />' + paper_authors + '<br />')

        if os.path.exists('./' + paper_id_str + '.pdf'):
            f.write('<a class="btn btn-primary btn-sm mt-1" href="' + 'https://papers.bmvc2023.org/' + paper_id_str + '.pdf' + '" role="button">PDF</a>&nbsp;')
        if os.path.exists('./' + paper_id_str + '_poster.pdf'):
            f.write('<a class="btn btn-primary btn-sm mt-1" href="' + 'https://bmvc2022.mpi-inf.mpg.de/BMVC2023/' + paper_id_str + '_poster.pdf' + '" role="button">Poster</a>&nbsp;')
        if os.path.exists('./' + paper_id_str + '_video.mp4'):
            f.write('<a class="btn btn-primary btn-sm mt-1" href="' + 'https://bmvc2022.mpi-inf.mpg.de/BMVC2023/' + paper_id_str + '_video.mp4' + '" role="button">Video</a>&nbsp;')
        if os.path.exists('./' + paper_id_str + '_supp.zip'):
            f.write('<a class="btn btn-primary btn-sm mt-1" href="' + 'https://bmvc2022.mpi-inf.mpg.de/BMVC2023/' + paper_id_str + '_supp.zip' + '" role="button">Supplementary</a>&nbsp;')
        if os.path.exists('./' + paper_id_str + '_supp.pdf'):
            f.write('<a class="btn btn-primary btn-sm mt-1" href="' + 'https://bmvc2022.mpi-inf.mpg.de/BMVC2023/' + paper_id_str + '_supp.pdf' + '" role="button">Supplementary</a>&nbsp;')
        if paper_github != '[Not Answered]':
            f.write('<a class="btn btn-primary btn-sm mt-1" href="' + paper_github + '" role="button">Code</a>&nbsp;')
        f.write('</td></tr>\n')

f.write('</tbody></table></div></main><footer class="footer bg-light"><div class="container"><div class="row align-items-center footer-row"><div class="col-xs-12 col-sm-12 col-lg-5 col-xl-5 pb-2 pt-2"><b>© 2023 The <a href="https://britishmachinevisionassociation.github.io/">BMVA</a></b><br><a href="https://imprint.mpi-klsb.mpg.de/inf/bmvc2022.mpi-inf.mpg.de">Imprint</a> &nbsp; <a href="https://data-protection.mpi-klsb.mpg.de/inf/bmvc2022.mpi-inf.mpg.de?lang=en">Data Protection</a></div><div class="col-xs-12 col-sm-12 col-lg-5 col-xl-7 pb-2 pt-2" style="font-size:10px;">The British Machine Vision Conference is organised by <a href="https://britishmachinevisionassociation.github.io/">The British Machine Vision Association and Society for Pattern Recognition</a>. The Association is a Company limited by guarantee, No.2543446, and a non-profit-making body, registered in England and Wales as Charity No.1002307 (Registered Office: Dept. of Computer Science, Durham University, South Road, Durham, DH1 3LE, UK).<br><p hidden><script type="text/javascript" id="clstr_globe" src="//clustrmaps.com/globe.js?d=wzUkN24cyDxLTiWGAKIGs6eT1DdKPGAZctgXfZX1Qxs"></script></p></div></div></footer><script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script src="/assets/js/jquery-3.5.1.slim.min.js"></script><script src="/assets/js/popper.min.js"></script><script src="/assets/js/bootstrap.min.js"></script><script src="/assets/js/jquery.date-filter.min.js"></script><script>$(document).ready(function(){/*console.log("Hello");*//*console.log($(".date-filter"));*/$(".date-filter").dateFilter();$(".date-older-filter").dateOlderFilter();});</script></body></html>')     
        
f.close()


book = xlrd.open_workbook("CameraReadyPapers.xls")

sh = book.sheet_by_index(0)

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

        author_list = paper_authors.split(";")

        all_author_names = []
        for author in author_list:
            author_name = author[:author.find('(')-1]
            all_author_names.append(author_name)

        paper_authors = paper_authors.replace(");", "),");
        paper_authors = paper_authors.replace(")*;", "),*");

        if os.path.exists(paper_id_str_short) != True:
            os.mkdir(paper_id_str_short)

        if os.path.exists(paper_id_str_short+"/index.html"):
            os.system("rm " + paper_id_str_short+"/index.html")
        f = open(paper_id_str_short+"/index.html", "a")
        f.write('<!DOCTYPE html><html lang="en-US"><head><meta charset="utf-8" /><meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" /><title>')
        f.write(paper_title)
        f.write('</title><link rel="stylesheet" href="../assets/css/style.css"><link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon/favicon-32x32.png"><link rel="icon" type="image/png" sizes="16x16" href="/assets/favicon/favicon-16x16.png"></head><body><div class="wrapper"><section><center><a href="../"><img src="../images/bmvc-logo.png" width="200" class="figure-img img-responsive center-block"></a><br /><br /></center><h2 class="project-name" style="font-weight:normal; font-size: 167%;" align="center">')
        f.write(paper_title)
        f.write('</h2><br><h5 style="font-weight:normal" align="center"><autocolor>')
        f.write(paper_authors)
        f.write('</autocolor></h5><h5 style="font-weight:normal;" align="center"><a href="http://bmvc2022.mpi-inf.mpg.de/BMVC/" target="_blank" ><I><autocolor>The 34<sup>th</sup> British Machine Vision Conference</autocolor></I></a></h5><div class="cta">')
        if os.path.exists('./' +  paper_id_str + '.pdf'):
            f.write('<a href="https://papers.bmvc2023.org/')
            f.write(paper_id_str + '.pdf')
            f.write('" role="button">PDF</a>')
        if os.path.exists('./' +  paper_id_str + '_poster.pdf'):
            f.write('<a href="https://bmvc2022.mpi-inf.mpg.de/BMVC2023/')
            f.write(paper_id_str + '_poster.pdf')
            f.write('" role="button">Poster</a>')
        if os.path.exists('./' +  paper_id_str + '_video.mp4'):
            f.write('<a href="https://bmvc2022.mpi-inf.mpg.de/BMVC2023/')
            f.write(paper_id_str + '_video.mp4')
            f.write('" role="button">Video</a>')
        if os.path.exists('./' +  paper_id_str + '_supp.zip'):
            f.write('<a href="https://bmvc2022.mpi-inf.mpg.de/BMVC2023/')
            f.write(paper_id_str + '_supp.zip')
            f.write('" role="button">Supplementary</a>')
        if os.path.exists('./' +  paper_id_str + '_supp.pdf'):
            f.write('<a href="https://bmvc2022.mpi-inf.mpg.de/BMVC2023/')
            f.write( paper_id_str + '_supp.pdf')
            f.write('" role="button">Supplementary</a>')
        if paper_github != '[Not Answered]':
            f.write('<a href="')
            f.write(paper_github)
            f.write('" role="button">Code</a>')
        f.write('<br></div><h2 id="abstract">Abstract</h2>')
        f.write(paper_abstract)
        f.write('<br><br>')

        if os.path.exists('./' +  paper_id_str + '_video.mp4'):
            f.write('<h2>Video</h2><center><iframe height="540" width="960" style="max-width:100%;max-height:100%;" src="https://bmvc2022.mpi-inf.mpg.de/BMVC2023/' + paper_id_str + '_video.mp4' + '" frameborder="0" allow="encrypted-media" allowfullscreen></iframe></center><br><br>')

        f.write('<h2>Citation</h2><div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>@inproceedings{')

        first_author_name = all_author_names[0].split(" ")[-1]

        f.write(first_author_name+'_2023_BMVC,\n')
        f.write('author    = {')
        for author_name_idx in range(len(all_author_names)):
            author_name = all_author_names[author_name_idx]
            if author_name_idx != len(all_author_names)-1:
                f.write(author_name + ' and')
            else:
                f.write(author_name + '},\n')
        f.write('title     = {'+paper_title+'},\n')
        f.write('booktitle = {34th British Machine Vision Conference 2023, {BMVC} 2023, Aberdeen, UK, November 20-24, 2023},\n')
        f.write('publisher = {BMVA},\n')
        f.write('year      = {2023},\n')
        f.write('url       = {https://papers.bmvc2023.org/' + paper_id_str + '.pdf' + '}\n')
        f.write('}\n')
        f.write('</code></pre></div></div>')

        f.write('<br><br><p><small>Copyright &copy 2023 <a href="https://britishmachinevisionassociation.github.io/" rel="noopener"><autocolor>The British Machine Vision Association and Society for Pattern Recognition</autocolor></a><br>The British Machine Vision Conference is organised by <a href="https://britishmachinevisionassociation.github.io/"><autocolor>The British Machine Vision Association and Society for Pattern Recognition</autocolor></a>. The Association is a Company limited by guarantee, No.2543446, and a non-profit-making body, registered in England and Wales as Charity No.1002307 (Registered Office: Dept. of Computer Science, Durham University, South Road, Durham, DH1 3LE, UK).</small></p><p><small><a href="https://imprint.mpi-klsb.mpg.de/inf/bmvc2022.mpi-inf.mpg.de" rel="noopener"><autocolor>Imprint</autocolor></a> | <a href="https://data-protection.mpi-klsb.mpg.de/inf/bmvc2022.mpi-inf.mpg.de?lang=en" rel="noopener"><autocolor>Data Protection</autocolor></a></small></p></section></div></body></html>')
        f.close()
        #pdb.set_trace()


#pdb.set_trace()