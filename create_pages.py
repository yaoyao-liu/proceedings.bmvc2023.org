import xlrd
import pdb
import os

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

        f = open('paper_' + paper_id_str+".html", "a")
        f.write('<!DOCTYPE html><html lang="en-US"><head><meta charset="utf-8" /><meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" /><title>')
        f.write(paper_title)
        f.write('</title><link rel="stylesheet" href="../assets/css/style.css"><link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon/favicon-32x32.png"><link rel="icon" type="image/png" sizes="16x16" href="/assets/favicon/favicon-16x16.png"></head><body><div class="wrapper"><section><center><a href="../"><img src="../images/bmvc-logo.png" width="200" class="figure-img img-responsive center-block"></a><br /><br /></center><h2 class="project-name" style="font-weight:normal; font-size: 167%;" align="center">')
        f.write(paper_title)
        f.write('</h2><br><h5 style="font-weight:normal" align="center"><autocolor>')
        f.write(paper_authors)
        f.write('</autocolor></h5><h5 style="font-weight:normal;" align="center"><a href="http://bmvc2023.mpi-inf.mpg.de/" target="_blank" ><I><autocolor>The 34<sup>th</sup> British Machine Vision Conference</autocolor></I></a></h5><div class="cta">')
        if os.path.exists('./' +  paper_id_str + '.pdf'):
            f.write('<a href="../')
            f.write(paper_id_str + '.pdf')
            f.write('" role="button">PDF</a>')
        if os.path.exists('./' +  paper_id_str + '_poster.pdf'):
            f.write('<a href="../')
            f.write(paper_id_str + '_poster.pdf')
            f.write('" role="button">Poster</a>')
        if os.path.exists('./' +  paper_id_str + '_video.mp4'):
            f.write('<a href="../')
            f.write(paper_id_str + '_video.mp4')
            f.write('" role="button">Video</a>')
        if os.path.exists('./' +  paper_id_str + '_supp.zip'):
            f.write('<a href="../')
            f.write(paper_id_str + '_supp.zip')
            f.write('" role="button">Supplementary</a>')
        if os.path.exists('./' +  paper_id_str + '_supp.pdf'):
            f.write('<a href="../')
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
            f.write('<h2>Video</h2><center><iframe height="540" width="960" style="max-width:100%;max-height:100%;" src="https://bmvc2023.mpi-inf.mpg.de/' + paper_id_str + '_video.mp4' + '" frameborder="0" allow="encrypted-media" allowfullscreen></iframe></center><br><br>')

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
        f.write('booktitle = {33rd British Machine Vision Conference 2023, {BMVC} 2023, London, UK, November 21-24, 2023},\n')
        f.write('publisher = {{BMVA} Press},\n')
        f.write('year      = {2023},\n')
        f.write('url       = {https://bmvc2023.mpi-inf.mpg.de/' + paper_id_str + '.pdf' + '}\n')
        f.write('}\n')
        f.write('</code></pre></div></div>')

        f.write('<br><br><p><small>Copyright &copy 2023 <a href="https://britishmachinevisionassociation.github.io/" rel="noopener"><autocolor>The British Machine Vision Association and Society for Pattern Recognition</autocolor></a><br>The British Machine Vision Conference is organised by <a href="https://britishmachinevisionassociation.github.io/"><autocolor>The British Machine Vision Association and Society for Pattern Recognition</autocolor></a>. The Association is a Company limited by guarantee, No.2543446, and a non-profit-making body, registered in England and Wales as Charity No.1002307 (Registered Office: Dept. of Computer Science, Durham University, South Road, Durham, DH1 3LE, UK).</small></p><p><small><a href="https://imprint.mpi-klsb.mpg.de/inf/bmvc2022.mpi-inf.mpg.de" rel="noopener"><autocolor>Imprint</autocolor></a> | <a href="https://data-protection.mpi-klsb.mpg.de/inf/bmvc2022.mpi-inf.mpg.de?lang=en" rel="noopener"><autocolor>Data Protection</autocolor></a></small></p></section></div></body></html>')
        f.close()
        #pdb.set_trace()


#pdb.set_trace()