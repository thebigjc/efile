import re
import os
import os.path

# Regular expression for pattern matching invoice numbers
invoice_pattern = re.compile(r'W\d\d\d\d\d\d\d')

# Get current path
my_path = os.getcwd()

def get_invoice_pattern(pdfname):
    """
    Given the name of an ocr'd pdf return the invoice number
    """
    txt_name = get_txt_filename(pdfname)
    file = open(txt_name)
    filestring = file.read()
    match = invoice_pattern.search(filestring)
    if match:
        return match.group()
    else:
        print("Can't find pattern")
        return null


def get_directory_contents(path):
    only_files = [f for f in os.listdir(my_path) if path.isfile(path.join(my_path, f))]
    return only_files


def get_pdf_list(files_in_directory):
    pdflist = []
    for current_file in files_in_directory:
        if re.search(r'.pdf', current_file):
            pdflist.append(current_file)
    return pdflist


def get_txt_filename(pdf_name):
    name_length = len(pdf_name)
    new_name = pdf_name[0:name_length - 3] + "txt"
    return new_name


def make_txt_file(pdf_name):
    os.system("pdftotext \"" + pdf_name + "\"")


def rename_pdf(pdf_name):
    make_txt_file(pdf_name)
    new_name = get_invoice_pattern(pdf_name) + ".pdf"
    os.remove(get_txt_filename(pdf_name))
    os.renames(pdf_name, new_name)


def rename_pdf_directory(pdf_list):
    for pdf_name in pdf_list:
        rename_pdf(pdf_name)


## renamepdfdirectory(getpdflist(getdirectorycontents(mypath)))
print get_directory_contents(my_path)
