# encoding: utf-8

import csv
import os
from io import TextIOWrapper
from zipfile import ZipFile
from PyPDF2 import PdfReader
from openpyxl import load_workbook


def size_file(name_file, path_, num_path_in_list):
    size_file = os.path.getsize(os.path.join(path_[num_path_in_list], name_file))
    return int(size_file)


def test_count_files_in_archive_and_size(open_archive, path_):
    size_zip = size_file(name_file="example.zip", path_=path_, num_path_in_list=2)
    assert size_zip == 1072000, f"Неверный размер архива, {size_zip} не равно 1072000"
    assert len(open_archive.filelist) == 5, f"Неверное кол-во файлов в архиве, {len(open_archive.filelist)} не равно 5"


def test_read_and_content_to_csv(path_):
    zip_file = ZipFile(os.path.join(path_[2], "example.zip"))
    with zip_file.open('SampleCSVFile_11kb.csv') as file:
        text = csv.reader(TextIOWrapper(file))
        list_csv = []
        for row in text:
            str_ = ','.join(row).replace(',', ',', 5)
            list_csv.append(str_)
    assert "5,Holmes HEPA Air Purifier,Carlos Soltero,515,30.94,21.78,5.94,Nunavut,Appliances,0.5" in list_csv, \
        f"Строки {'5,Holmes HEPA Air Purifier,Carlos Soltero,515,30.94,21.78,5.94,Nunavut,Appliances,0.5'} нет" \
        f"в файле {'SampleCSVFile_11kb.csv'}"
    file.close()


def test_read_and_content_to_xlsx(path_):
    zip_file = ZipFile(os.path.join(path_[2], "example.zip"))
    with zip_file.open("file_example_XLSX_10.xlsx") as file_xlsx:
        text = load_workbook(file_xlsx)
        sheet = text.active
        assert sheet.cell(row=8, column=7).value == "15/10/2017", f"Ожидаем {'15/10/2017'}," \
                                                                  f"фактически имеем {sheet.cell(row=8, column=7).value}"
    file_xlsx.close()


def test_read_and_content_to_pdf(path_):
    zip_file = ZipFile(os.path.join(path_[2], 'example.zip'))
    with zip_file as file_zip:
        file_pdf = file_zip.extract("file-example_PDF_1MB.pdf")
        reader = PdfReader(file_pdf)
        try:
            page = reader.pages[0]
            assert "Morbi viverra semper lorem nec molestie" in page.extract_text(), \
                f"Фраза {'Morbi viverra semper lorem nec molestie'} отсутствует в файле {'file-example_PDF_1MB.pdf'}"
        finally:
            os.remove(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   'file-example_PDF_1MB.pdf'))
            file_zip.close()
