import re
import os
import os.path

# Regular expression for pattern matching invoice numbers
invoicepattern = re.compile(r'W\d\d\d\d\d\d\d')

# Get current path
mypath = os.getcwd()


def getinvoicepattern(pdfname):
    """
    Given the name of an ocr'd pdf return the invoice number
    """
    txtname = gettxtfilename(pdfname)
    file = open(txtname)
    filestring = file.read()
    matchobject = invoicepattern.search(filestring)
    if matchobject:
        return matchobject.group()
    else:
        print("Can't find pattern")
        return null


def getdirectorycontents(path):
    onlyfiles = [f for f in os.listdir(mypath) if path.isfile(path.join(mypath, f))]
    return onlyfiles


def getpdflist(filesindirectory):
    pdflist = []
    for currentfile in filesindirectory:
        if re.search(r'.pdf', currentfile):
            pdflist.append(currentfile)
    return pdflist


def gettxtfilename(pdfname):
    namelength = len(pdfname)
    newname = pdfname[0:namelength - 3] + "txt"
    return newname


def maketxtfile(pdfname):
    os.system("pdftotext \"" + pdfname + "\"")


def renamepdf(pdfname):
    maketxtfile(pdfname)
    newname = getinvoicepattern(pdfname) + ".pdf"
    os.remove(gettxtfilename(pdfname))
    os.renames(pdfname, newname)


def renamepdfdirectory(pdflist):
    for pdfname in pdflist:
        renamepdf(pdfname)


## renamepdfdirectory(getpdflist(getdirectorycontents(mypath)))
print getdirectorycontents(mypath)
