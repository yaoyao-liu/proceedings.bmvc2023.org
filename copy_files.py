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

        if os.path.exists('./' + paper_id_str + '.pdf'):
            os.system('cp ' + './' + paper_id_str + '.pdf' + ' ./papers/' + paper_id_str + '.pdf')

        """
        if os.path.exists('./' + paper_id_str_short + '/CameraReady/' + paper_id_str + '.pdf'):
            os.system('cp ' + './' + paper_id_str_short + '/CameraReady/' + paper_id_str + '.pdf' + ' ./' + paper_id_str + '.pdf')
        if os.path.exists('./' + paper_id_str_short + '/CameraReady/' + paper_id_str + '_poster.pdf'):
            os.system('cp ' + './' + paper_id_str_short + '/CameraReady/' + paper_id_str + '_poster.pdf' + ' ./' + paper_id_str + '_poster.pdf')
        if os.path.exists('./' + paper_id_str_short + '/CameraReady/' + paper_id_str + '_video.mp4'):
            os.system('cp ' + './' + paper_id_str_short + '/CameraReady/' + paper_id_str + '_video.mp4' + ' ./' + paper_id_str + '_video.mp4')
        if os.path.exists('./' + paper_id_str_short + '/CameraReady/' + paper_id_str + '_supp.zip'):
            os.system('cp ' + './' + paper_id_str_short + '/CameraReady/' + paper_id_str + '_supp.zip' + ' ./' + paper_id_str + '_supp.zip')
        if os.path.exists('./' + paper_id_str_short + '/CameraReady/' + paper_id_str + '_supp.pdf'):
            os.system('cp ' + './' + paper_id_str_short + '/CameraReady/' + paper_id_str + '_supp.pdf' + ' ./' + paper_id_str + '_supp.pdf')
        """

        #os.system('rm -rf ' + './' + paper_id_str_short + '/CameraReady/*')
    