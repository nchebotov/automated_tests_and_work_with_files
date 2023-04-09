
import os
import pytest
from zipfile import ZipFile
from automated_tests_and_work_with_files.utils import file_management_utility


@pytest.fixture(scope='function')
def open_archive():
    path = file_management_utility.path_()[1]
    with ZipFile(os.path.join(path, 'example.zip'), 'r') as file_zip:
        yield file_zip
        file_zip.close()
