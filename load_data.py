from PIL import Image
import pdf2image
import os
import shutil
from glob import glob

import numpy as np
import re

import pandas as pd
from matplotlib import pyplot as plt


DATA_PATH = "./data/"
UK_PATH = "UK_Patents"
US_PATH = "US_Patents"



def save_pdf_to_tif(path, output_folder, name, format_=".tif", dpi=600):
    pil_images = pdf2image.convert_from_path(path, dpi=dpi, output_folder=output_folder)
    index = 1
    for image in pil_images:
        image.save(output_folder + name + str(index) + format_)
        index += 1

def data_pdftopil(corpus_root=DATA_PATH):
    print("Expected structure is :\n\
          ./data/country_directory/patent.pdf")
    patents = []
    patents_indexer = []
    pos = 0

    for country in os.listdir(corpus_root):
        path = corpus_root + country # ./data/country_directory 
        if(os.path.isdir(path)): # Filter potential additional files (zip, informative files..)
            for dir_ in os.listdir(path):
                patent_path = path + "/" + dir_
                name, ext = os.path.splitext(dir_)
                if (ext == ".pdf"): # .data/country_directory/patent.pdf
                    pdf = patent_path
                    print(pdf)
                    future_path = path+ "/" + name + "/"
                    try:
                        os.mkdir(future_path)
                        print(f"Directory {name} created")
                    except OSError as error:
                        print(error)  
                    save_pdf_to_tif(pdf, future_path, name)
                    shutil.move(pdf, future_path+ dir_)
                    for file in glob(future_path + "*.ppm"):
                        os.remove(file)
    return patents, patents_indexer 



def load_patents(corpus_root=DATA_PATH):
    print("Expected structure is :\n\
          ./data/country_directory/patent_directory/pages.tif")
    patents = []
    patents_indexer = []
    pos = 0

    for country in os.listdir(corpus_root):
        path = corpus_root + country # ./data/country_directory 
        if(os.path.isdir(path)): # Filter potential additional files (zip, informative files..)
            for dir_ in os.listdir(path):
                patent_path = path + "/" + dir_
                if(os.path.isdir(patent_path)): # ./data/country_directory/patent_directory
                    n = len(os.listdir(patent_path))
                    i = 0
                    for page in os.listdir(patent_path):
                        name, ext = os.path.splitext(page)
#                        print(f"{page} --- {name} --- {ext}")
                        if ext == ".tif":
                            with Image.open(patent_path+"/"+page) as im: 
                                patents.append(np.array(im))
                                part = f"_part{i+1}" if (n > 1) else ""
                                patents_indexer.append((dir_, dir_+part, pos))
                                pos += 1
                                i += 1
    return patents, patents_indexer 
data_pdftopil()
patents, patents_indexer = load_patents()
print("======================")
print(patents_indexer)
