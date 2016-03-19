import gzip


def Zipper(filename):
    inf = open(filename, 'rb')
    outf = gzip.open(filename + '.gz', 'wb')
    outf.write(inf.read())
    outf.close()
    inf.close()
