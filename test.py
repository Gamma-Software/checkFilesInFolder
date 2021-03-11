import os
import pytest
from main import get_files_from_folder, compare_files


def test_get_files_from_folder():
    # Folder A
    assert get_files_from_folder(os.getcwd()+"/tests/folderA/") == ['file.yml', 'file1.txt', 'file2.yaml']
    # Folder B
    assert get_files_from_folder(os.getcwd()+"/tests/folderB/") == ['file.yml', 'file1.txt', 'file2.yaml']
    # Folder C
    assert get_files_from_folder(os.getcwd()+"/tests/folderC/") == ['file.yml', 'file1.txt', 'file2.yaml']
    # Folder D
    assert get_files_from_folder(os.getcwd()+"/tests/folderD/") == []
    # Folder E
    assert get_files_from_folder(os.getcwd()+"/tests/folderE/") == ['file.yml', 'file1.txt', 'file2.yaml', 'file3.csv']
    # Folder F
    assert get_files_from_folder(os.getcwd()+"/tests/folderF/") == ['file2.yaml']


def test_compare_files():
    list1 = ['file.yml', 'file1.txt', 'file2.yaml']
    list2 = ['file.yml', 'file1.txt']
    list3 = ['file.yml']
    list4 = []
    list5 = ['file1.txt', 'file2.yaml', 'file.yml', 'file3.yml', 'file4.csv']
    list6 = ['file1.txt', 'file2.yaml', 'file.yml']
    list7 = ['file.yml', 'file.txt']
    list8 = ['file2.yml']
    assert len(compare_files(list1, list1)) == 0
    assert len(compare_files(list1, list6)) == 0
    assert len(compare_files(list1, list7)) != 0
    assert len(compare_files(list3, list8)) != 0
    assert len(compare_files(list3, list8)) != 0
    for list_to_compare in [list2, list3, list4, list5, list7, list8]:
        assert len(compare_files(list1, list_to_compare)) != 0
