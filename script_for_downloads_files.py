
import os
import time

from os.path import basename
from zipfile import ZipFile
from pathlib import Path
from selenium import webdriver
from selene.support.shared import browser
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def remove_files_in_downloads_dir():
    for file in Path('downloads').glob('*.*'):
        file.unlink()
    for file in Path('resourse').glob('*.zip'):
        file.unlink()


current_dir = os.path.dirname(os.path.abspath(__file__))

# Add options browser:
options = options.ChromiumOptions()
prefs = {
    "download.default_directory": os.path.join(current_dir, 'downloads'),
    "download.prompt_for_download": False,
    "plugins.always_open_pdf_externally": True
}
options.add_experimental_option("prefs", prefs)


# Create webdriver browser
# noinspection PyTypeChecker
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

browser.config.driver = driver


def download_files_jpeg():
    browser.open('https://demoqa.com/upload-download')
    browser.element('#downloadButton').click()


def download_file_csv():
    browser.open('https://sample-videos.com/download-sample-csv.php')
    browser.element('a[href*="Sample-Spreadsheet-100-rows.csv"]').click()


def download_file_xls_and_xlsx():
    browser.open('https://file-examples.com/index.php/sample-documents-download/sample-xls-download/')
    browser.element('a[href*="file_example_XLS_10.xls"]').click()
    time.sleep(4)
    browser.open('https://file-examples.com/index.php/sample-documents-download/sample-xls-download/')
    browser.element('a[href*="file_example_XLSX_10.xlsx"]').click()


def download_file_pdf():
    browser.open('https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/')
    browser.element('a[href*="file-example_PDF_1MB.pdf"]').click()


def archive():
    file_dir = os.listdir(os.path.join(current_dir, 'downloads'))
    path_zip = os.path.join(os.path.join(current_dir, 'resourse'), 'example.zip')
    with ZipFile(path_zip, "w") as zip_archive:
        for file in file_dir:
            add_file = os.path.join(os.path.join(current_dir, 'downloads'), file)
            zip_archive.write(add_file, basename(add_file))


if __name__ == '__main__':
    remove_files_in_downloads_dir()
    download_files_jpeg()
    download_file_csv()
    download_file_xls_and_xlsx()
    time.sleep(4)
    download_file_pdf()
    time.sleep(5)
    browser.quit()
    archive()
