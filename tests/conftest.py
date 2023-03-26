
import os
import pytest
from zipfile import ZipFile


@pytest.fixture(scope='session', autouse=True)
def path_():
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path_download = os.path.join(base_path, 'downloads')
    path_resourse = os.path.join(base_path, 'resourse')
    return [base_path, path_download, path_resourse]


@pytest.fixture(scope='function')
def open_archive(path_):
    with ZipFile(os.path.join(path_[2], 'example.zip'), 'r') as file_zip:
        yield file_zip
        file_zip.close()


# @pytest.fixture(scope='function', autouse=True)

