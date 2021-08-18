'''
author: mujeebishaque
Description: Converts all the png's found in the dir or in nested directory into PDF's.
Pre-requisite: pip install pillow
'''

import pathlib, os
import PIL.Image
from tkinter import filedialog, messagebox
from tkinter import *
import multiprocessing

def select_folder():
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    return folder_selected

def retrieve_pngs():
    result = list(pathlib.Path(select_folder()).glob('**/*.png'))
    return result

def get_binary_list():
    _list = retrieve_pngs()
    return _list[len(_list)//2:], _list[:len(_list)//2]

def convert_pngs(_first):
    
    for file in _first:
        _head, _tail = str(file).split('.')
        _title = _head.split(os.sep)[-1]
        image1 = PIL.Image.open(str(file))
        im1 = image1.convert('RGB')
        im1.save(_head+'.pdf')
        print(f"> processed and saved {_title}.pdf  . . .")

PROCESSES = []

def convert_to_pdf():
    _first, _last = get_binary_list()
    proc_1 = multiprocessing.Process(target=convert_pngs, args=[_first])
    proc_2 = multiprocessing.Process(target=convert_pngs, args=[_last])
    proc_1.start()
    proc_2.start()
    PROCESSES.append(proc_1)
    PROCESSES.append(proc_2)

def main():
    convert_to_pdf()
    for p in PROCESSES:
        p.join()

if __name__ == '__main__':
    main()