import logging
import pdftotext

logging.basicConfig(
    filename="gen_corp.log",
    format='[%(asctime)s - %(levelname)s] %(message)s',
    filemode='w',
    level=0
)

# Dictionary defining the start of
# content i.e. Prologue, in each novel
novels = {
    "1998": 0,
    "2000": 10,
    "2001": 14,
    "2003": 3,
    "2009": 17,
    "2013": 14,
    "2017": 11
}

for novel in novels:
    logging.info(f'Reading PDF {novel}.pdf')
    with open("novels/"+novel+".pdf", "rb") as f:
        pdf = pdftotext.PDF(f)

    logging.info(f'Extracting from {novel}.pdf <{novels[novel]}-{len(pdf)}>')
    pdf = [pdf[i] for i in range(novels[novel], len(pdf))]

    logging.info("Writing to CORPUS...")
    with open("novels/corpus.txt", "a") as f:
        f.write("\n".join(pdf))

logging.info("Writing finished!")
