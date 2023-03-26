import csv
import os
from io import TextIOWrapper
from zipfile import ZipInfo, ZipFile

import pytest


# base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# path_download = os.path.join(base_path, 'downloads')
# path_resourse = os.path.join(base_path, 'resourse')


def size_file(name_file, path_, num_path_in_list):
    size_file = os.path.getsize(os.path.join(path_[num_path_in_list], name_file))
    return int(size_file)


def test_count_files_in_archive_and_size(open_archive, path_):
    size_zip = size_file(name_file='example.zip', path_=path_, num_path_in_list=2)
    assert size_zip == 1072000, f"Неверный размер архива, {size_zip} не равно 1072000"
    assert len(open_archive.filelist) == 5, f"Неверное кол-во файлов в архиве, {len(open_archive.filelist)} не равно 5"


def test_read_and_content_to_csv(open_archive, path_):
    zip_file = ZipFile(os.path.join(path_[2], 'example.zip'))
    with zip_file.open('SampleCSVFile_11kb.csv') as file:
        text = csv.reader(TextIOWrapper(file))
        list_csv = []
        for row in text:
            str_ = ','.join(row).replace(',', ',', 5)
            list_csv.append(str_)
    assert "5,Holmes HEPA Air Purifier,Carlos Soltero,515,30.94,21.78,5.94,Nunavut,Appliances,0.5" in list_csv

