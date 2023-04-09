
import os


def path_():
    current_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    resourses_dir = os.path.join(current_dir, 'resourses')
    downloads_dir = os.path.join(resourses_dir, 'downloads')
    return [downloads_dir, resourses_dir, current_dir]


def size_files(name_file, num_path_in_list):
    path = path_()
    size_file = os.path.getsize(os.path.join(path[num_path_in_list], name_file))
    return size_file


def size_file_zip():
    size_zip = size_files(name_file="example.zip", num_path_in_list=1)
    return int(size_zip)
