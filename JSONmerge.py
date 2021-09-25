from glob import glob
from os import makedirs, path, walk
from pathlib import Path
import json

# Directories
input_dir = r'C:\Users\erics\Downloads\products_testen\en'
output_file = r'C:\Users\erics\Downloads\products_testen\output_file.json'

# Get array of files
#files = glob(path.join(input_dir, "**", "*.json"))


#filenames = next(walk(input_dir), (None, None, []))[2]  # [] if no file

files = glob(r'C:\Users\erics\Downloads\products_testen\en\*.json')

with open(output_file,'w') as o:
    o.write('[')
    for infile in files[:-1]: # loop over all files except the last one
        with open(infile,'r') as i:
            o.write(i.read().strip() + ',\n')
    with open(files[-1]) as i: # special treatement for last file
        o.write(i.read().strip() + ']\n')